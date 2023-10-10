# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YTDownloaderUI-new.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import src.ressource_qrc_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(635, 475)
        Form.setStyleSheet(u"QWidget{\n"
"	border-radius:5pt;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777201))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(60, 0, 10, 0)
        self.logoIcon = QLabel(self.frame_6)
        self.logoIcon.setObjectName(u"logoIcon")
        self.logoIcon.setMinimumSize(QSize(90, 90))
        self.logoIcon.setMaximumSize(QSize(90, 90))
        self.logoIcon.setPixmap(QPixmap(u":/icons/logo-transparent.ico"))
        self.logoIcon.setScaledContents(True)
        self.logoIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.logoIcon)


        self.horizontalLayout.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Xeron"])
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(254, 0, 57);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.versionLabel = QLabel(self.frame_13)
        self.versionLabel.setObjectName(u"versionLabel")
        font1 = QFont()
        font1.setFamilies([u"Nasalization"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.versionLabel.setFont(font1)
        self.versionLabel.setStyleSheet(u"color: rgba(216, 216, 216, 140);")
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.versionLabel, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_13, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignBottom)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    background-color:none;\n"
"    border: .5px solid rgb(254, 0, 57);;  \n"
"    color: rgb(254, 0, 57);\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"padding: 2px 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 1 #C0392B,                              \n"
"    stop: 0 #E74C3C );\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 0, 57);\n"
"    color:white;            \n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: none;\n"
"    border-color: #aaaaaa;\n"
"    color: #666666;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_3)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(25, 25))
        self.minimizeBtn.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.minimizeBtn, 0, Qt.AlignRight|Qt.AlignTop)

        self.quitBtn = QPushButton(self.frame_3)
        self.quitBtn.setObjectName(u"quitBtn")
        self.quitBtn.setMinimumSize(QSize(25, 25))
        self.quitBtn.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.quitBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.quitBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.optionFrame = QFrame(self.frame_4)
        self.optionFrame.setObjectName(u"optionFrame")
        self.optionFrame.setMinimumSize(QSize(180, 0))
        self.optionFrame.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    background-color:none;\n"
"    border: .5px solid rgb(254, 0, 57);;  \n"
"    color: rgb(254, 0, 57);\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 1 #C0392B,                              \n"
"    stop: 0 #E74C3C );\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 0, 57);\n"
"    color:white;            \n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: none;\n"
"    border-color: #aaaaaa;\n"
"    color: #666666;\n"
"}")
        self.optionFrame.setFrameShape(QFrame.StyledPanel)
        self.optionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.optionFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.Options = QLabel(self.optionFrame)
        self.Options.setObjectName(u"Options")
        font2 = QFont()
        font2.setFamilies([u"Xeron"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.Options.setFont(font2)
        self.Options.setStyleSheet(u"color: rgb(254, 0, 57);\n"
"font: 18pt \"Xeron\";")

        self.verticalLayout_5.addWidget(self.Options, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_9 = QFrame(self.optionFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.savePathLabel = QLabel(self.frame_9)
        self.savePathLabel.setObjectName(u"savePathLabel")
        self.savePathLabel.setStyleSheet(u"color:rgb(255, 85, 0);")
        self.savePathLabel.setAlignment(Qt.AlignCenter)
        self.savePathLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.savePathLabel)

        self.changePathBtn = QPushButton(self.frame_9)
        self.changePathBtn.setObjectName(u"changePathBtn")
        sizePolicy1.setHeightForWidth(self.changePathBtn.sizePolicy().hasHeightForWidth())
        self.changePathBtn.setSizePolicy(sizePolicy1)
        self.changePathBtn.setMinimumSize(QSize(120, 0))
        self.changePathBtn.setMaximumSize(QSize(140, 16777215))
        self.changePathBtn.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.changePathBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.openSaveDirBtn = QPushButton(self.frame_9)
        self.openSaveDirBtn.setObjectName(u"openSaveDirBtn")
        self.openSaveDirBtn.setMinimumSize(QSize(120, 0))
        self.openSaveDirBtn.setMaximumSize(QSize(140, 16777215))

        self.verticalLayout_4.addWidget(self.openSaveDirBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_9, 0, Qt.AlignVCenter)

        self.frame_12 = QFrame(self.optionFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(254, 0, 57);\n"
"font: 12pt \"Xeron\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.audioformatBox = QComboBox(self.frame_12)
        self.audioformatBox.setObjectName(u"audioformatBox")
        self.audioformatBox.setEnabled(True)
        self.audioformatBox.setMinimumSize(QSize(119, 0))
        self.audioformatBox.setMaximumSize(QSize(100, 16777215))
        self.audioformatBox.setLayoutDirection(Qt.LeftToRight)
        self.audioformatBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid rgb(254, 0, 57);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"border-color: red;\n"
"text-align:center;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"\n"
"    width: 15px;\n"
"	background-color: rgb(254, 0, 57);\n"
"    border-left-width: 1px;\n"
"    border-left-color:rgb(254, 0, 57);\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"	background-color: white;\n"
"} ")
        self.audioformatBox.setInputMethodHints(Qt.ImhNoEditMenu|Qt.ImhNoTextHandles)
        self.audioformatBox.setEditable(False)
        self.audioformatBox.setInsertPolicy(QComboBox.NoInsert)
        self.audioformatBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_9.addWidget(self.audioformatBox, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignVCenter)

        self.frame_8 = QFrame(self.optionFrame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 2, 4)
        self.downloadProgress = QProgressBar(self.frame_8)
        self.downloadProgress.setObjectName(u"downloadProgress")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.downloadProgress.sizePolicy().hasHeightForWidth())
        self.downloadProgress.setSizePolicy(sizePolicy3)
        self.downloadProgress.setMinimumSize(QSize(180, 0))
        self.downloadProgress.setStyleSheet(u"alternate-background-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);\n"
"selection-color: rgb(255, 0, 0);\n"
"border-radius: 5px;")
        self.downloadProgress.setValue(24)
        self.downloadProgress.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.downloadProgress)

        self.downloadBtn = QPushButton(self.frame_8)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMinimumSize(QSize(120, 0))
        self.downloadBtn.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_7.addWidget(self.downloadBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.optionFrame)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.listWidget = QListWidget(self.frame_5)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setStyleSheet(u"border: 1px solid rgb(254, 0, 57);;\n"
"border-radius: 2px;")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidget.setTextElideMode(Qt.ElideMiddle)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(2)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setItemAlignment(Qt.AlignCenter)
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listWidget)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 2)
        self.urlEdit = QLineEdit(self.frame_7)
        self.urlEdit.setObjectName(u"urlEdit")
        self.urlEdit.setMinimumSize(QSize(132, 25))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.urlEdit.setFont(font3)
        self.urlEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid rgb(254, 0, 57);;\n"
