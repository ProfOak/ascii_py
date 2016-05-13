import colorama
import os
from PIL import Image
from PIL import ImageDraw

class Ascii():
    def __init__(self, in_file):
        """ Python ascii image maker """

        self.letter_densities = '" .`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'

        self.from_pic = Image.open(in_file)
        self.to_pic = Image.new("RGB", self.from_pic.size, "black")
        self.draw = ImageDraw.Draw(self.to_pic)
        self.draw = ImageDraw.Draw(self.to_pic)

        self.MAX_W, self.MAX_H = self.from_pic.size

    def word_artify(self, words="#", step=3):
        """ create ascii image from word string """

        words = words.upper()

        h = w = i = 0

        # skip pixels by `step` amount and place characters around image
        while h < self.MAX_H:
            while w < self.MAX_W:
                # use a string as the art characters
                c = words[i]

                # loop around
                i = (i+1) % len(words)

                # get the color from the pixel
                p = self.from_pic.getpixel((w, h))

                # insert text based on pixel color
                self.draw.text((w, h), c, p)

                w += step
            h += step
            w = 0

        self.from_pic.close()

    def density_artify(self, step=7):
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

        while h < self.MAX_H:
            while w < self.MAX_W:
                # get brightness value
                brightness = 255 - grayscale_img.getpixel((w, h))
                clr = self.from_pic.getpixel((w, h))

                # select required character from the letter_densities list
                char_pos = (brightness/255.0) * (len(self.letter_densities) - 1)
                c = self.letter_densities[int(round(char_pos, 0))]
                self.draw.text((w, h), c, clr)

                w += step
            h += step
            w = 0

        self.from_pic.close()
        grayscale_img.close()


    def terminal_artify(self):
        """ covert image to ascii, display in terminal """

        # all colors are beautiful
        acab = [
            [(  0,   0,   0), colorama.Fore.LIGHTBLACK_EX],
            [(  0,   0, 255), colorama.Fore.BLUE],
            [(  0, 255,   0), colorama.Fore.GREEN],
            [(255,   0,   0), colorama.Fore.RED],
            [(255, 255, 255), colorama.Fore.WHITE],
            [(255,   0, 255), colorama.Fore.MAGENTA],
            [(  0, 255, 255), colorama.Fore.CYAN],
            [(255, 255,   0), colorama.Fore.YELLOW]
        ]

        acab = map(lambda x: [map(lambda v: v/255., x[0]), x[1]], acab)
        acab = map(lambda x: [map(lambda v: v**2.2, x[0]), x[1]], acab)

        # needed for Windows operating systems
        colorama.init()

        canvas = self.from_pic
        current_h, current_w = float(self.MAX_H), float(self.MAX_W)

        # resize to fit current dimensions of terminal
        t_height, t_width = self.get_terminal_size()

        if current_h > t_height or current_w > t_width:
            # floating point division
            scalar     = max(current_h/t_height, (current_w*2)/t_width)
            current_w  = int((current_w*2)/scalar)
            current_h  = int((current_h)/scalar)
            dimensions = current_w, current_h
            canvas     = self.from_pic.resize(dimensions)

        # used for brightness (density) levels
        grayscale_img = canvas.convert("L")

        image = ""

        for h in range(current_h):
            for w in range(current_w):
                # get brightness value
                brightness = grayscale_img.getpixel((w, h))/255.
                srgb = tuple(map(lambda v: (((v/255.)**2.2)), canvas.getpixel((w, h))))

                # select required character from the letter_densities list
                char_pos = brightness * (len(self.letter_densities) - 1)

                color = self._convert_color(srgb, brightness, acab)
                image += color + self.letter_densities[int(round(char_pos, 0))]
            image += "\n"

        # prints the converted image to terminal
        # (remove the last newline)
        print image[:-1] + colorama.Fore.RESET

        raw_input("Press enter to continue...")


    #######################################
    #           Helper Methods            #
    #######################################

    def _L2_min(self, v1, v2):
        """
            euclidian norm in a 2 dimensional space
            used for calculating shortest distance
        """

        return (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2

    def get_terminal_size(self):
        """ get the size to display an ascii image to the term """

        return map(int, os.popen('stty size', 'r').read().split())

    def _convert_color(self, rgb, brightness, acab):
        """ convert color using acab data """

        min_distance = 2
        index = 0

        for i in range(0, len(acab)):
            tmp = map(lambda v: v*brightness, acab[i][0])
            distance = self._L2_min(tmp, rgb)

            if distance < min_distance:
                index = i
                min_distance = distance

        return acab[index][1]

    def save(self, out_file="out.jpg"):
        """ save image to file """

        self.to_pic.save(out_file)
        self.to_pic.close()
