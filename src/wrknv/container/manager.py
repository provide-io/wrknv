# wrknv/container/manager.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Container Manager Implementation
================================
Thin orchestration facade for container operations.



    ContainerBuilder,
    ContainerExec,
    ContainerLifecycle,
    ContainerLogs,
    VolumeManager,
)


"""


@define
class ContainerManager:
    """Orchestrates container operations through specialized components."""
