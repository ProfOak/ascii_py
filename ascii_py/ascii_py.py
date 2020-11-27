import shutil
from collections import namedtuple
from typing import List, Tuple

import colorama  # type: ignore
from PIL import Image, ImageDraw  # type: ignore

RGB = Tuple[float, float, float]
Color = namedtuple("Color", ["rgb", "colorama"])



class Ascii:
    def __init__(self, in_file: str):
        """Set up data for how the image should be formatted at the end."""

        self.letter_densities = '" .`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'

        self.from_pic = Image.open(in_file)
        self.to_pic = Image.new("RGB", self.from_pic.size, "black")
        self.draw = ImageDraw.Draw(self.to_pic)

        self.MAX_W, self.MAX_H = self.from_pic.size

        self.color_list = (
            Color([0, 0, 0], colorama.Fore.LIGHTBLACK_EX),
            Color([0, 0, 255], colorama.Fore.BLUE),
            Color([0, 255, 0], colorama.Fore.GREEN),
            Color([255, 0, 0], colorama.Fore.RED),
            Color([255, 255, 255], colorama.Fore.WHITE),
            Color([255, 0, 255], colorama.Fore.MAGENTA),
            Color([0, 255, 255], colorama.Fore.CYAN),
            Color([255, 255, 0], colorama.Fore.YELLOW),
        )

        # convert everything to floats
        # linearize in case more colors are added
        self.color_list = [
            Color([(v / 255.0) ** 2.2 for v in color.rgb], color.colorama)
            for color in self.color_list
        ]  # type: ignore

    def word_artify(self, words: str = "#", step: int = 3):
        """Create ascii image from word string"""

        words = words.upper()

        h = w = i = 0

        # skip pixels by `step` amount and place characters around image
        while h < self.MAX_H:
            while w < self.MAX_W:
                # use a string as the art characters
                char = words[i]

                # loop around
                i = (i + 1) % len(words)

                # get the color from the pixel
                pixel = self.from_pic.getpixel((w, h))

                # insert text based on pixel color
                self.draw.text((w, h), char, pixel)

                w += step
            h += step
            w = 0

        self.from_pic.close()

    def density_artify(self, step: int = 7):
        """
        Generates the acsii image where the 'words' are selected based on
        the brightness of a pixel.

        A brighter pixel will have a character with lower visual density and
        a less bright pixel will have a character with high visual density.
        """

        if step < 7:
            step = 7

        h = 0
        w = 0

        # used for brightness (density) levels
        grayscale_img = self.from_pic.convert("L")

        while h < self.MAX_H:
            while w < self.MAX_W:
                # get brightness value
                brightness = 255 - grayscale_img.getpixel((w, h))
                color = self.from_pic.getpixel((w, h))

                # select required character from the letter_densities list
                char_pos = (brightness / 255.0) * (len(self.letter_densities) - 1)
                c = self.letter_densities[int(round(char_pos, 0))]
                self.draw.text((w, h), c, color)

                w += step
            h += step
            w = 0

        self.from_pic.close()
        grayscale_img.close()

    def terminal_artify(self):
        """Covert image to ascii, display in terminal"""

        # Workaround for Windows.
        colorama.init()

        canvas = self.from_pic
        current_h, current_w = float(self.MAX_H), float(self.MAX_W)

        # Resize to fit current dimensions of terminal.
        # shutil added get_terminal_size starting in python 3.3
        t_width, t_height = shutil.get_terminal_size()

        if current_h > t_height or current_w > t_width:
            scalar = max(current_h / t_height, (current_w * 2) / t_width)
            current_w = int((current_w * 2) / scalar)
            current_h = int((current_h) / scalar)
            dimensions = (current_w, current_h)
            canvas = self.from_pic.resize(dimensions)

        # used for brightness (density) levels
        grayscale_img = canvas.convert("L")

        image = ""

        for h in range(current_h):
            for w in range(current_w):
                brightness = grayscale_img.getpixel((w, h)) / 255.0
                pixel = _get_pixel(canvas, w, h)
                srgb = [(v / 255.0) ** 2.2 for v in pixel]

                # Select best matching character from the letter_densities list.
                char_pos = brightness * (len(self.letter_densities) - 1)
                color = self._convert_color(srgb, brightness)

                image += color + self.letter_densities[int(round(char_pos, 0))]
            image += "\n"

        # Remove that extra newline at the end.
        print(image[:-1] + colorama.Fore.RESET)

        self.from_pic.close()
        grayscale_img.close()

        input("Press enter to continue...")

    def _L2_min(self, v1: RGB, v2: RGB) -> float:
        """Calculate the distance between two colors using their RGB values.

        Use the Euclidian distance to perform this calculation.
        """

        return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2

    def _convert_color(self, rgb: RGB, brightness: float) -> str:
        """Figure out which is the closest color to the pixel being worked on."""

        min_distance = 2.0
        index = 0

        for i in range(len(self.color_list)):
            tmp = [v * brightness for v in self.color_list[i].rgb]
            distance = self._L2_min(tmp, rgb)  # type: ignore

            if distance < min_distance:
                index = i
                min_distance = distance

        return self.color_list[index].colorama

    def save(self, out_file: str = "out.jpg"):
        """Given a filename, save image to file."""

        self.to_pic.save(out_file)
        self.to_pic.close()


def _get_pixel(canvas: Image.Image, w: int, h: int) -> Tuple[int, int, int]:
    """Get the color of the pixel at the current spot in the canvas.

    getpixel() may return an int, instead of tuple of ints, if the source img
    is a PNG with a transparent layer.
    """
    pixel = canvas.getpixel((w, h))
    if isinstance(pixel, int):
        pixel = (pixel, pixel, 255)
    return pixel
