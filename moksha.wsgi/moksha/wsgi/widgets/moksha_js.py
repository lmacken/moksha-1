# This file is part of Moksha.
# Copyright (C) 2008-2010  Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tw2.core as twc
import tw2.jquery

moksha_js = twc.JSLink(
    modname=__name__,
    filename='static/moksha.js',
    resources=[tw2.jquery.jquery_js])

moksha_extension_points_js = twc.JSLink(
    modname="moksha",
    filename='public/javascript/moksha.extensions.js',
    resources=[moksha_js])
