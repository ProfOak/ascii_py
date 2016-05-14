#Ascii Py

Makin some pictures

This library requires the Pillow and colorama libraries

`python3 -m pip install -U Pillow colorama`

To use the gui you need PySide

`python3 -m pip install -U PySide`

At the time of this commit PySide can only be installed on Python versions 2.6, 2.7, 3.3, 3.4. If you wish to use the GUI you must have installed versions 3.3 or 3.4. You can read more about it here https://github.com/PySide/pyside-setup/issues/53

---

```
Usage: main.py [options]

Options:

  -h, --help            show this help message and exit
  -o FILENAME, --out=FILENAME
                        The filename you want your final image saved as
  -w WORDS, --words=WORDS
                        Use words to create your image
  -s STEP, --step=STEP  Choose the distance of your characters
  -d, --density         Adding the flag converts the image based on visual
                        density
  -t, --terminal        Print ascii image to terminal
```

Example usage
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

`$ python main.py -s 10 -w "dank memes" -o ayy_lmao_pizza.jpg Media/pizza_in.jpg`

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/pizza_in.jpg)

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/ayy_lmao_pizza.jpg)
