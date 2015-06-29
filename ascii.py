from PIL import Image
from PIL import ImageDraw
#from PIL import ImageFont

class Ascii():
    def __init__(self, in_file):
        self.from_pic = Image.open(in_file)

    def artify(self, words="#", step=3):
        self.to_pic = Image.new("RGB", self.from_pic.size, "black")
        words = words.upper()

        draw = ImageDraw.Draw(self.to_pic)

        MAX_W, MAX_H = self.from_pic.size
        h = w = i = 0

        # skip pixels by `step` amount and place characters around image
        while h < MAX_H:
            while w < MAX_W:
                # use a string as the art characters
                c = words[i]

                # loop around
                i = (i+1) % len(words)
                p = self.from_pic.getpixel((w, h))
                draw.text((w, h), c, p)
                w += step
            h += step
            w = 0

        self.from_pic.close()

    def save(self, out_file="out.jpg"):
        self.to_pic.save(out_file)
        self.to_pic.close()

