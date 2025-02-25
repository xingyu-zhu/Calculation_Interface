import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox, QLabel,  QMessageBox
from function import Function

class FunctionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = None
        self.b = None
        self.k_a1 = None
        self.k_a2 = None
        self.k_a3 = None
        self.k_a4 = None
        self.K = None
        self.y = None
        self.x = None

        self.setWindowTitle("Function Calculate")
        self.setGeometry(100, 100, 1000, 800)

        center_widget = QWidget()
        self.setCentralWidget(center_widget)

        layout = QGridLayout()
        center_widget.setLayout(layout)

        self.a_label = QLabel("Select Number of ionizable hydrogen ions: ")
        # self.a_label.setGeometry(100, 25, 300, 50)
        layout.addWidget(self.a_label, 0, 0)
        self.a_combobox = QComboBox(self)
        self.a_combobox.addItems(['0', '1', '2', '3', '4'])
        self.a = int(self.a_combobox.currentText())
        self.a_combobox.currentIndexChanged.connect(self.a_value)
        # self.a_combobox.setGeometry(400, 25, 300, 50)
        layout.addWidget(self.a_combobox, 0, 1)

        self.a_label = QLabel("Select coordination coefficient: ")
        layout.addWidget(self.a_label, 1, 0)
        self.b_combobox = QComboBox(self)
        self.b_combobox.addItems(['0.5', '1', '2'])
        self.b = float(self.b_combobox.currentText())
        # self.b_combobox.currentIndexChanged.connect(self.b_value)
        layout.addWidget(self.b_combobox, 1, 1)

        self.a_label = QLabel("Input ionization constant k a1")
        layout.addWidget(self.a_label, 2, 0)
        self.k_a1_edit = QLineEdit(self)
        self.k_a1_edit.setPlaceholderText("Please input ionization constant k a1")
        layout.addWidget(self.k_a1_edit, 2, 1)

        self.a_label = QLabel("Input ionization constant k a2")
        layout.addWidget(self.a_label, 3, 0)
        self.k_a2_edit = QLineEdit(self)
        self.k_a2_edit.setPlaceholderText("Please input ionization constant k a2")
        layout.addWidget(self.k_a2_edit, 3, 1)

        self.a_label = QLabel("Input ionization constant k a2")
        layout.addWidget(self.a_label, 4, 0)
        self.k_a3_edit = QLineEdit(self)
        self.k_a3_edit.setPlaceholderText("Please input ionization constant k a3")
        layout.addWidget(self.k_a3_edit, 4, 1)

        self.a_label = QLabel("Input ionization constant k a2")
        layout.addWidget(self.a_label, 5, 0)
        self.k_a4_edit = QLineEdit(self)
        self.k_a4_edit.setPlaceholderText("Please input ionization constant k a4")
        layout.addWidget(self.k_a4_edit, 5, 1)

        self.k_a1_edit.setEnabled(False)
        self.k_a2_edit.setEnabled(False)
        self.k_a3_edit.setEnabled(False)
        self.k_a4_edit.setEnabled(False)

        self.a_label = QLabel("Input conditional stability constant K")
        layout.addWidget(self.a_label, 6, 0)
        self.K_edit = QLineEdit(self)
        self.K_edit.setPlaceholderText("Please input conditional stability constant K")
        layout.addWidget(self.K_edit, 6, 1)

        self.a_label = QLabel("Input ligand concentration y")
        layout.addWidget(self.a_label, 7, 0)
        self.y_edit = QLineEdit(self)
        self.y_edit.setPlaceholderText("Please input ligand concentration y, y range is (0, 0.2)")
        layout.addWidget(self.y_edit, 7, 1)

        self.a_label = QLabel("Please input system pH value x")
        layout.addWidget(self.a_label, 8, 0)
        self.x_edit = QLineEdit(self)
        self.x_edit.setPlaceholderText("Please input system pH value x, x range is (10, 13)")
        layout.addWidget(self.x_edit, 8, 1)

        self.a_label = QLabel("Function calculation result: ")
        layout.addWidget(self.a_label, 9, 0)
        self.result_display = QLineEdit(self)
        layout.addWidget(self.result_display, 9, 1)
        self.result_display.setEnabled(False)

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        layout.addWidget(calculate_button, 10, 0, 1, 2)

    def a_value(self, index):
        self.k_a1_edit.setEnabled(True)
        self.k_a2_edit.setEnabled(True)
        self.k_a3_edit.setEnabled(True)
        self.k_a4_edit.setEnabled(True)
        self.a = int(index)
        if self.a == 0:
            self.k_a1_edit.setEnabled(False)
            self.k_a2_edit.setEnabled(False)
            self.k_a3_edit.setEnabled(False)
            self.k_a4_edit.setEnabled(False)
        elif self.a == 1:
            self.k_a2_edit.setEnabled(False)
            self.k_a3_edit.setEnabled(False)
            self.k_a4_edit.setEnabled(False)
        elif self.a == 2:
            self.k_a3_edit.setEnabled(False)
            self.k_a4_edit.setEnabled(False)
        elif self.a == 3:
            self.k_a4_edit.setEnabled(False)

    def b_value(self, index):
        self.b = float(index)

    def y_out_range(self, y):
        if float(y) < 0 or float(y) >= 0.2:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Input y value is out of range. y value range is (0, 0.2)")
            msg_box.setWindowTitle("Warning")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg_box.exec()
            return False
        else:
            return True

    def x_out_range(self, x):
        if float(x) < 10 or float(x) > 13:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Input x value is out of range. x value range is (10, 13)")
            msg_box.setWindowTitle("Warning")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg_box.exec()
            return False
        else:
            return True


    def check_data(self):
        flag = False
        try:
            self.a = int(self.a_combobox.currentText())
            if self.a == 0:
                self.k_a1, self.k_a2, self.k_a3, self.k_a4 = 0, 0, 0, 0
            elif self.a == 1:
                self.k_a1 = float(self.k_a1_edit.text())
                self.k_a2, self.k_a3, self.k_a4 = 0, 0, 0
            elif self.a == 2:
                self.k_a1 = float(self.k_a1_edit.text())
                self.k_a2 = float(self.k_a2_edit.text())
                self.k_a3, self.k_a4 = 0, 0
            elif self.a == 3:
                self.k_a1 = float(self.k_a1_edit.text())
                self.k_a2 = float(self.k_a2_edit.text())
                self.k_a3 = float(self.k_a3_edit.text())
                self.k_a4 = 0
            elif self.a == 4:
                self.k_a1 = float(self.k_a1_edit.text())
                self.k_a2 = float(self.k_a2_edit.text())
                self.k_a3 = float(self.k_a3_edit.text())
                self.k_a4 = float(self.k_a4_edit.text())

            self.b = float(self.b_combobox.currentText())

            self.K = float(self.K_edit.text())
            self.y = float(self.y_edit.text())
            self.x = float(self.x_edit.text())
            flag = True
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Invalid input. Please enter a number.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg_box.exec()

        return flag

    def calculate(self):
        data_check = self.check_data()
        if data_check:
            if self.y_out_range(y=self.y):
                if self.x_out_range(x=self.x):
                    f = Function(self.a, self.b, self.k_a1, self.k_a2, self.k_a3, self.k_a4, self.K, self.y, self.x)
                    self.result_display.setText(str(f.z()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FunctionWindow()
    main.show()
    sys.exit(app.exec())

