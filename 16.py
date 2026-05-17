import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class BMIApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(BMIApp, self).__init__()
        self.setupUi(self)  # настройка дизайна
        self.init_logic()  # настройка логики

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 755)
        MainWindow.setStyleSheet("background-color: #22222e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # шрифт
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(16)

        # общий стиль полей
        input_style = "background-color: #22222e; border: 2px solid #f66867; border-radius: 30px; color: white;"

        # поля ввода
        self.input_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.input_weight.setGeometry(QtCore.QRect(50, 320, 380, 60))
        self.input_weight.setFont(font)
        self.input_weight.setStyleSheet(input_style)
        self.input_weight.setAlignment(QtCore.Qt.AlignCenter)

        self.input_height = QtWidgets.QLineEdit(self.centralwidget)
        self.input_height.setGeometry(QtCore.QRect(50, 400, 380, 60))
        self.input_height.setFont(font)
        self.input_height.setStyleSheet(input_style)
        self.input_height.setAlignment(QtCore.Qt.AlignCenter)

        # поля вывода
        self.output_status = QtWidgets.QLineEdit(self.centralwidget)
        self.output_status.setGeometry(QtCore.QRect(50, 480, 380, 60))
        self.output_status.setFont(font)
        self.output_status.setStyleSheet(input_style)
        self.output_status.setAlignment(QtCore.Qt.AlignCenter)
        self.output_status.setReadOnly(True)

        self.output_bmi = QtWidgets.QLineEdit(self.centralwidget)
        self.output_bmi.setGeometry(QtCore.QRect(50, 560, 380, 60))
        self.output_bmi.setFont(font)
        self.output_bmi.setStyleSheet(input_style)
        self.output_bmi.setAlignment(QtCore.Qt.AlignCenter)
        self.output_bmi.setReadOnly(True)

        # кнопка
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 660, 380, 60))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton { color: white; background-color: #fb5b5d; border-radius: 30px; } QPushButton:pressed { background-color: #fa4244; }")

        #красная панель
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 271))
        self.frame.setStyleSheet("background-color: #fb5b5d")

        # заголовок
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setGeometry(QtCore.QRect(70, 20, 341, 51))
        font_t = QtGui.QFont("Montserrat", 16, QtGui.QFont.Bold)
        self.label_title.setFont(font_t)
        self.label_title.setStyleSheet("color: white;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("калькулятор ИМТ")

        # ИКОНКА (теперь icon.png)
        self.label_icon = QtWidgets.QLabel(self.frame)
        self.label_icon.setGeometry(QtCore.QRect(140, 80, 191, 171))
        self.label_icon.setPixmap(QtGui.QPixmap("icon.png")) # картинка из папки
        self.label_icon.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

    def init_logic(self):
        self.input_weight.setPlaceholderText('ваш вес (кг):')
        self.input_height.setPlaceholderText('ваш рост (см):')
        self.output_status.setPlaceholderText('состояние здоровья')
        self.output_bmi.setPlaceholderText('ваш ИМТ')
        self.pushButton.setText("рассчитать")

        # связка кнопки с функцией
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        try:
            w = float(self.input_weight.text().replace(',', '.'))
            h = float(self.input_height.text().replace(',', '.')) / 100

            bmi = round(w / (h * h), 2)

            # логика
            if bmi < 18.5:
                res = "дефицит веса"
            elif 18.5 <= bmi < 25:
                res = "нормальный вес"
            elif 25 <= bmi < 30:
                res = "лишний вес"
            else:
                res = "ожирение"

            # вывод результата
            self.output_bmi.setText(str(bmi))
            self.output_status.setText(res)

        except:
            self.output_status.setText("ошибка ввода")
            self.output_bmi.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec_())