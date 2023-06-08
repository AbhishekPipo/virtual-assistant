import sys
from PyQt5.QtWidgets import QWidget,QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from loginWindowGUI import Ui_Form




class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        print("Login Window")
        self.loginUI = Ui_Form()
        self.loginUI.setupUi(self)


        self.loginUI.Wrongcredmovie = QtGui.QMovie("C:\\Users\\sumit\\Desktop\\jarvis\\wrongcred.gif")
        self.loginUI.Wrongcred.setMovie(self.loginUI.Wrongcredmovie)


        self.loginUI.Wrongcred.hide()
        self.loginUI.Login.clicked.connect(self.ValidateLogin)
        self.loginUI.Password.setEchoMode(QLineEdit.Password)
        self.loginUI.Exit.clicked.connect(self.close)
        self.loginUI.Retry.clicked.connect(self.retrybutton)
    def ValidateLogin(self):
        uname =self.loginUI.username.text()
        pas = self.loginUI.Password.text()
        if uname == 'Rakshith' and pas == 'jarvis':
            print("Access Granted")
           
        else:
            self.startMovie()

    def startMovie(self):
        self.loginUI.Wrongcred.show()
        self.loginUI.Wrongcredmovie.start()
    def stopMovie(self):
        self.loginUI.Wrongcredmovie.stop()
        self.loginUI.Wrongcred.hide()
    def retrybutton(self):
        self.loginUI.username.clear()
        self.loginUI.Password.clear()
        self.stopMovie()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())
