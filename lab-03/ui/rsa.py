from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'F:\CHKHAN-0329\lab-03\cipher\rsa\platforms'
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 211, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 90, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 200, 101, 31))
        self.label_5.setObjectName("label_5")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(140, 300, 101, 31))
        self.btn_encrypt.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(270, 300, 93, 31))
        self.btn_decrypt.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(580, 300, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(700, 300, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(520, 20, 101, 31))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        # connect buttons to handlers
        # self.btn_encrypt.clicked.connect(self.on_encrypt)
        # self.btn_decrypt.clicked.connect(self.on_decrypt)
        # self.btn_sign.clicked.connect(self.on_sign)
        # self.btn_verify.clicked.connect(self.on_verify)
        # self.btn_gen_keys.clicked.connect(self.on_gen_keys)
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(100, 80, 311, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(100, 190, 311, 91))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(530, 190, 311, 91))
        self.txt_sign.setObjectName("txt_sign")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(530, 80, 311, 91))
        self.txt_info.setObjectName("txt_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">RSA CIPHER</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Plain Text:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">CipherText:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Infomation:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Signature:</span></p></body></html>"))
        self.btn_encrypt.setToolTip(_translate("MainWindow", "<html><head/><body><p>xc</p></body></html>"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))

    # simple handlers (placeholders) ---- add below retranslateUi or at end of class
    def on_encrypt(self):
        plain = self.txt_plain_text.toPlainText()
        cipher = plain[::-1]  # placeholder: reverse text
        self.txt_cipher_text.setPlainText(cipher)
        self.txt_info.setPlainText("Encrypted (placeholder)")

    def on_decrypt(self):
        cipher = self.txt_cipher_text.toPlainText()
        plain = cipher[::-1]  # reverse back
        self.txt_plain_text.setPlainText(plain)
        self.txt_info.setPlainText("Decrypted (placeholder)")

    def on_gen_keys(self):
        # placeholder behaviour
        self.txt_info.setPlainText("Keys generated (placeholder)")

    def on_sign(self):
        msg = self.txt_plain_text.toPlainText()
        sig = "SIG:" + msg[:10]  # placeholder signature
        self.txt_sign.setPlainText(sig)
        self.txt_info.setPlainText("Signed (placeholder)")

    def on_verify(self):
        # placeholder verify
        self.txt_info.setPlainText("Verified (placeholder)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
