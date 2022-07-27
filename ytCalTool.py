from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QLabel
import sys 

class ytCalTool(QWidget):
    def __init__(self, parent=None):
        super(ytCalTool, self).__init__(parent)
        self.setWindowTitle("ytCalTool")

        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QFormLayout()
        self.pUYLineEdit = QLineEdit("0")
        self.pDYLineEdit = QLineEdit("0")
        self.pJHLineEdit = QLineEdit("0")
        self.pSTLineEdit = QLineEdit("0.625")
        self.pLGLineEdit = QLineEdit()
        self.pTPLineEdit = QLineEdit()

        self.pUYLineEdit.setFont(font)
        self.pDYLineEdit.setFont(font)
        self.pJHLineEdit.setFont(font)
        self.pSTLineEdit.setFont(font)
        self.pLGLineEdit.setFont(font)
        self.pTPLineEdit.setFont(font)

        self.pUYLineEdit.returnPressed.connect(self._calculate)
        self.pDYLineEdit.returnPressed.connect(self._calculate)
        self.pJHLineEdit.returnPressed.connect(self._calculate)
        self.pSTLineEdit.returnPressed.connect(self._calculate)

        self.pUYLabel = QLabel("上缘")
        self.pDYLabel = QLabel("下缘")
        self.pJHLabel = QLabel("结合部")
        self.pSTLabel = QLabel("层厚(mm)")
        self.pLGLabel = QLabel("食管长度(cm)")
        self.pTPLabel = QLabel("分型(Ⅰ/Ⅱ/Ⅲ)")

        self.pUYLabel.setFont(font)
        self.pDYLabel.setFont(font)
        self.pJHLabel.setFont(font)
        self.pSTLabel.setFont(font)
        self.pLGLabel.setFont(font)
        self.pTPLabel.setFont(font)

        layout.addRow(self.pUYLabel, self.pUYLineEdit)
        layout.addRow(self.pDYLabel, self.pDYLineEdit)
        layout.addRow(self.pJHLabel, self.pJHLineEdit)
        layout.addRow(self.pSTLabel, self.pSTLineEdit)
        layout.addRow(self.pLGLabel, self.pLGLineEdit)
        layout.addRow(self.pTPLabel, self.pTPLineEdit)

        self.setLayout(layout)

    def _calculate(self):
        try:
            UY = float(self.pUYLineEdit.text())
            DY = float(self.pDYLineEdit.text())
            JH = float(self.pJHLineEdit.text())
            ST = float(self.pSTLineEdit.text())

            Length = (JH-UY)*ST/10.0
            if (UY+DY)/2.0-(JH+20.0/ST) > 0:
                Type = "Ⅲ型"
            elif (UY+DY)/2.0-(JH-10.0/ST) > 0:
                Type = "Ⅱ型"
            else:
                Type = "Ⅰ型"

            self.pLGLineEdit.setText(f"{Length:.3f}")
            self.pTPLineEdit.setText(Type)
        except:
            self._showMessage()

    def _showMessage(self):
        QtWidgets.QMessageBox.critical(self, "错误", "存在非法计算，请重新输入！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ytCalTool()
    win.show()
    sys.exit(app.exec_()) 