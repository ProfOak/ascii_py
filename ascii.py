from PIL import Image
from PIL import ImageDraw
#from PIL import ImageFont

class Ascii():
    def __init__(self, in_file):
        self.from_pic = Image.open(in_file)

    def artify(self, words="#"):
        self.to_pic = Image.new("RGB", self.from_pic.size, "black")
        words = words.upper()

        draw = ImageDraw.Draw(self.to_pic)

        MAX_W, MAX_H = self.from_pic.size
        STEP = 3
        h = w = i = 0

        # skip pixels by STEP amout and place characters around image
        while h < MAX_H:
            while w < MAX_W:
                # use a string as characters as the art characters
                c = words[i]

                # loop around
                i = (i+1) % len(words)

                draw.text((w, h), c, self.from_pic.getpixel((w, h)))
                w += STEP
            h += STEP
            w = 0

        self.from_pic.close()

    def save(self, out_file="out.jpg"):
        self.to_pic.save(out_file)
        self.to_pic.close()

