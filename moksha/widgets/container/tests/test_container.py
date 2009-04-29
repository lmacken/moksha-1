# This file is part of Moksha.
# Copyright (C) 2008-2009  Red Hat, Inc.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tw.api import Widget
from moksha.widgets.container import MokshaContainer

class TestContainer:

    def setUp(self):
        self.w = MokshaContainer('test')

    def test_render_widget(self):
        assert '<div id="test" ' in self.w()

    def test_widget_content(self):
        """ Ensure we can render a container with another widget """
        class MyWidget(Widget):
            template = """
                Hello World!
            """
        assert 'Hello World!' in self.w(content=MyWidget('mywidget'))

    def test_container_classes(self):
        rendered = self.w(**dict(skin3=True, stikynote=True,
                                 draggable=True, resizable=True))
        assert 'class="containerPlus draggable resizable"' in rendered, rendered
