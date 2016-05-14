import os
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ascii import Ascii

class Ascii_gui(QWidget):
    def __init__(self):
        super(Ascii_gui, self).__init__()

        self.setWindowTitle("ascii py")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowIcon(QIcon(QPixmap("Media/before.jpg")))

        self.create_widgets()
        self.connect_hooks()
        self.place_widgets()

        self.show()

        # don't really see the point in resizing
        self.setFixedSize(self.size())

    def get_input_file(self):
        self.in_line.setText(QFileDialog.getOpenFileName()[0])

    def get_output_file(self):
        return QFileDialog.getSaveFileName(prefferedName="out.jpg")[0]

    def flip_read_only(self):

        # mess
        read_only = self.words_line.isReadOnly()
        self.words_line.setReadOnly(not read_only)
        read_only = self.words_line.isReadOnly()

        if read_only:
            self.words_line.clear()
            self.words_line.setEnabled(False)
        else:
            self.words_line.setEnabled(True)


    def create_widgets(self):

        self.combo = QComboBox()
        self.combo.addItem("Words")
        self.combo.addItem("Density")

        self.in_label    = QLabel("From image")
        self.words_label = QLabel("Words to use")
        self.step_label  = QLabel("Distance between characters")
        self.combo_label = QLabel("Ascii type")

        self.in_line    = QLineEdit()
        self.words_line = QLineEdit()
        self.step_line  = QLineEdit("6")

        self.open_button     = QPushButton("Open File")
        self.save_img_button = QPushButton("Save Image As")

    def connect_hooks(self):
        self.open_button.clicked.connect(self.get_input_file)
        self.save_img_button.clicked.connect(self.save_img)
        self.combo.currentIndexChanged[str].connect(self.flip_read_only)

    def place_widgets(self):

        self.layout.addWidget(self.in_label, 1, 0, 1, 2)
        self.layout.addWidget(self.in_line, 2, 1, 1, 3)
        self.layout.addWidget(self.open_button, 2, 0, 1, 1)

        self.layout.addWidget(self.combo_label, 4, 0, 1, 1)
        self.layout.addWidget(self.combo, 5, 0, 1, 1)

        self.layout.addWidget(self.words_label, 4, 1, 1, 1)
        self.layout.addWidget(self.words_line, 5, 1, 1, 3)

        self.layout.addWidget(self.step_label, 7, 0, 1, 0)
        self.layout.addWidget(self.step_line, 8, 0, 1, 0)
        self.layout.addWidget(self.save_img_button, 9, 0, 1, 0)

    def save_img(self):
        in_file  = self.in_line.text()
        step     = self.step_line.text()
        words    = self.words_line.text()

        if step.isdigit():
            step = int(step)
        else:
            step = 3

        if words == "":
            words = "#"

        if not os.path.exists(in_file):
            QMessageBox().warning(None, "Error", "Input file does not exist",
                    QMessageBox.StandardButton.Ok)
            return
        output_file = self.get_output_file()

        if not (output_file.lower().endswith(".jpg") or
                output_file.lower().endswith(".png") or
                output_file.lower().endswith(".jpeg")):
            output_file += ".jpg"

        a = Ascii(in_file)
        a.word_artify(words, step)
        a.save(output_file)


def main():
    app = QApplication(sys.argv)
    a = Ascii_gui()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
