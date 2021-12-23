from PyQt5 import QtCore, QtGui, QtWidgets
from src.Interface.Output import OutputForm
from src.TransactionScript.Restaurant import Restaurant


##-- Окно
class Output(QtWidgets.QDialog):
    def __init__(self, button_clicked, parent=None):
        super().__init__(parent)
        self.ui = OutputForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Restaurants")

        self.button_clicked = button_clicked
        self.initUI()

    def initUI(self):
        if self.button_clicked == 0:
            self.show_all_lines()
        else:
            self.show_last_line()
        pass

    def show_all_lines(self):
        restaurant = Restaurant()
        rows = restaurant.getAll()

        self.ui.tableWidget.setRowCount(len(rows))
        tablerow = 0
        for row in rows:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))

            tablerow += 1
            pass
        pass

    def show_last_line(self):
        restaurant = Restaurant()
        restaurantInfo = restaurant.getLastRestaurant()

        self.ui.tableWidget.setRowCount(1)
        tablerow = 0
        self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(restaurantInfo[0])))
        self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(restaurantInfo[1])))
        self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(restaurantInfo[2])))
        self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(restaurantInfo[3])))
        pass

