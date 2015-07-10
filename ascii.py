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

    def density_artify(self, step=7):
        """
        Generates the acsii image where the 'words' are selected based on 
        the brightness of a pixel. 

        A brighter pixel will have a character with lower visual density and
        a less bright pixel will have a character with high visual density.
        """
        letter_densities = '" .`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'
        
        if step < 7:
            step = 7
        
        grayscale_img = self.from_pic.convert('L')

        self.to_pic = Image.new("RGB", self.from_pic.size, "black")
        draw = ImageDraw.Draw(self.to_pic)

        MAX_W, MAX_H = self.from_pic.size
        h = 0
        w = 0

        while h < MAX_H:
            while w < MAX_W:
                # get brightness value
                brightness = 255 - grayscale_img.getpixel((w, h))
                clr = self.from_pic.getpixel((w, h))

                # select required character from the letter_densities list
                char_pos = (brightness/255.0) * (len(letter_densities) - 1)

                c = letter_densities[int(round(char_pos, 0))] 

                draw.text((w, h), c, clr)
                w += step
            h += step
            w = 0
        self.from_pic.close()
        grayscale_img.close()

    def save(self, out_file="out.jpg"):
        self.to_pic.save(out_file)
        self.to_pic.close()

