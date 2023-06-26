"""
Suppose you are working on a graphical user interface (GUI) framework where you
need to create multiple instances of UI elements, such as buttons or labels,
with different configurations. You can use the Prototype pattern to clone the
base UI element prototypes and customize them as needed.
"""

import copy


class UIElement:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


# Usage
button_prototype = UIElement('Button')
label_prototype = UIElement('Label')

# Clone UI elements
button1 = button_prototype.clone()
button1.name = 'Button 1'

button2 = button_prototype.clone()
button2.name = 'Button 2'

label = label_prototype.clone()
label.name = 'Label 1'
