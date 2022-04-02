import random
import sys
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Sentence Word Shuffler')
window.setGeometry(0, 0, 500, 500)
window.setMaximumSize(500, 500)

input_msg = QLabel('Input your sentence', parent = window)
input_msg.move(28, 30)

output_msg = QLabel('', parent = window)
output_msg.setFixedSize(450, 300)
output_msg.setWordWrap(True)
output_msg.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
output_msg.move(28, 200)

def enter_sentence(sen):
    sen = sen.split()
    random.shuffle(sen)
    final_sen = '(' + ' / '.join(sen) + ')'
    print(final_sen)
    output_msg.setText(final_sen)

def copy_to_clipboard(sen):
    pyperclip.copy(sen)

shuffle_btn = QPushButton('Shuffle', parent = window)
shuffle_btn.clicked.connect(lambda: enter_sentence(input_box.toPlainText()))
shuffle_btn.move(215, 210)

copy_btn = QPushButton('COPY', parent = window)
copy_btn.clicked.connect(lambda: copy_to_clipboard(output_msg.text()))
copy_btn.move(215, 450)

input_box = QTextEdit('', parent=window)
input_box.setFixedSize(450, 150)
input_box.move(25, 50)
# input_box.returnPressed.connect(lambda: enter_sentence(input_box.text()))

window.show()

sys.exit(app.exec_())