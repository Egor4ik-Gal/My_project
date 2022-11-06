import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_page(object):
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
        self.label.setText(_translate("password_page", "<html><head/><body><p align=\"center\">Оказались в опасной ситуации?</p><p align=\"center\">Потерялись?</p><p align=\"center\">Не знаете что вам делать?</p></body></html>"))
        self.help_but.setText(_translate("password_page", "Мы поможем!"))



class Ui_reg_page(object):
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


class Ui_main_window(object):
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
        main_window_user.resize(679, 434)
        font = QtGui.QFont()
        font.setPointSize(12)
        main_window_user.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(main_window_user)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 331, 361))
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
        self.swap_password.setObjectName("swap_password")
        self.verticalLayout.addWidget(self.swap_password)
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.username = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username.setText("")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main_window_user)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 10, 311, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.count_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count_label.setObjectName("count_label")
        self.verticalLayout_2.addWidget(self.count_label)
        self.count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count.setText("")
        self.count.setObjectName("count")
        self.verticalLayout_2.addWidget(self.count)
        self.back_buttom = QtWidgets.QPushButton(main_window_user)
        self.back_buttom.setGeometry(QtCore.QRect(20, 390, 211, 28))
        self.back_buttom.setObjectName("back_buttom")

        self.retranslateUi(main_window_user)
        QtCore.QMetaObject.connectSlotsByName(main_window_user)

    def retranslateUi(self, main_window_user):
        _translate = QtCore.QCoreApplication.translate
        main_window_user.setWindowTitle(_translate("main_window_user", "Личный кабинет"))
        self.login_label.setText(_translate("main_window_user", "Логин:"))
        self.swap_password.setText(_translate("main_window_user", "Поменять пароль"))
        self.name_label.setText(_translate("main_window_user", "Ваше имя:"))
        self.count_label.setText(_translate("main_window_user", "Количество правильных ответов:"))
        self.back_buttom.setText(_translate("main_window_user", "<-- Назад"))


class Ui_Swap_password_window(object):
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


class Ui_Help_window(object):
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


class Ui_Help_window1(object):
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


class Ui_Help_window1_1(object):
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


class Ui_Help_window2(object):
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


class Password_form(QMainWindow, Ui_password_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Вход')
        QWidget.setFixedSize(self, 678, 361)
        self.Button_login.clicked.connect(self.run)
        self.reg_buttom.clicked.connect(self.registr)
        self.help_but.clicked.connect(self.help)

    def run(self):
        global form3
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT login FROM user_info""").fetchall()
        logins = []
        for elem in result:
            logins.append(elem[0])
        if self.lineEdit_login.text() in logins:
            password = cur.execute(
                f"""SELECT password, id_user FROM user_info where login = '{self.lineEdit_login.text()}'""").fetchall()
            if self.lineEdit_pasword.text() == password[0][0]:
                form3 = Main_window(password[0][-1])
                global form4
                form4 = Help_window(1)
                global form4_4
                form4_4 = Help_window4_result(1)
                form1.hide()
                form3.show()
                con.close()
            else:
                self.check_label.setText('Ошибка')
                con.close()
        else:
            self.check_label.setText('Ошибка!')
            con.close()
        con.close()

    def registr(self):
        form1.hide()
        form2.show()

    def help(self):
        global form4
        form4 = Help_window(0)
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
        if self.lineEdit_login.text() == '':
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Заполните поле для логина!<br/></span></p></body></html>")
        elif self.lineEdit_password.text() == '':
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Заполните поле для пароля!<br/></span></p></body></html>")
        elif self.lineEdit_name_user.text() == '':
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Заполните поле для имени!<br/></span></p></body></html>")
        if len(self.lineEdit_password.text()) > 7:
            count_upper = 0
            count_lowwer = 0
            count_numbers = 0
            for i in self.lineEdit_password.text():
                if i in '1234567890':
                    count_numbers += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё':
                    count_lowwer += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё'.upper():
                    count_upper += 1
                else:
                    self.error_label.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть только цифры и буквы!<br/></span></p></body></html>")
                    break
            con = sqlite3.connect("info.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT login FROM user_info""").fetchall()
            logins = []
            for elem in result:
                logins.append(elem[0])
            if count_upper == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть заглавные буквы!<br/></span></p></body></html>")
            elif count_lowwer == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть строчные буквы!<br/></span></p></body></html>")
            elif count_numbers == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть цифры!<br/></span></p></body></html>")
            elif self.lineEdit_login.text() in logins:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Этот логин уже занят!<br/></span></p></body></html>")
            else:
                global form3
                inf = cur.execute(
                    f"""INSERT INTO user_info(login, password, username, score) VALUES('{self.lineEdit_login.text()}',
                     '{self.lineEdit_password.text()}', '{self.lineEdit_name_user.text()}', '0')""")
                con.commit()
                result = cur.execute("""SELECT id_user FROM user_info""").fetchall()
                result = result[0][0]
                con.close()
                form2.hide()
                form3 = Main_window(result)
                form3.show()