"	border: 1px solid red;\n"
"\n"
"}")
        self.urlEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.urlEdit)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    background-color:none;\n"
"    border: .5px solid rgb(254, 0, 57);;  \n"
"    color: rgb(254, 0, 57);\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 1 #C0392B,                              \n"
"    stop: 0 #E74C3C );\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 0, 57);\n"
"    color:white;            \n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: none;\n"
"    border-color: #aaaaaa;\n"
"    color: #666666;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 2, 2)
        self.removeUrlBtn = QPushButton(self.frame_11)
        self.removeUrlBtn.setObjectName(u"removeUrlBtn")
        self.removeUrlBtn.setMinimumSize(QSize(120, 0))
        self.removeUrlBtn.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.removeUrlBtn)

        self.addUrlBtn = QPushButton(self.frame_11)
        self.addUrlBtn.setObjectName(u"addUrlBtn")
        self.addUrlBtn.setMinimumSize(QSize(120, 0))
        self.addUrlBtn.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.addUrlBtn)


        self.verticalLayout_8.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logoIcon.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Youtube MP3 Downloader", None))
        self.versionLabel.setText(QCoreApplication.translate("Form", u"Version 1.4 \u00a9 S3R43o3 2023", None))
        self.minimizeBtn.setText(QCoreApplication.translate("Form", u"-", None))
        self.quitBtn.setText(QCoreApplication.translate("Form", u"X", None))
        self.Options.setText(QCoreApplication.translate("Form", u"Options", None))
        self.savePathLabel.setText(QCoreApplication.translate("Form", u"Savepath", None))
        self.changePathBtn.setText(QCoreApplication.translate("Form", u"Change Path", None))
        self.openSaveDirBtn.setText(QCoreApplication.translate("Form", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Audio Format", None))
        self.audioformatBox.setPlaceholderText(QCoreApplication.translate("Form", u"Select...", None))
        self.downloadBtn.setText(QCoreApplication.translate("Form", u"Download", None))
        self.urlEdit.setText("")
        self.urlEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter a Youtube URL here...", None))
        self.removeUrlBtn.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.addUrlBtn.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

