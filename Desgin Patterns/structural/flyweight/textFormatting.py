"""In applications that involve text processing or formatting, the Flyweight pattern can be used to optimize the
memory usage of commonly used formatting styles. Instead of creating a new object for each text element,
you can share the formatting objects among multiple text elements with the same style. This reduces the memory
footprint and improves performance. """


class TextFormatting:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def apply_formatting(self, text):
        return f"<span style='font-family:{self.font}; font-size:{self.size}; color:{self.color}'>{text}</span>"


class TextElement:
    def __init__(self, text, formatting):
        self.text = text
        self.formatting = formatting

    def render(self):
        formatted_text = self.formatting.apply_formatting(self.text)
        print(formatted_text)


# Usage
formatting = TextFormatting("Arial", "12px", "#000000")
text_element1 = TextElement("Hello", formatting)
text_element2 = TextElement("World", formatting)

text_element1.render()  # Renders: <span style='font-family:Arial; font-size:12px; color:#000000'>Hello</span>
text_element2.render()  # Renders: <span style='font-family:Arial; font-size:12px; color:#000000'>World</span>
