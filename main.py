from ascii import Ascii
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-o", "--out", dest = "filename", default = "out.jpg",
            help = "The filename you want your final image saved as")
    parser.add_option("-w", "--words", dest = "words", default = "#",
            help = "Use words to create your image")
    parser.add_option("-s", "--step", dest = "step", type = "int", default = 3,
            help = "choose the distance of your characters")
    parser.add_option("-t", "--type", default='n', dest='typ',
            help="the type of ascii art to generate. n: normal, d:density")

    (options, args) = parser.parse_args()

    if len(args) > 0:
        in_file = args[0]
    else:
        print "Failed to provide an input image"
        return

    a = Ascii(in_file)
    if (options.typ.lower() == 'd'):
        a.density_artify(step=options.step)
    else:
        a.artify(options.words, options.step)
    a.save(options.filename)

if __name__ == "__main__":
    main()

