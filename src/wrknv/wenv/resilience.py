# wrknv/wenv/resilience.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resilience Configuration for wrknv
===================================
Retry policies, circuit breakers, and fallback chains for network operations.
from __future__ import annotations
from provide.foundation.resilience import BackoffStrategy, RetryPolicy, SyncCircuitBreaker