class Main_window(QMainWindow, Ui_main_window):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setupUi(self)
        self.setWindowTitle('Главное окно')
        QWidget.setFixedSize(self, 609, 410)
        self.user_buttom.clicked.connect(self.run)
        self.help_button.clicked.connect(self.open_help_win)

    def run(self):
        global form3_1
        form3_1 = Main_window_user(self.id)
        form3.hide()
        form3_1.show()

    def open_help_win(self):
        form4.show()
        form3.hide()


class Main_window_user(QMainWindow, Ui_main_window_user):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id
        QWidget.setFixedSize(self, 679, 434)
        self.swap_password.clicked.connect(self.run)
        self.back_buttom.clicked.connect(self.back)
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        info = cur.execute(f"""SELECT login, username FROM user_info
                                            WHERE id_user = {id}""").fetchall()
        con.close()
        info = info[0]
        self.login.setText(str(info[0]))
        self.username.setText(str(info[1]))

    def run(self):
        global form3_2
        form3_2 = Swap_password(self.id)
        form3_1.hide()
        form3_2.show()

    def back(self):
        form3_1.hide()
        form3.show()


class Swap_password(QMainWindow, Ui_Swap_password_window):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setupUi(self)
        QWidget.setFixedSize(self, 340, 480)
        self.pushButton_swap.clicked.connect(self.run)
        self.back_pushButton.clicked.connect(self.back)
        self.error_label.setWordWrap(True)

    def run(self):
        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        info = cur.execute(f"""SELECT password FROM user_info
                                                    WHERE id_user = {self.id}""").fetchall()
        info = info[0][0]
        con.close()
        if self.lineEdit_old_password.text() == info:
            count_upper = 0
            count_lowwer = 0
            count_numbers = 0
            for i in self.lineEdit_new_password.text():
                if i in '1234567890':
                    count_numbers += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё':
                    count_lowwer += 1
                elif i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъэфжыдвлаопрмистчяьбюё'.upper():
                    count_upper += 1
                else:
                    self.error_label.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть только цифры и буквы!<br/></span></p></body></html>")
                    break
            if count_upper == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть заглавные буквы!<br/></span></p></body></html>")
            elif count_lowwer == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть строчные буквы!<br/></span></p></body></html>")
            elif count_numbers == 0:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">В пароле должны быть цифры!<br/></span></p></body></html>")
            elif len(self.lineEdit_new_password.text()) < 8:
                self.error_label.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Пароль должен быть больше 7 символов!<br/></span></p></body></html>")
            elif self.lineEdit_new_password.text() == self.lineEdit_new_password2.text() and len(
                    self.lineEdit_new_password.text()) > 7:
                con = sqlite3.connect("info.sqlite")
                cur = con.cursor()
                inf = cur.execute(
                    f"""UPDATE user_info SET password = '{self.lineEdit_new_password.text()}' where id_user = '{self.id}'""")
                con.commit()
                con.close()
                form3_2.hide()
                form3_1.show()
        else:
            self.error_label.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;"
                " color:#ff0000;\">Неправильный пароль<br/></span></p></body></html>")

    def back(self):
        form3_2.hide()
        form3_1.show()


class Help_window(QMainWindow, Ui_Help_window):
    def __init__(self, reg):
        super().__init__()
        self.reg = reg
        self.setupUi(self)
        QWidget.setFixedSize(self, 475, 496)
        self.next_but.clicked.connect(self.run)

    def run(self):
        global form4_1_1
        global form4_1
        global form4_4
        if self.question_radiob1.isChecked():
            form4_1 = Help_window1(self.reg)
            form4_1.show()
            form4.hide()
        #
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


#


class Help_window1(QMainWindow, Ui_Help_window1):
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


class Help_window1_result1(QMainWindow, Ui_Help_window1_1):
    def __init__(self, count, reg):
        super().__init__()
        self.reg = reg
        self.setupUi(self)
        self.count = count
        QWidget.setFixedSize(self, 593, 564)
        self.return_but.clicked.connect(self.back)

        con = sqlite3.connect("info.sqlite")
        cur = con.cursor()
        if self.count == 1:
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
        if self.reg == 0:
            form4_1_1.hide()
            form1.show()
        else:
            form4_1_1.hide()
            form3.show()


class Help_window4_result(QMainWindow, Ui_Help_window2):
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


class Teach_window(QMainWindow, ):
    pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form1 = Password_form()
    form2 = Regist_window()
    form3 = Main_window(1)
    form3_1 = Main_window_user(1)
    form3_2 = Swap_password(1)
    form4 = Help_window(0)
    form4_1 = Help_window1(0)
    form4_1_1 = Help_window1_result1(3, 0)
    form4_4 = Help_window4_result(0)
    form1.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
