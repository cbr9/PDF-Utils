# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 505)
        MainWindow.setMinimumSize(QtCore.QSize(733, 497))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(-1, 25, -1, 25)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.extractPages = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractPages.sizePolicy().hasHeightForWidth())
        self.extractPages.setSizePolicy(sizePolicy)
        self.extractPages.setMaximumSize(QtCore.QSize(149, 16777215))
        self.extractPages.setBaseSize(QtCore.QSize(200, 0))
        self.extractPages.setObjectName("extractPages")
        self.options = QtWidgets.QButtonGroup(MainWindow)
        self.options.setObjectName("options")
        self.options.addButton(self.extractPages)
        self.gridLayout_4.addWidget(self.extractPages, 1, 0, 1, 1)
        self.rangePages = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangePages.sizePolicy().hasHeightForWidth())
        self.rangePages.setSizePolicy(sizePolicy)
        self.rangePages.setMaximumSize(QtCore.QSize(500, 16777215))
        self.rangePages.setAutoFillBackground(True)
        self.rangePages.setInputMask("")
        self.rangePages.setObjectName("rangePages")
        self.gridLayout_4.addWidget(self.rangePages, 1, 1, 1, 1)
        self.mergeDocs = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergeDocs.sizePolicy().hasHeightForWidth())
        self.mergeDocs.setSizePolicy(sizePolicy)
        self.mergeDocs.setObjectName("mergeDocs")
        self.options.addButton(self.mergeDocs)
        self.gridLayout_4.addWidget(self.mergeDocs, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(21, 26, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputLabel.sizePolicy().hasHeightForWidth())
        self.outputLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setAutoFillBackground(False)
        self.outputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.outputLabel.setScaledContents(True)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setWordWrap(True)
        self.outputLabel.setIndent(0)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_2.addWidget(self.outputLabel)
        self.outputName = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.outputName.setFont(font)
        self.outputName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputName.setAutoFillBackground(True)
        self.outputName.setText("")
        self.outputName.setObjectName("outputName")
        self.verticalLayout_2.addWidget(self.outputName)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK.sizePolicy().hasHeightForWidth())
        self.OK.setSizePolicy(sizePolicy)
        self.OK.setObjectName("OK")
        self.horizontalLayout_5.addWidget(self.OK)
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFile.sizePolicy().hasHeightForWidth())
        self.openFile.setSizePolicy(sizePolicy)
        self.openFile.setObjectName("openFile")
        self.horizontalLayout_5.addWidget(self.openFile)
        self.clearFields = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearFields.sizePolicy().hasHeightForWidth())
        self.clearFields.setSizePolicy(sizePolicy)
        self.clearFields.setObjectName("clearFields")
        self.horizontalLayout_5.addWidget(self.clearFields)
        self.readmeFile = QtWidgets.QPushButton(self.centralwidget)
        self.readmeFile.setObjectName("readmeFile")
        self.horizontalLayout_5.addWidget(self.readmeFile)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, 18, 20, 10)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLabel.sizePolicy().hasHeightForWidth())
        self.inputLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.inputLabel.setFont(font)
        self.inputLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.inputLabel.setLineWidth(0)
        self.inputLabel.setMidLineWidth(0)
        self.inputLabel.setScaledContents(True)
        self.inputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLabel.setWordWrap(True)
        self.inputLabel.setIndent(0)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout_2.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.editListOfDocs = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editListOfDocs.sizePolicy().hasHeightForWidth())
        self.editListOfDocs.setSizePolicy(sizePolicy)
        self.editListOfDocs.setObjectName("editListOfDocs")
        self.gridLayout_2.addWidget(self.editListOfDocs, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.outputLabel.setBuddy(self.outputName)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.extractPages.setText(_translate("MainWindow", "Extract Pages:  "))
        self.rangePages.setPlaceholderText(_translate("MainWindow", "Ex.: 1,2,3-30-2 (pages 1 and 2 and from page 3 to 30 picking out every two pages)"))
        self.mergeDocs.setText(_translate("MainWindow", "Merge"))
        self.outputLabel.setText(_translate("MainWindow", "OUTPUT"))
        self.outputName.setPlaceholderText(_translate("MainWindow", "Select a name for the output file (it must end in \".pdf\")"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.openFile.setText(_translate("MainWindow", "Open File"))
        self.clearFields.setText(_translate("MainWindow", "Clear Fields"))
        self.readmeFile.setText(_translate("MainWindow", "README"))
        self.inputLabel.setText(_translate("MainWindow", "INPUT"))
        self.editListOfDocs.setText(_translate("MainWindow", "Add or Remove Files"))
