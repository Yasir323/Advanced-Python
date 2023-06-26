"""In game development, especially in 2D games with large numbers of sprites, the Flyweight pattern can be used to
optimize the memory usage of character sprites. Instead of storing individual sprite objects for each character,
you can share common properties (e.g., image, animations) among multiple characters of the same type. This reduces
memory consumption and facilitates efficient rendering. """


class CharacterSprite:
    def __init__(self, image):
        self.image = image

    def render(self):
        print(f"Rendering character with image: {self.image}")


def load_character_image(character_type):
    pass


class CharacterFactory:
    def __init__(self):
        self.sprites = {}

    def get_character_sprite(self, character_type):
        if character_type not in self.sprites:
            image = load_character_image(character_type)
            self.sprites[character_type] = CharacterSprite(image)
        return self.sprites[character_type]


# Usage
factory = CharacterFactory()

character1 = factory.get_character_sprite("Hero")
character1.render()  # Renders: Rendering character with image: hero.png

character2 = factory.get_character_sprite("Enemy")
character2.render()  # Renders: Rendering character with image: enemy.png

character3 = factory.get_character_sprite("Hero")
character3.render()  # Renders: Rendering character with image: hero.png
