import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_page(object):  # создаю дизайн для окна "password_page"
    def setupUi(self, password_page):
        password_page.setObjectName("password_page")
        password_page.resize(678, 361)
        font = QtGui.QFont()
        font.setPointSize(12)
        password_page.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(password_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 421, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_login = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.verticalLayout.addWidget(self.label_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.label_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.lineEdit_pasword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_pasword.setObjectName("lineEdit_pasword")
        self.verticalLayout.addWidget(self.lineEdit_pasword)
        self.horizontalLayoutWidget = QtWidgets.QWidget(password_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 280, 371, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reg_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.reg_label.setObjectName("reg_label")
        self.horizontalLayout.addWidget(self.reg_label)
        self.reg_buttom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reg_buttom.setObjectName("reg_buttom")
        self.horizontalLayout.addWidget(self.reg_buttom)
        self.Button_login = QtWidgets.QPushButton(password_page)
        self.Button_login.setGeometry(QtCore.QRect(490, 90, 161, 28))
        self.Button_login.setObjectName("Button_login")
        self.check_label = QtWidgets.QLabel(password_page)
        self.check_label.setGeometry(QtCore.QRect(490, 150, 161, 31))
        self.check_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.check_label.setText("")
        self.check_label.setObjectName("check_label")
        self.label = QtWidgets.QLabel(password_page)
        self.label.setGeometry(QtCore.QRect(470, 220, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.help_but = QtWidgets.QPushButton(password_page)
        self.help_but.setGeometry(QtCore.QRect(480, 310, 181, 31))
        self.help_but.setObjectName("help_but")

        self.retranslateUi(password_page)
        QtCore.QMetaObject.connectSlotsByName(password_page)

    def retranslateUi(self, password_page):
        _translate = QtCore.QCoreApplication.translate
        password_page.setWindowTitle(_translate("password_page", "Изменение пароля"))
        self.label_login.setText(_translate("password_page", "Логин:"))
        self.label_password.setText(_translate("password_page", "Пароль:"))
        self.reg_label.setText(_translate("password_page", "Впервые здесь?"))
        self.reg_buttom.setText(_translate("password_page", "Зарегестрируйтесь!"))
        self.Button_login.setText(_translate("password_page", "Вход"))
        self.label.setText(_translate("password_page",
                                      "<html><head/><body><p align=\"center\">Оказались в опасной ситуации?</p><p align=\"center\">Потерялись?</p><p align=\"center\">Не знаете что вам делать?</p></body></html>"))
        self.help_but.setText(_translate("password_page", "Мы поможем!"))


class Ui_reg_page(object):  # создаю дизайн для окна "reg_page"
    def setupUi(self, reg_page):
        reg_page.setObjectName("reg_page")
        reg_page.resize(546, 440)
        font = QtGui.QFont()
        font.setPointSize(12)
        reg_page.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(reg_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 481, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_reg = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_reg.setFont(font)
        self.label_reg.setObjectName("label_reg")
        self.verticalLayout.addWidget(self.label_reg)
        self.label_reg_login = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_reg_login.setFont(font)
        self.label_reg_login.setObjectName("label_reg_login")
        self.verticalLayout.addWidget(self.label_reg_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setMaxLength(16)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWhatsThis("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_password.setMaxLength(12)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_name_user = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name_user.setFont(font)
        self.lineEdit_name_user.setObjectName("lineEdit_name_user")
        self.verticalLayout.addWidget(self.lineEdit_name_user)
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error_label.setEnabled(True)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.reg_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reg_Button.setObjectName("reg_Button")
        self.verticalLayout.addWidget(self.reg_Button)

        self.retranslateUi(reg_page)
        QtCore.QMetaObject.connectSlotsByName(reg_page)

    def retranslateUi(self, reg_page):
        _translate = QtCore.QCoreApplication.translate
        reg_page.setWindowTitle(_translate("reg_page", "Form"))
        self.label_reg.setText(
            _translate("reg_page", "<html><head/><body><p align=\"center\">Регистрация</p></body></html>"))
        self.label_reg_login.setText(_translate("reg_page", "Ваш логин:"))
        self.label.setText(_translate("reg_page", "Ваш пароль:"))
        self.label_2.setText(_translate("reg_page", "Ваше имя:"))
        self.error_label.setText(_translate("reg_page",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                                            " color:#ff0000;\"><br/></span></p></body></html>"))
        self.reg_Button.setText(_translate("reg_page", "Зарегестрироваться"))


class Ui_main_window(object):  # создаю дизайн для окна "main_window"
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(609, 410)
        font = QtGui.QFont()
        font.setPointSize(12)
        main_window.setFont(font)
        self.name_label = QtWidgets.QLabel(main_window)
        self.name_label.setGeometry(QtCore.QRect(390, 30, 191, 41))
        self.name_label.setObjectName("name_label")
        self.user_buttom = QtWidgets.QPushButton(main_window)
        self.user_buttom.setGeometry(QtCore.QRect(390, 90, 171, 31))
        self.user_buttom.setObjectName("user_buttom")
        self.help_button = QtWidgets.QPushButton(main_window)
        self.help_button.setGeometry(QtCore.QRect(240, 350, 161, 31))
        self.help_button.setObjectName("help_button")
        self.read_label = QtWidgets.QLabel(main_window)
        self.read_label.setGeometry(QtCore.QRect(50, 40, 271, 31))
        self.read_label.setObjectName("read_label")
        self.read_Button = QtWidgets.QPushButton(main_window)
        self.read_Button.setGeometry(QtCore.QRect(90, 90, 161, 28))
        self.read_Button.setObjectName("read_Button")
        self.help_label = QtWidgets.QLabel(main_window)
        self.help_label.setGeometry(QtCore.QRect(160, 220, 301, 121))
        self.help_label.setObjectName("help_label")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Form"))
        self.name_label.setText(_translate("main_window", "Имя пользователя"))
        self.user_buttom.setText(_translate("main_window", "Личный кабинет"))
        self.help_button.setText(_translate("main_window", "Мы поможем!"))
        self.read_label.setText(_translate("main_window", "Хотите узнать что-то новое?"))
        self.read_Button.setText(_translate("main_window", "Да!"))
        self.help_label.setText(_translate("main_window",
                                           "<html><head/><body><p align=\"center\"><span style=\""
                                           " font-size:12pt;\">Оказались в опасной ситуации?</span></p><p align=\"center\"><span"
                                           " style=\" font-size:12pt;\">Потерялись?</span></p><p align=\"center\"><span"
                                           " style=\" font-size:12pt;\">Не знаете что вам делать?</span></p></body></html>"))


class Ui_main_window_user(object):
    def setupUi(self, main_window_user):
        main_window_user.setObjectName("main_window_user")
        main_window_user.resize(681, 431)
        font = QtGui.QFont()
        font.setPointSize(12)
        main_window_user.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(main_window_user)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.login_label.setObjectName("login_label")
        self.verticalLayout.addWidget(self.login_label)
        self.login = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.login.setText("")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.swap_password = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.swap_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.swap_password.setObjectName("swap_password")
        self.verticalLayout.addWidget(self.swap_password)
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.username = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.username.setText("")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.back_buttom = QtWidgets.QPushButton(main_window_user)
        self.back_buttom.setGeometry(QtCore.QRect(20, 390, 211, 31))
        self.back_buttom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_buttom.setObjectName("back_buttom")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main_window_user)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 10, 312, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 4)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.count_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count_label.setObjectName("count_label")
        self.verticalLayout_2.addWidget(self.count_label)
        self.count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count.setText("")
        self.count.setObjectName("count")
        self.verticalLayout_2.addWidget(self.count)
        self.leave_but = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.leave_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leave_but.setObjectName("leave_but")
        self.verticalLayout_2.addWidget(self.leave_but)
        self.origin = QtWidgets.QPushButton(main_window_user)
        self.origin.setGeometry(QtCore.QRect(522, 390, 151, 28))
        self.origin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.origin.setObjectName("origin")

        self.retranslateUi(main_window_user)
        QtCore.QMetaObject.connectSlotsByName(main_window_user)

    def retranslateUi(self, main_window_user):
        _translate = QtCore.QCoreApplication.translate
        main_window_user.setWindowTitle(_translate("main_window_user", "Личный кабинет"))
        self.login_label.setText(_translate("main_window_user", "Ваш логин:"))
        self.swap_password.setText(_translate("main_window_user", "Поменять пароль"))
        self.name_label.setText(_translate("main_window_user", "Ваше имя:"))
        self.back_buttom.setText(_translate("main_window_user", "<-- Назад"))
        self.count_label.setText(_translate("main_window_user", "Количество правильных ответов:"))
        self.leave_but.setText(_translate("main_window_user", "Выйти из аккаунта"))
        self.origin.setText(_translate("main_window_user", "Источники"))


class Ui_Swap_password_window(object):  # создаю дизайн для окна "Swap_password_window"
    def setupUi(self, Swap_password_window):
        Swap_password_window.setObjectName("Swap_password_window")
        Swap_password_window.resize(340, 480)
        font = QtGui.QFont()
        font.setPointSize(12)
        Swap_password_window.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Swap_password_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 261, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_old_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_old_password.setObjectName("label_old_password")
        self.verticalLayout.addWidget(self.label_old_password)
        self.lineEdit_old_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_old_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_old_password.setObjectName("lineEdit_old_password")
        self.verticalLayout.addWidget(self.lineEdit_old_password)
        self.label_new_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_new_password.setObjectName("label_new_password")
        self.verticalLayout.addWidget(self.label_new_password)
        self.lineEdit_new_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.verticalLayout.addWidget(self.lineEdit_new_password)
        self.label_new_password2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_new_password2.setObjectName("label_new_password2")
        self.verticalLayout.addWidget(self.label_new_password2)
        self.lineEdit_new_password2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_new_password2.setObjectName("lineEdit_new_password2")
        self.verticalLayout.addWidget(self.lineEdit_new_password2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Swap_password_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 380, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.back_pushButton.setObjectName("back_pushButton")
        self.horizontalLayout.addWidget(self.back_pushButton)
        self.pushButton_swap = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_swap.setObjectName("pushButton_swap")
        self.horizontalLayout.addWidget(self.pushButton_swap)
        self.error_label = QtWidgets.QLabel(Swap_password_window)
        self.error_label.setGeometry(QtCore.QRect(20, 320, 301, 51))
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Swap_password_window)
        QtCore.QMetaObject.connectSlotsByName(Swap_password_window)

    def retranslateUi(self, Swap_password_window):
        _translate = QtCore.QCoreApplication.translate
        Swap_password_window.setWindowTitle(_translate("Swap_password_window", "Изменение пароля"))
        self.label_old_password.setText(_translate("Swap_password_window",
                                                   "<html><head/><body><p align=\"center\"><span style=\""
                                                   " font-size:12pt; text-decoration: underline;\">Введите старый пароль:</span></p></body></html>"))
        self.label_new_password.setText(_translate("Swap_password_window",
                                                   "<html><head/><body><p align=\"center\"><span style=\""
                                                   " font-size:12pt; text-decoration: underline;\">Введите новый пароль:</span></p></body></html>"))
        self.label_new_password2.setText(_translate("Swap_password_window",
                                                    "<html><head/><body><p align=\"center\"><span style=\""
                                                    " font-size:12pt; text-decoration: underline;\">Повторите пароль:</span></p></body></html>"))
        self.back_pushButton.setText(_translate("Swap_password_window", "<-- Назад"))
        self.pushButton_swap.setText(_translate("Swap_password_window", "Поменять"))
        self.error_label.setText(
            _translate("Swap_password_window", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


class Ui_Help_window(object):  # создаю дизайн для окна "Help_window"
    def setupUi(self, Help_window):
        Help_window.setObjectName("Help_window")
        Help_window.resize(475, 496)
        font = QtGui.QFont()
        font.setPointSize(12)
        Help_window.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Help_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 418, 423))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 33)
        self.verticalLayout.setSpacing(44)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.question_label.setEnabled(True)
        self.question_label.setObjectName("question_label")
        self.verticalLayout.addWidget(self.question_label)
        self.question_radiob1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob1.setIconSize(QtCore.QSize(20, 20))
        self.question_radiob1.setObjectName("question_radiob1")
        self.verticalLayout.addWidget(self.question_radiob1)
        self.question_radiob2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob2.setObjectName("question_radiob2")
        self.verticalLayout.addWidget(self.question_radiob2)
        self.question_radiob3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob3.setObjectName("question_radiob3")
        self.verticalLayout.addWidget(self.question_radiob3)
        self.question_radiob4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob4.setObjectName("question_radiob4")
        self.verticalLayout.addWidget(self.question_radiob4)
        self.next_but = QtWidgets.QPushButton(Help_window)
        self.next_but.setGeometry(QtCore.QRect(160, 430, 151, 33))
        self.next_but.setObjectName("next_but")
        self.next_but.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(Help_window)
        QtCore.QMetaObject.connectSlotsByName(Help_window)

    def retranslateUi(self, Help_window):
        _translate = QtCore.QCoreApplication.translate
        Help_window.setWindowTitle(_translate("Help_window", "Быстрая помощь"))
        self.question_label.setText(_translate("Help_window",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Что у вас случилось?</span></p></body></html>"))
        self.question_radiob1.setText(_translate("Help_window", "Я потерялся"))
        self.question_radiob2.setText(_translate("Help_window", "Я попал в дтп"))
        self.question_radiob3.setText(_translate("Help_window", "Человеку стало плохо"))
        self.question_radiob4.setText(_translate("Help_window", "Произошло(-ходит) стихийное бедствие"))
        self.next_but.setText(_translate("Help_window", "Дальше"))


class Ui_Help_window1(object):  # создаю дизайн для окна "Help_window1"
    def setupUi(self, Help_window1):
        Help_window1.setObjectName("Help_window1")
        Help_window1.resize(475, 496)
        font = QtGui.QFont()
        font.setPointSize(12)
        Help_window1.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Help_window1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 418, 423))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 43)
        self.verticalLayout.setSpacing(66)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.question_label.setEnabled(True)
        self.question_label.setObjectName("question_label")
        self.verticalLayout.addWidget(self.question_label)
        self.question_radiob1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob1.setIconSize(QtCore.QSize(20, 20))
        self.question_radiob1.setObjectName("question_radiob1")
        self.verticalLayout.addWidget(self.question_radiob1)
        self.question_radiob2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob2.setObjectName("question_radiob2")
        self.verticalLayout.addWidget(self.question_radiob2)
        self.next_but = QtWidgets.QPushButton(Help_window1)
        self.next_but.setGeometry(QtCore.QRect(160, 430, 151, 33))
        self.next_but.setObjectName("next_but")
        self.next_but.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(Help_window1)
        QtCore.QMetaObject.connectSlotsByName(Help_window1)

    def retranslateUi(self, Help_window1):
        _translate = QtCore.QCoreApplication.translate
        Help_window1.setWindowTitle(_translate("Help_window1", "Быстрая помощь"))
        self.question_label.setText(_translate("Help_window1",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Где вы потерялись?</span></p></body></html>"))
        self.question_radiob1.setText(_translate("Help_window1", "В лесу"))
        self.question_radiob2.setText(_translate("Help_window1", "В городе"))
        self.next_but.setText(_translate("Help_window1", "Дальше"))


class Ui_Help_window1_1(object):  # создаю дизайн для окна "Help_window1_1"
    def setupUi(self, Help_window1_1):
        Help_window1_1.setObjectName("Help_window1_1")
        Help_window1_1.setEnabled(True)
        Help_window1_1.resize(593, 564)
        font = QtGui.QFont()
        font.setPointSize(12)
        Help_window1_1.setFont(font)
        self.info_textEdit = QtWidgets.QTextEdit(Help_window1_1)
        self.info_textEdit.setEnabled(True)
        self.info_textEdit.setGeometry(QtCore.QRect(0, 0, 591, 511))
        self.info_textEdit.setReadOnly(True)
        self.info_textEdit.setObjectName("info_textEdit")
        self.return_but = QtWidgets.QPushButton(Help_window1_1)
        self.return_but.setGeometry(QtCore.QRect(100, 520, 401, 31))
        self.return_but.setObjectName("return_but")

        self.retranslateUi(Help_window1_1)
        QtCore.QMetaObject.connectSlotsByName(Help_window1_1)

    def retranslateUi(self, Help_window1_1):
        _translate = QtCore.QCoreApplication.translate
        Help_window1_1.setWindowTitle(_translate("Help_window1_1", "Быстрая помощь"))
        self.return_but.setText(_translate("Help_window1_1", "Вернуться на главную страницу"))


class Ui_Help_window2(object):  # создаю дизайн для окна "Help_window2"
    def setupUi(self, Help_window2):
        Help_window2.setObjectName("Help_window2")
        Help_window2.resize(475, 496)
        font = QtGui.QFont()
        font.setPointSize(12)
        Help_window2.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Help_window2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 421, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 33)
        self.verticalLayout.setSpacing(49)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_question = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_question.setObjectName("label_question")
        self.verticalLayout.addWidget(self.label_question)
        self.question_radiob1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob1.setObjectName("question_radiob1")
        self.verticalLayout.addWidget(self.question_radiob1)
        self.question_radiob2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob2.setObjectName("question_radiob2")
        self.verticalLayout.addWidget(self.question_radiob2)
        self.question_radiob3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob3.setObjectName("question_radiob3")
        self.verticalLayout.addWidget(self.question_radiob3)
        self.question_radiob4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.question_radiob4.setObjectName("question_radiob4")
        self.verticalLayout.addWidget(self.question_radiob4)
        self.next_button = QtWidgets.QPushButton(Help_window2)
        self.next_button.setGeometry(QtCore.QRect(130, 450, 211, 28))
        self.next_button.setObjectName("next_button")

        self.retranslateUi(Help_window2)
        QtCore.QMetaObject.connectSlotsByName(Help_window2)

    def retranslateUi(self, Help_window2):
        _translate = QtCore.QCoreApplication.translate
        Help_window2.setWindowTitle(_translate("Help_window2", "Быстрая помощь"))
        self.label_question.setText(_translate("Help_window2",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Какое бедствие у вас произошло?</span></p></body></html>"))
        self.question_radiob1.setText(_translate("Help_window2", "Землетрясение"))
        self.question_radiob2.setText(_translate("Help_window2", "Наводнение"))
        self.question_radiob3.setText(_translate("Help_window2", "Лесной пожар"))
        self.question_radiob4.setText(_translate("Help_window2", "Надвигается ураган, буря, смерч"))
        self.next_button.setText(_translate("Help_window2", "Далее"))


class Ui_Teach_window(object):  # создаю дизайн для окна "Teach_window"
    def setupUi(self, Teach_window):
        Teach_window.setObjectName("Teach_window")
        Teach_window.resize(398, 469)
        font = QtGui.QFont()
        font.setPointSize(12)
        Teach_window.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Teach_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 50)
        self.verticalLayout.setSpacing(59)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.text_label.setObjectName("text_label")
        self.verticalLayout.addWidget(self.text_label)
        self.theme1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.theme1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.theme1.setObjectName("theme1")
        self.verticalLayout.addWidget(self.theme1)
        self.theme2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.theme2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.theme2.setObjectName("theme2")
        self.verticalLayout.addWidget(self.theme2)
        self.theme3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.theme3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.theme3.setObjectName("theme3")
        self.verticalLayout.addWidget(self.theme3)
        self.back_but = QtWidgets.QPushButton(Teach_window)
        self.back_but.setGeometry(QtCore.QRect(120, 420, 141, 31))
        self.back_but.setObjectName("back_but")

        self.retranslateUi(Teach_window)
        QtCore.QMetaObject.connectSlotsByName(Teach_window)

    def retranslateUi(self, Teach_window):
        _translate = QtCore.QCoreApplication.translate
        Teach_window.setWindowTitle(_translate("Teach_window", "Темы"))
        self.text_label.setText(_translate("Teach_window",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Выберете тему:</span></p></body></html>"))
        self.theme1.setText(_translate("Teach_window", "Первая медицинская помощь"))
        self.theme2.setText(_translate("Teach_window", "Обязанности пешехода"))
        self.theme3.setText(_translate("Teach_window", "Пожар в доме"))
        self.back_but.setText(_translate("Teach_window", "<-- Назад"))


class Ui_Theme(object):  # создаю дизайн окна Theme
    def setupUi(self, Theme):
        Theme.setObjectName("Theme")
        Theme.resize(713, 553)
        font = QtGui.QFont()
        font.setPointSize(12)
        Theme.setFont(font)
        self.textEdit_themes = QtWidgets.QTextEdit(Theme)
        self.textEdit_themes.setGeometry(QtCore.QRect(0, 0, 711, 451))
        self.textEdit_themes.setReadOnly(True)
        self.textEdit_themes.setObjectName("textEdit_themes")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Theme)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 460, 401, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.back_but.setObjectName("back_but")
        self.horizontalLayout.addWidget(self.back_but)
        self.test_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.test_but.setObjectName("test_but")
        self.horizontalLayout.addWidget(self.test_but)
        self.label = QtWidgets.QLabel(Theme)
        self.label.setGeometry(QtCore.QRect(50, 460, 101, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("6C-1D.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Theme)
        QtCore.QMetaObject.connectSlotsByName(Theme)

    def retranslateUi(self, Theme):
        _translate = QtCore.QCoreApplication.translate
        Theme.setWindowTitle(_translate("Theme", "Тема"))
        self.back_but.setText(_translate("Theme", "<-- Назад"))
        self.test_but.setText(_translate("Theme", "Пройти тест"))


class Ui_test_win(object):  # создаю дизайн для окна "Test_win"
    def setupUi(self, test_win):
        test_win.setObjectName("test_win")
        test_win.resize(536, 618)
        font = QtGui.QFont()
        font.setPointSize(12)
        test_win.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(test_win)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 471, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_answer = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_answer.setMaxLength(3)
        self.lineEdit_answer.setObjectName("lineEdit_answer")
        self.gridLayout.addWidget(self.lineEdit_answer, 2, 0, 1, 1)
        self.label_timer = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_timer.setObjectName("label_timer")
        self.gridLayout.addWidget(self.label_timer, 0, 0, 1, 1)
        self.textEdit_question = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_question.setReadOnly(True)
        self.textEdit_question.setObjectName("textEdit_question")
        self.gridLayout.addWidget(self.textEdit_question, 1, 0, 1, 1)
        self.pushButton_answer = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_answer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_answer.setObjectName("pushButton_answer")
        self.gridLayout.addWidget(self.pushButton_answer, 3, 0, 1, 1)

        self.retranslateUi(test_win)
        QtCore.QMetaObject.connectSlotsByName(test_win)

    def retranslateUi(self, test_win):
        _translate = QtCore.QCoreApplication.translate
        test_win.setWindowTitle(_translate("test_win", "Тест"))
        self.label_timer.setText(
            _translate("test_win", "<html><head/><body><p align=\"center\">00:00:00<br/></p></body></html>"))
        self.pushButton_answer.setText(_translate("test_win", "Завершить"))


class Ui_answer(object):  # создаю дизайн для окна "answer"
    def setupUi(self, answer):
        answer.setObjectName("answer")
        answer.resize(475, 353)
        font = QtGui.QFont()
        font.setPointSize(12)
        answer.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(answer)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.back_but = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.back_but.setObjectName("back_but")
        self.gridLayout.addWidget(self.back_but, 2, 1, 1, 1)
        self.back_but_read = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.back_but_read.setObjectName("back_but_read")
        self.gridLayout.addWidget(self.back_but_read, 2, 0, 1, 1)
        self.label_answer = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_answer.setObjectName("label_answer")
        self.gridLayout.addWidget(self.label_answer, 1, 0, 1, 2)

        self.retranslateUi(answer)
        QtCore.QMetaObject.connectSlotsByName(answer)

    def retranslateUi(self, answer):
        _translate = QtCore.QCoreApplication.translate
        answer.setWindowTitle(_translate("answer", "Ответ"))
        self.back_but.setText(_translate("answer", "Вернуться на главную"))
        self.back_but_read.setText(_translate("answer", "Ввернуться в учебник"))
        self.label_answer.setText(_translate("answer",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Вы правильно решили все задания!</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Вы получили 3 балла</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Вы потратили на тест $</span></p></body></html>"))


class Ui_origins_win(object):
    def setupUi(self, origins_win):
        origins_win.setObjectName("origins_win")
        origins_win.setEnabled(True)
        origins_win.resize(593, 564)
        font = QtGui.QFont()
        font.setPointSize(12)
        origins_win.setFont(font)
        self.origin_textEdit = QtWidgets.QTextEdit(origins_win)
        self.origin_textEdit.setEnabled(True)
        self.origin_textEdit.setGeometry(QtCore.QRect(0, 0, 591, 511))
        self.origin_textEdit.setReadOnly(True)
        self.origin_textEdit.setObjectName("origin_textEdit")
        self.return_but = QtWidgets.QPushButton(origins_win)
        self.return_but.setGeometry(QtCore.QRect(100, 520, 401, 31))
        self.return_but.setObjectName("return_but")

        self.retranslateUi(origins_win)
        QtCore.QMetaObject.connectSlotsByName(origins_win)

    def retranslateUi(self, origins_win):
        _translate = QtCore.QCoreApplication.translate
        origins_win.setWindowTitle(_translate("origins_win", "Источники"))
        self.origin_textEdit.setHtml(_translate("origins_win",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p></body></html>"))
        self.return_but.setText(_translate("origins_win", "Вернуться в личный кабинет"))


class Password_form(QMainWindow,
                    Ui_password_page):  # создаю первое окно с возможностью регистрацииБ входа в приложение и быстрой помощью
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загружаю дизайн
        self.setWindowTitle('Вход')  # меняю название окна
        QWidget.setFixedSize(self, 678, 361)  # фиксирую размер окна
        self.Button_login.clicked.connect(self.run)  # присоединяю кнопку к функции 'run'
        self.reg_buttom.clicked.connect(self.registr)  # присоединяю кнопку к функции 'registr'
        self.help_but.clicked.connect(self.help)  # присоединяю кнопку к функции 'help'

    def run(self):
        global form3
        con = sqlite3.connect("info.sqlite")  # подключаюсь к базе данных
        cur = con.cursor()
        result = cur.execute("""SELECT login FROM user_info""").fetchall()  # собираю все логины которые есть
        logins = []
        for elem in result:
            logins.append(elem[0])
        if self.lineEdit_login.text() in logins:  # проверяю есть ли логин вписанный пользователем ву БД
            password = cur.execute(
                f"""SELECT password, id_user FROM user_info where login = '{self.lineEdit_login.text()}'""").fetchall()  # проверяю пароль и забираю id_user для корректного отражение в личном кабинете
            if self.lineEdit_pasword.text() == password[0][0]:
                form3 = Main_window(password[0][-1])  # передаю в Main_window id пользователя
                global form4
                form4 = Help_window(1)  # передаю в Help_window флаг регистрации пользователя
                global form4_4
                form4_4 = Help_window4_result(1)  # передаю в Help_window флаг регистрации пользователя
                global id_user
                id_user = password[0][-1]  # передаю в глобальную переменную id пользователя
                form1.hide()  # закрываю окно
                form3.show()  # открываю основное (main_window) окно
                con.close()
                self.lineEdit_login.setText('')
                self.lineEdit_pasword.setText('')
            else:
                self.check_label.setText('Ошибка')  # оишбка если не совпадает пароль
                con.close()
        else:
            self.check_label.setText('Ошибка!')  # ошибка если ни один из логинов не совпадает
            con.close()
        con.close()

    def registr(self):
        form1.hide()  # перевожу пользователя на окно для регистрации
        form2.show()

    def help(self):
        global form4  # перевожу пользователя на окно с быстрой помощью
        form4 = Help_window(
            0)  # передаю значение 0, чтобы по выходу из совета пользователя перекинуло на окно входа в аккаунт, а не в main
        form1.hide()
        form4.show()


class Regist_window(QMainWindow, Ui_reg_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Регистрация')
        QWidget.setFixedSize(self, 546, 440)
        self.reg_Button.clicked.connect(self.run)

    def run(self):
        if self.lineEdit_login.text() == '':  # проверю чтобы поле логина было не пустым, иначе ошибка
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                "Заполните поле для логина!<br/></span></p></body></html>")
        elif self.lineEdit_password.text() == '':  # проверю чтобы поле пароля было не пустым, иначе ошибка
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                "Заполните поле для пароля!<br/></span></p></body></html>")
        elif self.lineEdit_name_user.text() == '':  # проверю чтобы поле имени было не пустым, иначе ошибка
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                "Заполните поле для имени!<br/></span></p></body></html>")
        elif len(self.lineEdit_password.text()) < 8:  # проверю чтобы длинну пароля было не пустым, иначе ошибка
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                "В пароле должно содержаться больше 7 символов!<br/></span></p></body></html>")
        if len(self.lineEdit_password.text()) > 7:  # если длинна пароля больше 7 символов, то проверяю пароль на различные символы
            count_upper = 0  # проверка чтобы хотя бы 1 символ был заглавной буквой
            count_lowwer = 0  # проверка чтобы хотя бы 1 символ был строчной буквой
            count_numbers = 0  # проверка чтобы хотя бы 1 символ был цифрой
            for i in self.lineEdit_password.text():  # проверю пароль на наличие разных символов, иначе оишбка
                if i in '1234567890':
                    count_numbers += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё':
                    count_lowwer += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё'.upper():
                    count_upper += 1
                else:
                    self.error_label.setText(                       # если не выполняется минимальный критерий - ошибка
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                        "В пароле должны быть только цифры и буквы!<br/></span></p></body></html>")
                    break
            con = sqlite3.connect("info.sqlite")  # подключаюсь к БД
            cur = con.cursor()
            result = cur.execute("""SELECT login, id_user FROM user_info""").fetchall()  # беру из БД логин и id юзера
            logins = []
            ids = []
            for elem in result:  # распределяю логины и id
                logins.append(elem[0])
                ids.append(elem[1])
            ids = max(ids) + 1  # создаю новый неповторяющийся id_user
            if count_upper == 0:  # проверяю пароль на наличие заглавных букв
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть заглавные буквы!<br/></span></p></body></html>")
            elif count_lowwer == 0:  # проверяю пароль на наличие строчных букв
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть строчные буквы!<br/></span></p></body></html>")
            elif count_numbers == 0:  # проверяю пароль на наличие цифр
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть цифры!<br/></span></p></body></html>")
            elif self.lineEdit_login.text() in logins:  # проверяю чтобы логин не повторялся
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "Этот логин уже занят!<br/></span></p></body></html>")
            else:
                global form3
                global form4
                form4 = Help_window(1)
                inf = cur.execute(
                    f"""INSERT INTO user_info(id_user, login, password, username, score)
                     VALUES('{str(ids)}', '{self.lineEdit_login.text()}',
                     '{self.lineEdit_password.text()}', '{self.lineEdit_name_user.text()}', '0')""")  # создаю нового пользователя в БД
                con.commit()  # сохраняю изменения таблицы
                result = cur.execute("""SELECT id_user FROM user_info""").fetchall()
                list_id = []
                for elem in result:
                    list_id.append(elem[0])
                list_id.sort()
                result = list_id[-1]  # определяю id нового юзера и запоминаю его
                con.close()
                global id_user
                id_user = result
                form2.hide()
                form3 = Main_window(result)
                form3.show()


class Main_window(QMainWindow, Ui_main_window):  # создаю Main_window
    def __init__(self, id):  # прописываю обязательную передачу id
        super().__init__()
        self.id = id
        self.setupUi(self)
        self.setWindowTitle('Главное окно')
        QWidget.setFixedSize(self, 609, 410)
        self.user_buttom.clicked.connect(self.run)  #
        self.help_button.clicked.connect(self.open_help_win)  # привязываю кнопки
        self.read_Button.clicked.connect(self.read)  #
        global form5_3
        form5_3 = Answer_win(0, '00:00:00',
                             self.id)  # передаю в class Answer_win: 1. id темы, 2. время прохождения теста, 3. id_user

    def run(self):
        global form3_1
        form3_1 = Main_window_user(self.id)
        form3.hide()
        form3_1.show()

    def open_help_win(self):
        form4.show()
        form3.hide()

    def read(self):
        form3.hide()
        form5.show()


class Main_window_user(QMainWindow, Ui_main_window_user):  # сощдаю class Main_window_user
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id
        QWidget.setFixedSize(self, 679, 434)
        self.swap_password.clicked.connect(self.run)
        self.back_buttom.clicked.connect(self.back)
        self.leave_but.clicked.connect(self.leave)
        self.origin.clicked.connect(self.origins)
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        info = cur.execute(f"""SELECT login, username, score FROM user_info
                                            WHERE id_user = {id}""").fetchall()  # получаю информацию о пользователе
        con.close()
        info = info[0]
        self.login.setText(str(info[0]))  #
        self.username.setText(str(info[1]))  # вывожу информацию в различные labels
        self.count.setText(str(info[2]))  #

    def run(self):
        global form3_2
        form3_2 = Swap_password(self.id)  # передаю в окно для изминения пароля id пользователя и запускаю это окно
        form3_1.hide()
        form3_2.show()

    def back(self):
        form3_1.hide()
        form3.show()

    def leave(self):  # обрабатываю функцию выхода из личного кабинета
        valid = QMessageBox.question(
            self, 'Выход из аккаунта', "Вы действительно хотите выйти из аккаунта?",
            QMessageBox.Yes, QMessageBox.No)
        # уточняю у пользователя хочет ли он выйти из аккаунта
        if valid == QMessageBox.Yes:
            form3_1.hide()
            form1.show()

    def origins(self):
        form3_1.hide()
        form6.show()


class Origin_win(QMainWindow, Ui_origins_win):  # создаю класс Origin_win,
    # в котором показываю ссылки на сайты с которых взял информацию
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QWidget.setFixedSize(self, 593, 564)
        self.return_but.clicked.connect(self.back)
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        info = cur.execute("""SELECT help_text FROM help_info
                                                            WHERE id = 15""").fetchall()
        info = info[0][0]
        with open(info, 'r', encoding='utf8') as f:
            data = f.read()
            self.origin_textEdit.setText(data)
        con.close()

    def back(self):
        form6.hide()
        form3_1.show()


class Swap_password(QMainWindow, Ui_Swap_password_window):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setupUi(self)
        QWidget.setFixedSize(self, 340, 480)
        self.pushButton_swap.clicked.connect(self.run)
        self.back_pushButton.clicked.connect(self.back)
        self.error_label.setWordWrap(True)  # разрешаю перенос слов в label

    def run(self):
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        info = cur.execute(f"""SELECT password FROM user_info
                                    WHERE id_user = {self.id}""").fetchall()  # получаю правильный пароль пользователя
        info = info[0][0]
        con.close()
        if self.lineEdit_old_password.text() == info:  # если введенный пароль совпадает со старым
            count_upper = 0
            count_lowwer = 0
            count_numbers = 0
            for i in self.lineEdit_new_password.text():  # начинаю проверку нового пароля
                if i in '1234567890':
                    count_numbers += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё':
                    count_lowwer += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё'.upper():
                    count_upper += 1
                else:
                    self.error_label.setText(
                        "<html><head/><body><p align=\"center\"><span style=\""
                        " font-size:12pt; color:#ff0000;\">"
                        "В пароле должны быть только цифры и буквы!<br/></span></p></body></html>")
                    break
            if count_upper == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть заглавные буквы!<br/></span></p></body></html>")
            elif count_lowwer == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть строчные буквы!<br/></span></p></body></html>")
            elif count_numbers == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "В пароле должны быть цифры!<br/></span></p></body></html>")
            elif len(self.lineEdit_new_password.text()) < 8:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">"
                    "Пароль должен быть больше 7 символов!<br/></span></p></body></html>")
            elif self.lineEdit_new_password.text() == self.lineEdit_new_password2.text() and len(
                    self.lineEdit_new_password.text()) > 7:
                con = sqlite3.connect("info.sqlite")
                cur = con.cursor()
                inf = cur.execute(
                    f"""UPDATE user_info SET password = '{self.lineEdit_new_password.text()}'
                     where id_user = '{self.id}'""")  # обновляю пароль в БД для пользователя
                con.commit()
                con.close()
                form3_2.hide()
                form3_1.show()
        else:
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                " color:#ff0000;\">Неправильный пароль<br/></span></p></body></html>")

    def back(self):
        form3_2.hide()  # делаю возвращение на прошлое окно
        form3_1.show()


class Help_window(QMainWindow, Ui_Help_window):  # class Help_window
    def __init__(self, reg):
        super().__init__()
        self.reg = reg
        self.setupUi(self)
        QWidget.setFixedSize(self, 475, 496)
        self.next_but.clicked.connect(self.run)

    def run(self):
        global form4_1_1  # передаю в различные формы нужные id и флаг регистрации
        global form4_1
        global form4_4
        if self.question_radiob1.isChecked():
            form4_1 = Help_window1(self.reg)
            form4_1.show()
            form4.hide()
        elif self.question_radiob2.isChecked():
            form4_1_1 = Help_window1_result1(3, self.reg)
            form4_1_1.show()
            form4.hide()
        elif self.question_radiob3.isChecked():
            form4_1_1 = Help_window1_result1(4, self.reg)
            form4_1_1.show()
            form4.hide()
        elif self.question_radiob4.isChecked():
            form4_4 = Help_window4_result(self.reg)
            form4_4.show()
            form4.hide()


class Help_window1(QMainWindow, Ui_Help_window1):  # создаю class Help_window1
    def __init__(self, reg):
        super().__init__()
        self.setupUi(self)
        self.reg = reg
        QWidget.setFixedSize(self, 475, 496)
        self.next_but.clicked.connect(self.run)

    def run(self):
        global form4_1_1
        if self.question_radiob1.isChecked():
            form4_1_1 = Help_window1_result1(1, self.reg)
            form4_1_1.show()
            form4_1.hide()
        elif self.question_radiob2.isChecked():
            form4_1_1 = Help_window1_result1(2, self.reg)
            form4_1_1.show()
            form4_1.hide()


class Help_window1_result1(QMainWindow, Ui_Help_window1_1):  # создаю class Help_window1_result1
    def __init__(self, count, reg):
        super().__init__()
        self.reg = reg  # флаг регистрации
        self.setupUi(self)
        self.count = count  # выступает как id_user
        QWidget.setFixedSize(self, 593, 564)
        self.return_but.clicked.connect(self.back)
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        if self.count == 1:  # начинаю проверку по id чтобы понять какой текст выводить из БД
            result = cur.execute("""SELECT help_text FROM help_info
                                        WHERE id = 1""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 2:
            result = cur.execute("""SELECT help_text FROM help_info
                                                    WHERE id = 2""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 3:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                WHERE id = 3""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 4:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                WHERE id = 4""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 5:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                        WHERE id = 5""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 6:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                            WHERE id = 6""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 7:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                            WHERE id = 7""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()
        elif self.count == 8:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                            WHERE id = 8""").fetchall()
            result = result[0]
            self.info_textEdit.setText(str(result[0]))
            con.close()

    def back(self):
        if self.reg == 0:  # если пользователь неавторизированн
            form4_1_1.hide()  # то выходить на окно со входом
            form1.show()
        else:
            form4_1_1.hide()  # иначе возвращается в главное меню
            form3.show()


class Help_window4_result(QMainWindow, Ui_Help_window2):  # как class Help_window1, разница лишь в тексте
    def __init__(self, reg):
        super().__init__()
        self.reg = reg
        self.setupUi(self)
        QWidget.setFixedSize(self, 475, 496)
        self.next_button.clicked.connect(self.run)

    def run(self):
        global form4_1_1
        if self.question_radiob1.isChecked():
            form4_1_1 = Help_window1_result1(5, self.reg)
            form4_1_1.show()
            form4_4.hide()
        elif self.question_radiob2.isChecked():
            form4_1_1 = Help_window1_result1(6, self.reg)
            form4_1_1.show()
            form4_4.hide()
        elif self.question_radiob3.isChecked():
            form4_1_1 = Help_window1_result1(7, self.reg)
            form4_1_1.show()
            form4_4.hide()
        elif self.question_radiob4.isChecked():
            form4_1_1 = Help_window1_result1(8, self.reg)
            form4_1_1.show()
            form4_4.hide()


class Teach_window(QMainWindow, Ui_Teach_window):  # создаю class Teach_window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QWidget.setFixedSize(self, 398, 469)
        self.back_but.clicked.connect(self.back)  #
        self.theme1.clicked.connect(self.theme1_1)  # конекчу кнопки
        self.theme2.clicked.connect(self.theme2_1)  #
        self.theme3.clicked.connect(self.theme3_1)  #

    def back(self):
        form5.hide()  # обрабатываю кнопку выхода
        form3.show()

    def theme1_1(self):  # обрабатываю разные темы
        global form5_1
        form5_1 = Theme(1)
        form5_1.show()
        form5.hide()

    def theme2_1(self):
        global form5_1
        form5_1 = Theme(2)
        form5_1.show()
        form5.hide()

    def theme3_1(self):
        global form5_1
        form5_1 = Theme(3)
        form5_1.show()
        form5.hide()


class Theme(QMainWindow, Ui_Theme):  # создаю class Theme
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        QWidget.setFixedSize(self, 713, 553)
        self.back_but.clicked.connect(self.back)
        self.test_but.clicked.connect(self.test)
        self.id = id
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        if self.id == 1:  # загружаю сценарии в зависимости id
            result = cur.execute("""SELECT help_text FROM help_info
                                                WHERE id = 9""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit_themes.setText(data)
            self.label.setPixmap(QtGui.QPixmap("help.jpg"))
            con.close()
        elif self.id == 2:
            result = cur.execute("""SELECT help_text FROM help_info
                                                            WHERE id = 10""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit_themes.setText(data)
            self.label.setPixmap(QtGui.QPixmap("man.png"))
            con.close()
        elif self.id == 3:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                        WHERE id = 11""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit_themes.setText(data)
            self.label.setPixmap(QtGui.QPixmap("fire.png"))
            con.close()

    def back(self):
        form5_1.hide()
        form5.show()

    def test(self):
        global form5_2
        form5_2 = Test_win(self.id)  # передаю id темы, чтобы определять какой тест нужно вывести
        form5_2.show()
        form5_1.hide()


class Test_win(QMainWindow, Ui_test_win):  # создаю class Test_win
    def __init__(self, id):
        self.id = id
        super().__init__()
        self.setupUi(self)
        QWidget.setFixedSize(self, 536, 618)
        self.pushButton_answer.clicked.connect(self.run)
        self.timer = QtCore.QTimer()  # создаю объект QTimer() чтобы засекать время проходения теста
        self.time = QtCore.QTime(0, 0, 0)
        self.timer.timeout.connect(self.timerEvent)  # подключаю таймер к функции времени
        self.timer.start(1000)  # делаю задержку между изменением времени в 1000 милисекунд (в 1 секунду)
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        if self.id == 1:  # подгружаю тесты из файлов .txt
            result = cur.execute("""SELECT help_text FROM help_info
                                                        WHERE id = 12""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.answer = data[
                              -3:]  # вывожу весь текст кроме последних 3 символов, т.к. последнии 3 символа это ответ
                self.textEdit_question.setText(data[:-3])
            con.close()
        elif self.id == 2:
            result = cur.execute("""SELECT help_text FROM help_info
                                                                    WHERE id = 13""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit_question.setText(data[:-3])
            con.close()
        elif self.id == 3:
            result = cur.execute("""SELECT help_text FROM help_info WHERE id = 14""").fetchall()
            result = result[0]
            with open(result[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit_question.setText(data[:-3])
            con.close()

    def run(self):
        global form5_3
        if self.id == 1:  # проверка id теста и дальше проверка на правильность ответа, выдача кол баллов и времени, затраченного на тест
            if self.lineEdit_answer.text() == '321':
                form5_3 = Answer_win(3, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() == '':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[1] == '2' and self.lineEdit_answer.text()[0] != '3' and \
                    self.lineEdit_answer.text()[2] != '1':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[2] == '1' and self.lineEdit_answer.text()[0] != '3' and \
                    self.lineEdit_answer.text()[1] != '2':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif (self.lineEdit_answer.text()[:2] == '32') or (self.lineEdit_answer.text()[1:] == '21') or (
                    self.lineEdit_answer.text()[0] == '3' and self.lineEdit_answer.text()[2] == '1'):
                form5_3 = Answer_win(2, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[0] == '3' and self.lineEdit_answer.text()[1:] != '21':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() != '321':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
        elif self.id == 2:
            if self.lineEdit_answer.text() == '111':
                form5_3 = Answer_win(3, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() == '':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[1] == '1' and self.lineEdit_answer.text()[0] != '1' and \
                    self.lineEdit_answer.text()[2] != '1':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[2] == '1' and self.lineEdit_answer.text()[0] != '1' and \
                    self.lineEdit_answer.text()[1] != '1':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif (self.lineEdit_answer.text()[:2] == '11') or (self.lineEdit_answer.text()[1:] == '11') or (
                    self.lineEdit_answer.text()[0] == '1' and self.lineEdit_answer.text()[2] == '1'):
                form5_3 = Answer_win(2, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[0] == '1' and self.lineEdit_answer.text()[1:] != '11':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() != '111':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
        elif self.id == 3:
            if self.lineEdit_answer.text() == '213':
                form5_3 = Answer_win(3, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() == '':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[1] == '1' and self.lineEdit_answer.text()[0] != '2' and \
                    self.lineEdit_answer.text()[2] != '3':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[2] == '3' and self.lineEdit_answer.text()[0] != '2' and \
                    self.lineEdit_answer.text()[1] != '1':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif (self.lineEdit_answer.text()[:2] == '21') or (self.lineEdit_answer.text()[1:] == '13') or (
                    self.lineEdit_answer.text()[0] == '2' and self.lineEdit_answer.text()[2] == '3'):
                form5_3 = Answer_win(2, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text()[0] == '2' and self.lineEdit_answer.text()[1:] != '13':
                form5_3 = Answer_win(1, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()
            elif self.lineEdit_answer.text() != '213':
                form5_3 = Answer_win(0, self.time.toString('hh:mm:ss'), id_user)
                form5_2.hide()
                form5_3.show()

    def timerEvent(self):
        self.time = self.time.addSecs(1)  # добавляю в таймер новую секунду
        self.label_timer.setText(
            f"<html><head/><body><p align=\"center\">{self.time.toString('hh:mm:ss')}<br/></p></body></html>")


class Answer_win(QMainWindow, Ui_answer):
    def __init__(self, count, time, id):
        self.count = count  # количество баллов (правильных ответов)
        self.time = time  # время
        self.id = id  # id юзера
        super().__init__()
        self.setupUi(self)
        QWidget.setFixedSize(self, 475, 353)
        result = self.label_answer.text().replace('3', f'{self.count}', 1).replace('$', f'{self.time}',
                                                                                   1)  # заменяю '3'
        # на колчество баллов на баллы которые получил пользователь и заменяю '$' на время, затраченное пользователем
        if self.count == 1:
            result = result.replace('Вы правильно решили все задания!', 'Вы запомнили не все!', 1)
            result = result.replace('балла', 'балл', 1)  # если пользователь получил 1 балл, то меняеться окончание
        elif self.count == 0:
            result = result.replace('Вы правильно решили все задания!', 'Подготовтесь лучше!', 1)
            result = result.replace('балла', 'баллов')  # если пользователь получил 0 баллов, то меняеться окончание
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        result2 = cur.execute(
            f"""SELECT score FROM user_info WHERE id_user = '{self.id}'""").fetchall()  # получаю score пользователя
        score = result2[0][0]
        inf = cur.execute(
            f"""UPDATE user_info SET score = '{self.count + score}' where id_user = '{self.id}'""")  # обноваляю score
                                                                                                     # пользователя
        con.commit()
        con.close()
        self.label_answer.setText(result)
        self.back_but.clicked.connect(self.back_but_win)
        self.back_but_read.clicked.connect(self.back_but_readtext)

    def back_but_win(self):
        form5_3.hide()
        form3.show()

    def back_but_readtext(self):
        form5.show()
        form5_3.hide()


def except_hook(cls, exception, traceback):  # функция чтобы видеть код ошибки
    sys.__excepthook__(cls, exception, traceback)


id_user = 1
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form1 = Password_form()  # прописываю различные переменные чтобы
    form2 = Regist_window()  # вызывать окна, без переменных окна при вызове сами закрываться
    form3 = Main_window(1)
    form3_1 = Main_window_user(1)
    form3_2 = Swap_password(1)
    form4 = Help_window(0)
    form4_1 = Help_window1(0)
    form4_1_1 = Help_window1_result1(3, 0)
    form4_4 = Help_window4_result(0)
    form5 = Teach_window()
    form5_1 = Theme(0)
    form5_2 = Test_win(1)
    form5_3 = Answer_win(0, '00:00:00', 1)
    form6 = Origin_win()
    form1.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
