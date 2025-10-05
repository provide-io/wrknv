"""
Resilience Configuration for wrknv
===================================
Retry policies, circuit breakers, and fallback chains for network operations.
"""

from __future__ import annotations

from provide.foundation.resilience import BackoffStrategy, CircuitBreaker, RetryPolicy


# GitHub API Retry Policy
GITHUB_RETRY_POLICY = RetryPolicy(
    max_retries=3,
    backoff_strategy=BackoffStrategy.EXPONENTIAL,
    initial_delay=1.0,
    max_delay=30.0,
    exceptions=(Exception,),  # Retry on any exception
)

# Download Retry Policy (more retries for downloads)
DOWNLOAD_RETRY_POLICY = RetryPolicy(
    max_retries=5,
    backoff_strategy=BackoffStrategy.EXPONENTIAL,
    initial_delay=2.0,
    max_delay=60.0,
    exceptions=(Exception,),
)

# GitHub API Circuit Breaker
github_circuit_breaker = CircuitBreaker(
    failure_threshold=5,  # Open after 5 failures
    timeout=60.0,  # Stay open for 60 seconds
    expected_exception=Exception,
)

# Download Circuit Breaker
download_circuit_breaker = CircuitBreaker(
    failure_threshold=3,  # Open after 3 failures
    timeout=30.0,  # Stay open for 30 seconds
    expected_exception=Exception,
)


def get_retry_policy(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def get_circuit_breaker(operation_type: str = "default") -> CircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)
