from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import os
from dotenv import load_dotenv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setStyleSheet("background-color: rgb(111, 111, 165);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 90, 191, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 530, 700, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setToolTipDuration(-1)
        self.label_3.setStyleSheet("background-color: rgb(91, 91, 136);")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(450, 300, 191, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(50, 150, 101, 31))
        self.spinBox.setMaximum(9999)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 410, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency converter v.2"))
        self.comboBox.setItemText(0, _translate("MainWindow", "US dollar USD"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Euro EUR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Belarusian ruble BYN"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Kazakhstani tenge KZT"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Canadian dollar CAD"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Polish zloty PLN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Russian ruble RUB"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Ukrainian hryvnia UAH"))
        self.label.setText(_translate("MainWindow", "Currency converter"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "US dollar USD"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Euro EUR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Belarusian ruble BYN"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Kazakhstani tenge KZT"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Canadian dollar CAD"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Polish zloty PLN"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Russian ruble RUB"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Ukrainian hryvnia UAH"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))

    def add_function(self):
        self.pushButton.clicked.connect(lambda: self.get_response(self.spinBox.value(), self.comboBox.currentText()[-3:], self.comboBox_2.currentText()[-3:]))

    def get_response(self, amount, from_currency, to_currency):
        if amount > 0:
            if from_currency == to_currency:
                self.write_result(int(amount))
            else:
                load_dotenv()
                response = requests.get(
                    str(os.getenv("API_URL")) + str(from_currency)).json()
                self.write_result(float(response["conversion_rates"][to_currency]) * amount)
        else:
            self.write_result(0)

    def write_result(self, num: int):
        self.label_3.setText(str(round(num, 3)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())