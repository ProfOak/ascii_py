from ascii import Ascii
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-o", "--out", dest = "filename", default = "out.jpg",
            help = "The filename you want your final image saved as")
    parser.add_option("-w", "--words", dest = "words", default = "#",
            help = "Use words to create your image")
    parser.add_option("-s", "--step", dest = "step", type = "int", default = 3,
            help = "Choose the distance of your characters")
    parser.add_option("-d", "--density", action="store_true", dest='density',
            help="Adding the flag converts the image based on visual density")
    parser.add_option("-t", "--terminal", action="store_true", dest='terminal',
            help="Print ascii image to terminal")

    (options, args) = parser.parse_args()

    if len(args) > 0:
        in_file = args[0]
    else:
        print "Failed to provide an input image"
        return

    a = Ascii(in_file)

    if options.density:
        a.density_artify(step=options.step)
    elif options.terminal:
        a.terminal_artify()
    else:
        a.word_artify(options.words, options.step)

    a.save(options.filename)

if __name__ == "__main__":
    main()

