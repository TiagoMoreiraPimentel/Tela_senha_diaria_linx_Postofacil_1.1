import codigo

# COLE O CODIGO ALTERADO AQUI NO LOGAR DO ABAIXO
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(293, 344)
        mainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        mainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 311, 81))
        self.frame.setStyleSheet("image: url('C:/Users/nitro/Desktop/projeto senha diaria linx/no3.png');")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, 80, 311, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 10, 225, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-10, 130, 311, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textbox_senha = QtWidgets.QLabel(self.frame_3)
        self.textbox_senha.setGeometry(QtCore.QRect(100, 20, 104, 58))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textbox_senha.setFont(font)
        self.textbox_senha.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 36pt \"MS Shell Dlg 2\";")
        self.textbox_senha.setTextFormat(QtCore.Qt.AutoText)
        self.textbox_senha.setScaledContents(False)
        self.textbox_senha.setWordWrap(False)
        self.textbox_senha.setOpenExternalLinks(False)
        self.textbox_senha.setObjectName("textbox_senha")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-10, 230, 311, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.botao_sair = QtWidgets.QPushButton(self.frame_4)
        self.botao_sair.setGeometry(QtCore.QRect(120, 10, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_sair.sizePolicy().hasHeightForWidth())
        self.botao_sair.setSizePolicy(sizePolicy)
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom-color: rgb(255, 85, 0);\n"
"border-top-color: rgb(255, 85, 0);\n"
"border-color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.botao_sair.setObjectName("botao_sair")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(-10, 280, 311, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 271, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_2.setObjectName("label_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.botao_sair.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Programa - Senha Diaria Linx NO3"))
        self.label.setText(_translate("mainWindow", "A senha diaria é:"))
        self.textbox_senha.setText(_translate("mainWindow", "0205"))
        self.botao_sair.setText(_translate("mainWindow", "FECHAR"))
        self.label_2.setText(_translate("mainWindow", "Desenvolvido por Tiago Pimentel - Cel: (11)9 47096148"))
        # COLE O CODIGO ALTERADO AQUI NO LOGAR DO ACIMA

        #FIXO NÃO ALTERAR
        senha1 = str(codigo.senha1)
        senha2 = str(codigo.senha2)
        senha3 = str(codigo.senha3)
        senha4 = str(codigo.senha4)
        self.textbox_senha.setText(senha1 + senha2 + senha3 + senha4)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

