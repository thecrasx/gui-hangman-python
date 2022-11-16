# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 573)
        MainWindow.setMinimumSize(QSize(607, 573))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #2A2C32;\n"
"color: #999999")
        self.centralWidgetVLayout = QVBoxLayout(self.centralwidget)
        self.centralWidgetVLayout.setSpacing(0)
        self.centralWidgetVLayout.setObjectName(u"centralWidgetVLayout")
        self.centralWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout = QVBoxLayout(self.startPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gameLabel = QLabel(self.startPage)
        self.gameLabel.setObjectName(u"gameLabel")
        font = QFont()
        font.setPointSize(72)
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet(u"QLabel {\n"
"	color: #999999;\n"
"	padding-top: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.gameLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.buttonsContainer = QFrame(self.startPage)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.buttonsContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startBtn = QPushButton(self.buttonsContainer)
        self.startBtn.setObjectName(u"startBtn")
        font1 = QFont()
        font1.setPointSize(14)
        self.startBtn.setFont(font1)
        self.startBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #383A42;\n"
"	color: #999999;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 10px;\n"
"	padding: 10px 20px 10px 20px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #474953\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border: 3px solid #2A2C32\n"
"}")

        self.verticalLayout_2.addWidget(self.startBtn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.buttonsContainer, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.startPage)
        self.gamePage = QWidget()
        self.gamePage.setObjectName(u"gamePage")
        self.verticalLayout_4 = QVBoxLayout(self.gamePage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.hangmanContainer = QFrame(self.gamePage)
        self.hangmanContainer.setObjectName(u"hangmanContainer")
        self.hangmanContainer.setFrameShape(QFrame.StyledPanel)
        self.hangmanContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.hangmanContainer)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.counterLabel = QLabel(self.hangmanContainer)
        self.counterLabel.setObjectName(u"counterLabel")
        font2 = QFont()
        font2.setPointSize(20)
        self.counterLabel.setFont(font2)

        self.verticalLayout_3.addWidget(self.counterLabel, 0, Qt.AlignHCenter)

        self.hangmanLabel = QLabel(self.hangmanContainer)
        self.hangmanLabel.setObjectName(u"hangmanLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hangmanLabel.sizePolicy().hasHeightForWidth())
        self.hangmanLabel.setSizePolicy(sizePolicy)
        self.hangmanLabel.setPixmap(QPixmap(u"assets/Stage 1.png"))

        self.verticalLayout_3.addWidget(self.hangmanLabel, 0, Qt.AlignHCenter)

        self.wordLabel = QLabel(self.hangmanContainer)
        self.wordLabel.setObjectName(u"wordLabel")
        font3 = QFont()
        font3.setPointSize(28)
        self.wordLabel.setFont(font3)

        self.verticalLayout_3.addWidget(self.wordLabel)


        self.verticalLayout_4.addWidget(self.hangmanContainer, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.gamePage)
        self.finalPage = QWidget()
        self.finalPage.setObjectName(u"finalPage")
        self.verticalLayout_6 = QVBoxLayout(self.finalPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.resultLabel = QLabel(self.finalPage)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet(u"QLabel {\n"
"	color: #999999;\n"
"	padding-top: 20px;\n"
"}")

        self.verticalLayout_6.addWidget(self.resultLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.buttonsContainer_2 = QFrame(self.finalPage)
        self.buttonsContainer_2.setObjectName(u"buttonsContainer_2")
        self.buttonsContainer_2.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.buttonsContainer_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.playAgainBtn = QPushButton(self.buttonsContainer_2)
        self.playAgainBtn.setObjectName(u"playAgainBtn")
        self.playAgainBtn.setFont(font1)
        self.playAgainBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.playAgainBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #383A42;\n"
"	color: #999999;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 10px;\n"
"	padding: 10px 20px 10px 20px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #474953\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	border: 3px solid #2A2C32\n"
"}")

        self.verticalLayout_5.addWidget(self.playAgainBtn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.buttonsContainer_2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.finalPage)

        self.centralWidgetVLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gameLabel.setText(QCoreApplication.translate("MainWindow", u"Hangman", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.counterLabel.setText(QCoreApplication.translate("MainWindow", u"0/3", None))
        self.hangmanLabel.setText("")
        self.wordLabel.setText("")
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Win", None))
        self.playAgainBtn.setText(QCoreApplication.translate("MainWindow", u"Play Again", None))
    # retranslateUi

