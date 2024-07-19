# 1. Constructing the class.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 2. Defining set_width.
    def set_width(self, width):
        self.width = width

    # 3. Defining set_height.
    def set_height(self, height):
        self.height = height

    # 4. Defining get_area (returning width + height).
    def get_area(self):
        return self.width * self.height

    # 5. Defining get_perimeter (returning 2 * width + 2 * height).
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # 6. Defining get_diagonal (returning [width ** 2 + height ** 2] ** .5).
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # 7. Defining get_picture ( if width or height > 50, return 'Too big for picture')
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ('*' * self.width + '\n') * self.height

    # 8. Defining get_amount_inside [i.e rectangle(width=4, height=8) can fit inside two squares (length=4)].
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    # 9. Defining __init__ (storing side length in width & height attributes from Rectangle).
    def __init__(self, side):
        super().__init__(side, side)

    # 10. Defining the methods to represent Square sides.
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"