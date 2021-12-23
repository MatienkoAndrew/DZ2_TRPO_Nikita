from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 632)
        Dialog.setStyleSheet("background-color: rgb(10, 10, 125);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setStyleSheet("background-color: rgb(200, 251, 251);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.metro_label = QtWidgets.QLabel(self.frame)
        self.metro_label.setGeometry(QtCore.QRect(0, 165, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.metro_label.setFont(font)
        self.metro_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.metro_label.setObjectName("metro_label")

        self.metroEdit = QtWidgets.QLineEdit(self.frame)
        self.metroEdit.setGeometry(QtCore.QRect(260, 165, 250, 30))
        self.metroEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.metroEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.metroEdit.setObjectName("metroEdit")

        self.kitchen_label = QtWidgets.QLabel(self.frame)
        self.kitchen_label.setGeometry(QtCore.QRect(0, 250, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.kitchen_label.setFont(font)
        self.kitchen_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.kitchen_label.setObjectName("kitchen_label")

        self.kitchetEdit = QtWidgets.QLineEdit(self.frame)
        self.kitchetEdit.setGeometry(QtCore.QRect(260, 250, 250, 30))
        self.kitchetEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.kitchetEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.kitchetEdit.setObjectName("kitchetEdit")

        self.mean_bill_label = QtWidgets.QLabel(self.frame)
        self.mean_bill_label.setGeometry(QtCore.QRect(0, 335, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mean_bill_label.setFont(font)
        self.mean_bill_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.mean_bill_label.setObjectName("mean_bill_label")

        self.mean_billEdit = QtWidgets.QLineEdit(self.frame)
        self.mean_billEdit.setGeometry(QtCore.QRect(260, 335, 250, 30))
        self.mean_billEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.mean_billEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.mean_billEdit.setObjectName("mean_billEdit")

        self.write = QtWidgets.QPushButton(self.frame)
        self.write.setGeometry(QtCore.QRect(350, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.write.setFont(font)
        self.write.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.write.setObjectName("pushButton")

        self.go_one_line = QtWidgets.QPushButton(self.frame)
        self.go_one_line.setGeometry(QtCore.QRect(0, 450, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.go_one_line.setFont(font)
        self.go_one_line.setStyleSheet("background-color: rgb(10, 17, 0);")
        self.go_one_line.setObjectName("pushButton1")

        self.go_last_line = QtWidgets.QPushButton(self.frame)
        self.go_last_line.setGeometry(QtCore.QRect(400, 450, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.go_last_line.setFont(font)
        self.go_last_line.setStyleSheet("background-color: rgb(10, 17, 0);")
        self.go_last_line.setObjectName("pushButton2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.metro_label.setText(_translate("Dialog", "Введите станцию метро"))
        self.write.setText(_translate("Dialog", "Записать"))
        self.go_one_line.setText(_translate("Dialog", "Все записи"))
        self.go_last_line.setText(_translate("Dialog", "Последняя запись"))
        self.kitchen_label.setText(_translate("Dialog", "Введите кухню"))
        self.mean_bill_label.setText(_translate("Dialog", "Введите средний чек"))

