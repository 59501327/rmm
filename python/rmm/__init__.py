# Copyright (c) 2018-2021, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import weakref

from rmm import mr
from rmm._lib.device_buffer import DeviceBuffer
from rmm._version import get_versions
from rmm.mr import disable_logging, enable_logging, get_log_filenames
from rmm.rmm import (
    RMMError,
    RMMNumbaManager,
    _numba_memory_manager,
    is_initialized,
    register_reinitialize_hook,
    reinitialize,
    rmm_cupy_allocator,
    unregister_reinitialize_hook,
)

__all__ = [
    "DeviceBuffer",
    "RMMError",
    "RMMNumbaManager",
    "disable_logging",
    "enable_logging",
    "get_log_filenames",
    "get_versions",
    "is_initialized",
    "mr",
    "register_reinitialize_hook",
    "reinitialize",
    "rmm_cupy_allocator",
    "unregister_reinitialize_hook",
]

__version__ = get_versions()["version"]
