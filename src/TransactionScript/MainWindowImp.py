from PyQt5 import QtCore, QtGui, QtWidgets
from src.Interface.MainWindow import Ui_Dialog
from src.TransactionScript.Restaurant import Restaurant
from src.TransactionScript.OutputImp import Output


##-- Главное окно
class MainForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Restaurants")
        self.BD = None

        self.ui.write.clicked.connect(self.get_restaurant)
        self.ui.go_one_line.clicked.connect(self.goToBD)
        self.ui.go_last_line.clicked.connect(self.goToBD2)

    def get_restaurant(self):
        metro = self.ui.metroEdit.text()
        kitchen = self.ui.kitchetEdit.text()
        avg_bill = self.ui.mean_billEdit.text()

        restaurant = Restaurant()
        restaurant.createRestaurant(metro, kitchen, avg_bill)
        QtWidgets.QMessageBox.about(self, "Предупреждение", "Записано в БД")

    # если нажата кнопка "Все записи"
    def goToBD(self):
        self.BD = Output(0)
        self.BD.show()

    def goToBD2(self):
        self.BD = Output(1)
        self.BD.show()

