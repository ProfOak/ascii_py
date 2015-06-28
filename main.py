from ascii import Ascii
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-o", "--out", dest = "filename",
        help = "The filename you want your final image saved as")
    parser.add_option("-w", "--words", dest = "words",
        help = "Use words to create your image")
    (options, args) = parser.parse_args()

    out_file = "out.jpg"
    words = "#"

    if options.filename:
        out_file = options.filename
    if options.words:
        words = options.words
    if len(args) > 0:
        in_file = args[0]
    else:
        print "Failed to provide an input image"
        return

    a = Ascii(in_file)
    a.artify(words)
    a.save(out_file)

if __name__ == "__main__":
    main()
