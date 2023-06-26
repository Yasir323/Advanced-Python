class HTMLElement:
    def __init__(self, tag):
        self.tag = tag
        self.attributes = {}
        self.children = []

    def set_attribute(self, name, value):
        self.attributes[name] = value
        return self

    def add_child(self, child):
        self.children.append(child)
        return self

    def __str__(self):
        attrs = ' '.join(f'{name}="{value}"' for name, value in self.attributes.items())
        children = ''.join(str(child) for child in self.children)
        return f'<{self.tag} {attrs}>{children}</{self.tag}>'


# Usage
html = (
    HTMLElement('div')
    .set_attribute('class', 'container')
    .add_child(HTMLElement('h1').set_attribute('id', 'title').add_child('Hello, World!'))
    .add_child(HTMLElement('p').add_child('This is a paragraph.'))
)
print(html)
