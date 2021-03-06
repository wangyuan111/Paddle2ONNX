#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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

from __future__ import absolute_import

from .op_mapper import OpMapper, register_op_mapper
from . import nn
from . import math
from . import activation
from . import tensor
from . import logic

from .detection import yolo_box
from .detection import multiclass_nms
from .detection import prior_box
from .detection import box_coder
from .sequence import im2sequence
