import os
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ascii import Ascii

def get_input_file():
    in_line.setText(QFileDialog.getOpenFileName()[0])

def get_output_file():
    out_line.setText(QFileDialog.getSaveFileName()[0])

def save_img():
    in_file  = in_line.text()
    out_file = out_line.text()
    step     = step_line.text()
    words    = words_line.text()

    if step.isdigit():
        step = int(step)
    else:
        step = 3

    if not os.path.exists(in_file):
        QMessageBox().warning(None, "Error", "Input file does not exist",
                QMessageBox.StandardButton.Ok)
        return

    if not (out_file.lower().endswith(".jpg") or
            out_file.lower().endswith(".png") or
            out_file.lower().endswith(".jpeg")):
        out_file += ".jpg"

    a = Ascii(in_file)
    a.artify(words, step)
    a.save(out_file)

app = QApplication(sys.argv)
root = QWidget()
root.setWindowTitle("Ascii Py")
root_layout = QGridLayout()

# === CREATE ===
in_label    = QLabel("From")
out_label   = QLabel("To")
words_label = QLabel("Words to use")
step_label  = QLabel("Step Amount")

in_line    = QLineEdit()
out_line   = QLineEdit("out.jpg")
words_line = QLineEdit("#")
step_line  = QLineEdit("3")

open_button     = QPushButton("Open File")
save_button     = QPushButton("Save As")
save_img_button = QPushButton("Save Image")
# === CREATE ===

# === HOOK ===
open_button.clicked.connect(get_input_file)
save_button.clicked.connect(get_output_file)
save_img_button.clicked.connect(save_img)
# === HOOK ===

# === PLACE ===
root_layout.addWidget(in_label, 1,0,1,1)
root_layout.addWidget(in_line, 2,0,1,1)
root_layout.addWidget(open_button, 3,0,1,1)

root_layout.addWidget(out_label, 1,1,1,1)
root_layout.addWidget(out_line, 2,1,1,1)
root_layout.addWidget(save_button, 3,1,1,1)

root_layout.addWidget(words_label, 4,0,1,1)
root_layout.addWidget(words_line, 5,0,1,1)

root_layout.addWidget(step_label, 4,1,1,1)
root_layout.addWidget(step_line, 5,1,1,1)
root_layout.addWidget(save_img_button, 6,0,1,2)
# === PLACE ===

root.setLayout(root_layout)
root.show()

# don't relaly see the point in resizing
root.setFixedSize(root.size())

app.exec_()
sys.exit()

