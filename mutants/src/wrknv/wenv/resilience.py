#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Resilience Configuration for wrknv
===================================
Retry policies, circuit breakers, and fallback chains for network operations."""

from __future__ import annotations

from provide.foundation.resilience import (
    BackoffStrategy,
    RetryPolicy,
    SyncCircuitBreaker,
)

# GitHub API Retry Policy
GITHUB_RETRY_POLICY = RetryPolicy(
    max_attempts=3,
    backoff=BackoffStrategy.EXPONENTIAL,
    base_delay=1.0,
    max_delay=30.0,
    jitter=True,
    retryable_errors=(Exception,),  # Retry on any exception
)

# Download Retry Policy (more retries for downloads)
DOWNLOAD_RETRY_POLICY = RetryPolicy(
    max_attempts=5,
    backoff=BackoffStrategy.EXPONENTIAL,
    base_delay=2.0,
    max_delay=60.0,
    jitter=True,
    retryable_errors=(Exception,),
)

# GitHub API Circuit Breaker
github_circuit_breaker = SyncCircuitBreaker(
    failure_threshold=5,  # Open after 5 failures
    recovery_timeout=60.0,  # Stay open for 60 seconds
    expected_exception=Exception,
)

# Download Circuit Breaker
download_circuit_breaker = SyncCircuitBreaker(
    failure_threshold=3,  # Open after 3 failures
    recovery_timeout=30.0,  # Stay open for 30 seconds
    expected_exception=Exception,
)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x_get_retry_policy__mutmut_orig(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_1(operation_type: str = "XXdefaultXX") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_2(operation_type: str = "DEFAULT") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_3(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = None
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_4(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "XXgithubXX": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_5(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "GITHUB": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_6(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "XXdownloadXX": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_7(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "DOWNLOAD": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_8(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "XXdefaultXX": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_9(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "DEFAULT": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_10(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(None, GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_11(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, None)


def x_get_retry_policy__mutmut_12(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(GITHUB_RETRY_POLICY)


def x_get_retry_policy__mutmut_13(operation_type: str = "default") -> RetryPolicy:
    """Get retry policy for operation type."""
    policies = {
        "github": GITHUB_RETRY_POLICY,
        "download": DOWNLOAD_RETRY_POLICY,
        "default": GITHUB_RETRY_POLICY,
    }
    return policies.get(operation_type, )

x_get_retry_policy__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_retry_policy__mutmut_1': x_get_retry_policy__mutmut_1, 
    'x_get_retry_policy__mutmut_2': x_get_retry_policy__mutmut_2, 
    'x_get_retry_policy__mutmut_3': x_get_retry_policy__mutmut_3, 
    'x_get_retry_policy__mutmut_4': x_get_retry_policy__mutmut_4, 
    'x_get_retry_policy__mutmut_5': x_get_retry_policy__mutmut_5, 
    'x_get_retry_policy__mutmut_6': x_get_retry_policy__mutmut_6, 
    'x_get_retry_policy__mutmut_7': x_get_retry_policy__mutmut_7, 
    'x_get_retry_policy__mutmut_8': x_get_retry_policy__mutmut_8, 
    'x_get_retry_policy__mutmut_9': x_get_retry_policy__mutmut_9, 
    'x_get_retry_policy__mutmut_10': x_get_retry_policy__mutmut_10, 
    'x_get_retry_policy__mutmut_11': x_get_retry_policy__mutmut_11, 
    'x_get_retry_policy__mutmut_12': x_get_retry_policy__mutmut_12, 
    'x_get_retry_policy__mutmut_13': x_get_retry_policy__mutmut_13
}

def get_retry_policy(*args, **kwargs):
    result = _mutmut_trampoline(x_get_retry_policy__mutmut_orig, x_get_retry_policy__mutmut_mutants, args, kwargs)
    return result 

get_retry_policy.__signature__ = _mutmut_signature(x_get_retry_policy__mutmut_orig)
x_get_retry_policy__mutmut_orig.__name__ = 'x_get_retry_policy'


def x_get_circuit_breaker__mutmut_orig(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_1(operation_type: str = "XXdefaultXX") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_2(operation_type: str = "DEFAULT") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_3(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = None
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_4(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "XXgithubXX": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_5(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "GITHUB": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_6(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "XXdownloadXX": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_7(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "DOWNLOAD": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_8(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "XXdefaultXX": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_9(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "DEFAULT": github_circuit_breaker,
    }
    return breakers.get(operation_type, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_10(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(None, github_circuit_breaker)


def x_get_circuit_breaker__mutmut_11(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, None)


def x_get_circuit_breaker__mutmut_12(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(github_circuit_breaker)


def x_get_circuit_breaker__mutmut_13(operation_type: str = "default") -> SyncCircuitBreaker:
    """Get circuit breaker for operation type."""
    breakers = {
        "github": github_circuit_breaker,
        "download": download_circuit_breaker,
        "default": github_circuit_breaker,
    }
    return breakers.get(operation_type, )

x_get_circuit_breaker__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_circuit_breaker__mutmut_1': x_get_circuit_breaker__mutmut_1, 
    'x_get_circuit_breaker__mutmut_2': x_get_circuit_breaker__mutmut_2, 
    'x_get_circuit_breaker__mutmut_3': x_get_circuit_breaker__mutmut_3, 
    'x_get_circuit_breaker__mutmut_4': x_get_circuit_breaker__mutmut_4, 
    'x_get_circuit_breaker__mutmut_5': x_get_circuit_breaker__mutmut_5, 
    'x_get_circuit_breaker__mutmut_6': x_get_circuit_breaker__mutmut_6, 
    'x_get_circuit_breaker__mutmut_7': x_get_circuit_breaker__mutmut_7, 
    'x_get_circuit_breaker__mutmut_8': x_get_circuit_breaker__mutmut_8, 
    'x_get_circuit_breaker__mutmut_9': x_get_circuit_breaker__mutmut_9, 
    'x_get_circuit_breaker__mutmut_10': x_get_circuit_breaker__mutmut_10, 
    'x_get_circuit_breaker__mutmut_11': x_get_circuit_breaker__mutmut_11, 
    'x_get_circuit_breaker__mutmut_12': x_get_circuit_breaker__mutmut_12, 
    'x_get_circuit_breaker__mutmut_13': x_get_circuit_breaker__mutmut_13
}

def get_circuit_breaker(*args, **kwargs):
    result = _mutmut_trampoline(x_get_circuit_breaker__mutmut_orig, x_get_circuit_breaker__mutmut_mutants, args, kwargs)
    return result 

get_circuit_breaker.__signature__ = _mutmut_signature(x_get_circuit_breaker__mutmut_orig)
x_get_circuit_breaker__mutmut_orig.__name__ = 'x_get_circuit_breaker'


# 🧰🌍🔚
