import os, sys
import colorama
from PIL import Image
from PIL import ImageDraw



def L2_min(v1, v2):
    return (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2

class TerminalCanvas:
    def __init__(self):
        colorama.init()
        self.height, self.width = self.getSize()
        self.canvas = Image.new('RGB',(self.width, self.height), "black")
        self.acab = [
            [(0, 0, 0), colorama.Fore.BLACK],
            [(0, 0, 255), colorama.Fore.BLUE],
            [(0, 255, 0), colorama.Fore.GREEN],
            [(255, 0, 0),colorama.Fore.RED],
            [(255, 255, 255),colorama.Fore.WHITE],
            [(255, 0, 255),colorama.Fore.MAGENTA],
            [(0, 255, 255),colorama.Fore.CYAN],
            [(255, 255, 0),colorama.Fore.YELLOW]
        ]

        self.acab = map(lambda x: [map(lambda v: v/255., x[0]), x[1]], self.acab)
        self.acab = map(lambda x: [map(lambda v: v**2.2, x[0]), x[1]], self.acab)

    def convertColor(self, rgb, brightness):
        min_distance = 2
        index = 0

        for i in range(0, len(self.acab)):
            tmp = map(lambda v: v*brightness, self.acab[i][0])
            distance = L2_min(tmp, rgb)
            if distance < min_distance:
                index = i
                min_distance = distance

        return self.acab[index][1]

    def getSize(self):
        return map(int, os.popen('stty size', 'r').read().split())

    def render(self):
        letter_densities = '" .`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'
        
        grayscale_img = self.canvas.convert('L')
        MAX_W, MAX_H = self.canvas.size
        h = 0
        w = 0

        image = ""
        for h in range(0, MAX_H):
            for w in range(0, MAX_W):
                # get brightness value
                brightness = grayscale_img.getpixel((w, h))/255.
                srgb = tuple(map(lambda v: (((v/255.)**2.2)), self.canvas.getpixel((w, h))))

                # select required character from the letter_densities list
                char_pos = brightness * (len(letter_densities) - 1)
                
                color = self.convertColor(srgb, brightness)
                image += color + letter_densities[int(round(char_pos, 0))] 

        print image + colorama.Fore.RESET
		
    def project(self, image, x, y, width, height):
        if x+width < 0 or x > self.width:
            return

        if y+height < 0 or y > self.height:
            return

        self.canvas.paste(image.resize((width, height)), (x, y))
        self.canvas.save("wup.jpg")

if __name__ == "__main__":
    c = TerminalCanvas()
    image = Image.open(sys.argv[1])
    c.project(image, 0, 0, c.width, c.height)
    c.render()
