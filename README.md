# Ascii Py

Makin some pictures

Install instructions
---

Using pip
---

```
python3 -m pip install ascii_py
```

From source
---

```
git clone https://github.com/profoak/ascii_py
cd ascii_py
python3 setup.py install
```

Usage
---

```
usage: ascii_py [-h] [-o OUT] [-w WORDS] [-s STEP] [-d] [-t] input_file

positional arguments:
  input_file            Input file to convert from.

optional arguments:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The filename you want your final image saved as.
  -w WORDS, --words WORDS
                        Use words to create your image.
  -s STEP, --step STEP  Choose the distance of your characters.
  -d, --density         Adding the flag converts the image based on visual density.
  -t, --terminal        Print ascii image to terminal.
```

Example images
---

Original image:

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/before.jpg)

Default usage:

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/after.jpg)

Density flag:

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/density.jpg)

Terminal flag (screenshot):

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/terminal.jpg)

Other flags usage example:
---

`$ ascii_py -s 10 -w "dank memes" -o ayy_lmao_pizza.jpg Media/pizza_in.jpg`

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/pizza_in.jpg)

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/ayy_lmao_pizza.jpg)
