# -*- coding: utf-8 -*-

# Copyright (c) 2016 Ericsson AB
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

import pystache
import types


class Pystache(object):

    _pystache = {
        name: getattr(pystache, name)
        for name in dir(pystache) if not name.startswith('_') and isinstance(getattr(pystache, name), types.FunctionType)
    }

    def __getattr__(self, attr):
        if attr in self._pystache:
            return self._pystache[attr]
        raise AttributeError(attr)

    def show_module(self):
        import inspect
        print inspect.getsource(pystache)


def register(node=None, actor=None):
    return Pystache()
