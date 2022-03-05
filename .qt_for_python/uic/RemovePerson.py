# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lucas\Documents\GitHub\ShortProjects\Python\LoginApp\RemovePerson.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(425, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(425, 425))
        MainWindow.setMaximumSize(QtCore.QSize(425, 425))
        MainWindow.setStyleSheet("background-color:lightgreen;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(80, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancelar.setFont(font)
        self.pushButton_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_cancelar.setStyleSheet("background-color:white; border: 2px solid green; border-radius: 9px;")
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.label_aviso = QtWidgets.QLabel(self.centralwidget)
        self.label_aviso.setGeometry(QtCore.QRect(80, 180, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_aviso.setFont(font)
        self.label_aviso.setStyleSheet("color: green;")
        self.label_aviso.setText("")
        self.label_aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aviso.setObjectName("label_aviso")
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setGeometry(QtCore.QRect(80, 110, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_codigo.setFont(font)
        self.lineEdit_codigo.setMouseTracking(True)
        self.lineEdit_codigo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_codigo.setStyleSheet("background-color:white; border: 2px solid green; border-radius: 9px;")
        self.lineEdit_codigo.setInputMask("")
        self.lineEdit_codigo.setText("")
        self.lineEdit_codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_codigo.setPlaceholderText("Digite o código")
        self.lineEdit_codigo.setClearButtonEnabled(False)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(80, 50, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_titulo.setStyleSheet("color:green;")
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.pushButton_verificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_verificar.setEnabled(True)
        self.pushButton_verificar.setGeometry(QtCore.QRect(240, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_verificar.setFont(font)
        self.pushButton_verificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_verificar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_verificar.setStyleSheet("border: 2px solid green; border-radius: 9px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_verificar.setObjectName("pushButton_verificar")
        self.pushButton_remover = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remover.setEnabled(False)
        self.pushButton_remover.setGeometry(QtCore.QRect(80, 360, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_remover.setFont(font)
        self.pushButton_remover.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_remover.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_remover.setStyleSheet("border: 2px solid green; border-radius: 9px;\n"
"background-color: rgb(255, 200, 200);")
        self.pushButton_remover.setObjectName("pushButton_remover")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_codigo, self.pushButton_cancelar)
        MainWindow.setTabOrder(self.pushButton_cancelar, self.pushButton_verificar)
        MainWindow.setTabOrder(self.pushButton_verificar, self.pushButton_remover)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Remoção"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "CANCELAR"))
        self.label_titulo.setText(_translate("MainWindow", "Digite o código do aluno que deseja remover."))
        self.pushButton_verificar.setText(_translate("MainWindow", "VERIFICAR"))
        self.pushButton_remover.setText(_translate("MainWindow", "REMOVER"))
