from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

app = QApplication([])
window = QWidget()
window2 = QWidget()
window3 = QWidget()
window.resize(600, 470)
window.setWindowTitle("Здоров'я")

label = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
label2 = QLabel("Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я.\nПроба Руфє навантажувальним комплексом,призначеним для оцінки працездатності серця при фізичному навантаженні.\nУ випробуваного,що знаходиться в положенні лежачи на спині протягом 5 хв,визначають частоту пульсу за 15 секунд;\nпотім протягом 45 секунд випробуваний виконує 30 присідань.\nПісля закінчення навантаження випробуваний лягає,і в нього знову підраховується кількість пульсацій за перші 15 секунд,\nА потім - за останні 15 секунд першої хвилини періоду відновлення.\nВажливо! Якщо в процесі проведення випробування ви відчуєте себе погано(з'явиться запаморочення,шум\nвухах,сильна задишка та ін.) то тест небхідно перервати і звернутися до лікаря.")

button = QPushButton("Почати")
layout = QGridLayout()
button.setFixedSize(100, 30)
layout.addWidget(label, 0, 0, 1, 3)
layout.addWidget(label2, 1, 0, 1, 3)
layout.addWidget(QLabel(), 2, 0)
layout.addWidget(button, 2, 1)
layout.addWidget(QLabel(), 2, 2)

window.setLayout(layout)


def show_window2():
    window.hide()
    window2.show()


def show_window3():
    window2.hide()
    window3.show()


def start_test(timer_label, duration):
    timer_font = QFont()
    timer_font.setPointSize(24)

    timer_label.setFont(timer_font)
    timer_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

    layout2.addWidget(timer_label)
    window2.setLayout(layout2)
    window2.show()

    def update_timer():
        remaining_time = int(timer_label.text()) - 1
        timer_label.setText(str(remaining_time))
        if remaining_time <= 0:
            timer.stop()
            layout2.removeWidget(timer_label)
            timer_label.deleteLater()

    timer = QtCore.QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)


def start_first_test():
    timer_label = QLabel("15")
    start_test(timer_label, 15)


def start_first_test2():
    timer_label = QLabel("45")
    start_test(timer_label, 45)


def start_first_test3():
    timer_label = QLabel("60")
    start_test(timer_label, 60)


button.clicked.connect(show_window2)

window2.setWindowTitle("Здоров'я")
window2.resize(600, 470)
window3.setWindowTitle("Здоров'я")
window3.resize(600, 470)


layout2 = QVBoxLayout()

line1 = QLabel()
layout2.addWidget(line1)

name = QLabel("Введіть П.І.Б.:")
layout2.addWidget(name)
pib = QLineEdit()
pib.setFixedSize(140, 20)
layout2.addWidget(pib)

years = QLabel("Повних років:")
layout2.addWidget(years)
years2 = QLineEdit()
years2.setFixedSize(140, 20)
layout2.addWidget(years2)

tyt = QLabel('Ляжте на спину і заміряте пульс за 15 секунд.Натисніть кнопку "Почати перший тест",щоб запустити таймер.\nРезультат запишіть у відповідне поле.')
layout2.addWidget(tyt)

button2 = QPushButton("Почати перший тест")
button2.setFixedSize(120, 25)
layout2.addWidget(button2)
button2.clicked.connect(start_first_test)

results1 = QLineEdit()
results1.setFixedSize(140, 20)
layout2.addWidget(results1)

tyt2 = QLabel('Виконуйте 30 присідань за 45 секунд.Для цього настисніть кнопку "Почати робити присідання",щоб запустити лічильник присідань.')
layout2.addWidget(tyt2)

button3 = QPushButton("Почати робити присідання")
button3.setFixedSize(150, 25)
layout2.addWidget(button3)
button3.clicked.connect(start_first_test2)

tyt3 = QLabel("Лягте на спину і заміряйте пульс спочатку за перші 15 секунд хвилини,потім за останні 15 секунд хвилин без виміру пульсацій.Результати запишіть у відповідні поля.")
layout2.addWidget(tyt3)

button4 = QPushButton("Почати фінальний тест")
button4.setFixedSize(140, 25)
layout2.addWidget(button4)
button4.clicked.connect(start_first_test3)

results2 = QLineEdit()
results2.setFixedSize(140, 20)
layout2.addWidget(results2)

results3 = QLineEdit()
results3.setFixedSize(140, 20)
layout2.addWidget(results3)



def calculate_rufier_index():
    p1 = int(results1.text())
    p2 = int(results2.text())
    p3 = int(results3.text())

    rufier_index = (4 * (p1 + p2 + p3) - 200) / 10
    results4.setText(f"Індекс Руф'є: {rufier_index:.2f}")
    age = int(years2.text())
    max_heart_rate = 220 - age

     

    if rufier_index >= 90:
        result_text = "Висока"
    elif rufier_index >= 81:
        result_text = "Чудова"
    elif rufier_index >= 65:
        result_text = "Середня"
    elif rufier_index >= 40:
        result_text = "Нижче середньої"
    else:
        result_text = "Низька"

    if p1 > max_heart_rate or p2 > max_heart_rate or p3 > max_heart_rate:
        result_text += " (Враховуючи вік, результат може бути занижений)"

    results5.setText("Працездатність серця: " + result_text)


button5 = QPushButton("Фінальний результат")
button5.setFixedSize(140, 25)
layout3 = QHBoxLayout()
layout3.addWidget(button5)
layout2.addLayout(layout3)
button5.clicked.connect(show_window3)
button5.clicked.connect(calculate_rufier_index)

layout4 = QVBoxLayout()

results4 = QLabel("Індекс Руф'є:")
results4.setAlignment(QtCore.Qt.AlignCenter)  
layout4.addWidget(results4)

results5 = QLabel("Працездатність серця : ")
results5.setAlignment(QtCore.Qt.AlignCenter)  
layout4.addWidget(results5)

window3.setLayout(layout4)
window2.setLayout(layout2)

window.show()
app.exec_()