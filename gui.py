# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat Oct 28 20:24:28 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1091, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(14)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(True)
        # PyQT禁止窗口最大化按钮：
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # PyQT禁止调整窗口大小:
        self.setFixedSize(self.width(), self.height())
        app_path=""
        if getattr(sys,'frozen',False):
            app_path=os.path.dirname(sys.executable) #sys.executable：python.exe所在目录
        else:
            app_path=os.path.abspath('.')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(app_path,"icons/logo.ico"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 1011, 211))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.loginButton = QtGui.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(30, 170, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(210, 120, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 31, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.passwordEdit = QtGui.QLineEdit(self.groupBox)
        self.passwordEdit.setGeometry(QtCore.QRect(70, 110, 113, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 80, 31, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pidcomboBox = QtGui.QComboBox(self.groupBox)
        self.pidcomboBox.setGeometry(QtCore.QRect(270, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.pidcomboBox.setFont(font)
        self.pidcomboBox.setObjectName(_fromUtf8("pidcomboBox"))
        self.okButton = QtGui.QPushButton(self.groupBox)
        self.okButton.setGeometry(QtCore.QRect(410, 170, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.okButton.setFont(font)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.usernameEdit = QtGui.QLineEdit(self.groupBox)
        self.usernameEdit.setGeometry(QtCore.QRect(70, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.sipaddrcomboBox = QtGui.QComboBox(self.groupBox)
        self.sipaddrcomboBox.setGeometry(QtCore.QRect(270, 110, 361, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.sipaddrcomboBox.setFont(font)
        self.sipaddrcomboBox.setObjectName(_fromUtf8("sipaddrcomboBox"))
        self.logoutButton = QtGui.QPushButton(self.groupBox)
        self.logoutButton.setGeometry(QtCore.QRect(140, 170, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName(_fromUtf8("logoutButton"))
        self.publicradioButton = QtGui.QRadioButton(self.groupBox)
        self.publicradioButton.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.publicradioButton.setObjectName(_fromUtf8("publicradioButton"))
        self.netradioButton = QtGui.QRadioButton(self.groupBox)
        self.netradioButton.setGeometry(QtCore.QRect(690, 30, 89, 16))
        self.netradioButton.setObjectName(_fromUtf8("netradioButton"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(710, 60, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(710, 140, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.classcomboBox = QtGui.QComboBox(self.groupBox)
        self.classcomboBox.setGeometry(QtCore.QRect(758, 50, 131, 31))
        self.classcomboBox.setObjectName(_fromUtf8("classcomboBox"))
        self.netloginpushButton = QtGui.QPushButton(self.groupBox)
        self.netloginpushButton.setGeometry(QtCore.QRect(790, 170, 71, 31))
        self.netloginpushButton.setObjectName(_fromUtf8("netloginpushButton"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(710, 100, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.username2lineEdit = QtGui.QLineEdit(self.groupBox)
        self.username2lineEdit.setGeometry(QtCore.QRect(760, 90, 131, 31))
        self.username2lineEdit.setObjectName(_fromUtf8("username2lineEdit"))
        self.searchpushButton = QtGui.QPushButton(self.groupBox)
        self.searchpushButton.setGeometry(QtCore.QRect(914, 130, 51, 31))
        self.searchpushButton.setObjectName(_fromUtf8("searchpushButton"))
        self.ipcomboBox = QtGui.QComboBox(self.groupBox)
        self.ipcomboBox.setGeometry(QtCore.QRect(760, 131, 131, 31))
        self.ipcomboBox.setObjectName(_fromUtf8("ipcomboBox"))
        self.netlogoutpushButton = QtGui.QPushButton(self.groupBox)
        self.netlogoutpushButton.setGeometry(QtCore.QRect(900, 170, 81, 31))
        self.netlogoutpushButton.setObjectName(_fromUtf8("netlogoutpushButton"))
        self.controlgroupBox = QtGui.QGroupBox(self.centralwidget)
        self.controlgroupBox.setGeometry(QtCore.QRect(39, 239, 641, 201))
        self.controlgroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controlgroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.controlgroupBox.setObjectName(_fromUtf8("controlgroupBox"))
        self.loopspinBox = QtGui.QSpinBox(self.controlgroupBox)
        self.loopspinBox.setGeometry(QtCore.QRect(390, 110, 111, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.loopspinBox.setFont(font)
        self.loopspinBox.setMaximum(1000000000)
        self.loopspinBox.setObjectName(_fromUtf8("loopspinBox"))
        self.label_8 = QtGui.QLabel(self.controlgroupBox)
        self.label_8.setGeometry(QtCore.QRect(390, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.loopcheckBox = QtGui.QCheckBox(self.controlgroupBox)
        self.loopcheckBox.setGeometry(QtCore.QRect(390, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.loopcheckBox.setFont(font)
        self.loopcheckBox.setObjectName(_fromUtf8("loopcheckBox"))
        self.clearpushButton = QtGui.QPushButton(self.controlgroupBox)
        self.clearpushButton.setGeometry(QtCore.QRect(90, 10, 61, 30))
        self.clearpushButton.setObjectName(_fromUtf8("clearpushButton"))
        self.sendButton = QtGui.QPushButton(self.controlgroupBox)
        self.sendButton.setGeometry(QtCore.QRect(380, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.sendtextEdit = QtGui.QTextEdit(self.controlgroupBox)
        self.sendtextEdit.setGeometry(QtCore.QRect(10, 51, 361, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.sendtextEdit.setFont(font)
        self.sendtextEdit.setObjectName(_fromUtf8("sendtextEdit"))
        self.label_9 = QtGui.QLabel(self.controlgroupBox)
        self.label_9.setGeometry(QtCore.QRect(540, 50, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.countslineEdit = QtGui.QLineEdit(self.controlgroupBox)
        self.countslineEdit.setGeometry(QtCore.QRect(540, 70, 81, 31))
        self.countslineEdit.setObjectName(_fromUtf8("countslineEdit"))
        self.cmdstoppushButton = QtGui.QPushButton(self.controlgroupBox)
        self.cmdstoppushButton.setGeometry(QtCore.QRect(450, 159, 61, 31))
        self.cmdstoppushButton.setObjectName(_fromUtf8("cmdstoppushButton"))
        self.controlstoppushButton = QtGui.QPushButton(self.controlgroupBox)
        self.controlstoppushButton.setGeometry(QtCore.QRect(180, 10, 61, 31))
        self.controlstoppushButton.setObjectName(_fromUtf8("controlstoppushButton"))
        self.displaygroupBox = QtGui.QGroupBox(self.centralwidget)
        self.displaygroupBox.setGeometry(QtCore.QRect(730, 240, 321, 201))
        self.displaygroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.displaygroupBox.setObjectName(_fromUtf8("displaygroupBox"))
        self.label_12 = QtGui.QLabel(self.displaygroupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.combstextBrowser = QtGui.QTextBrowser(self.displaygroupBox)
        self.combstextBrowser.setGeometry(QtCore.QRect(10, 50, 121, 141))
        self.combstextBrowser.setObjectName(_fromUtf8("combstextBrowser"))
        self.label_11 = QtGui.QLabel(self.displaygroupBox)
        self.label_11.setGeometry(QtCore.QRect(140, 30, 31, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.devlisttextBrowser = QtGui.QTextBrowser(self.displaygroupBox)
        self.devlisttextBrowser.setGeometry(QtCore.QRect(140, 50, 171, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.devlisttextBrowser.setFont(font)
        self.devlisttextBrowser.setObjectName(_fromUtf8("devlisttextBrowser"))
        self.freshpushButton = QtGui.QPushButton(self.displaygroupBox)
        self.freshpushButton.setGeometry(QtCore.QRect(230, 10, 71, 30))
        self.freshpushButton.setObjectName(_fromUtf8("freshpushButton"))
        self.logcatgroupBox = QtGui.QGroupBox(self.centralwidget)
        self.logcatgroupBox.setGeometry(QtCore.QRect(40, 450, 1011, 221))
        self.logcatgroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logcatgroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.logcatgroupBox.setObjectName(_fromUtf8("logcatgroupBox"))
        self.logcattextBrowser = QtGui.QTextBrowser(self.logcatgroupBox)
        self.logcattextBrowser.setGeometry(QtCore.QRect(80, 20, 921, 191))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.logcattextBrowser.setFont(font)
        self.logcattextBrowser.setAutoFillBackground(False)
        self.logcattextBrowser.setObjectName(_fromUtf8("logcattextBrowser"))
        self.cleartextBrowsepushButton = QtGui.QPushButton(self.logcatgroupBox)
        self.cleartextBrowsepushButton.setGeometry(QtCore.QRect(10, 40, 61, 31))
        self.cleartextBrowsepushButton.setObjectName(_fromUtf8("cleartextBrowsepushButton"))
        self.gundongpushButton = QtGui.QPushButton(self.logcatgroupBox)
        self.gundongpushButton.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.gundongpushButton.setObjectName(_fromUtf8("gundongpushButton"))
        self.logcatstoppushButton = QtGui.QPushButton(self.logcatgroupBox)
        self.logcatstoppushButton.setGeometry(QtCore.QRect(10, 140, 61, 31))
        self.logcatstoppushButton.setObjectName(_fromUtf8("logcatstoppushButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        # self.statusbar = QtGui.QStatusBar(MainWindow)
        # self.statusbar.setObjectName(_fromUtf8("statusbar"))
        # MainWindow.setStatusBar(self.statusbar)
        # self.menuBar = QtGui.QMenuBar(MainWindow)
        # self.menuBar.setGeometry(QtCore.QRect(0, 0, 1091, 23))
        # self.menuBar.setObjectName(_fromUtf8("menuBar"))
        # MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartHome", None))
        self.groupBox.setTitle(_translate("MainWindow", "选择登录方式", None))
        self.loginButton.setText(_translate("MainWindow", "登录", None))
        self.label_4.setText(_translate("MainWindow", "好友类型", None))
        self.label_5.setText(_translate("MainWindow", "MAC地址", None))
        self.label_2.setText(_translate("MainWindow", "密码", None))
        self.label.setText(_translate("MainWindow", "账号", None))
        self.okButton.setText(_translate("MainWindow", "确认", None))
        self.logoutButton.setText(_translate("MainWindow", "退出登录", None))
        self.publicradioButton.setText(_translate("MainWindow", "公网登录", None))
        self.netradioButton.setText(_translate("MainWindow", "内网登录", None))
        self.label_3.setText(_translate("MainWindow", "类型", None))
        self.label_6.setText(_translate("MainWindow", "IP地址", None))
        self.netloginpushButton.setText(_translate("MainWindow", "登录", None))
        self.label_7.setText(_translate("MainWindow", "账号", None))
        self.searchpushButton.setText(_translate("MainWindow", "搜索", None))
        self.netlogoutpushButton.setText(_translate("MainWindow", "退出登录", None))
        self.controlgroupBox.setTitle(_translate("MainWindow", "控制命令", None))
        self.label_8.setText(_translate("MainWindow", "设置循环次数", None))
        self.loopcheckBox.setText(_translate("MainWindow", "是否循环", None))
        self.clearpushButton.setText(_translate("MainWindow", "清空", None))
        self.sendButton.setText(_translate("MainWindow", "发送", None))
        self.label_9.setText(_translate("MainWindow", "执行次数", None))
        self.cmdstoppushButton.setText(_translate("MainWindow", "暂停", None))
        self.controlstoppushButton.setText(_translate("MainWindow", "停止", None))
        self.displaygroupBox.setTitle(_translate("MainWindow", "设备与场景显示", None))
        self.label_12.setText(_translate("MainWindow", "场景", None))
        self.label_11.setText(_translate("MainWindow", "设备", None))
        self.freshpushButton.setText(_translate("MainWindow", "刷新", None))
        self.logcatgroupBox.setTitle(_translate("MainWindow", "显示信息", None))
        self.cleartextBrowsepushButton.setText(_translate("MainWindow", "清空", None))
        self.gundongpushButton.setText(_translate("MainWindow", "自动滚动", None))
        self.logcatstoppushButton.setText(_translate("MainWindow", "暂停", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())