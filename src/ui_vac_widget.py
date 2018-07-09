# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/vac_widget.ui'
#
# Created: Sun Jul  8 23:09:03 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(352, 164)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusLed_7 = TaurusLed(Form)
        self.taurusLed_7.setObjectName(_fromUtf8("taurusLed_7"))
        self.gridLayout.addWidget(self.taurusLed_7, 1, 7, 1, 1)
        self.taurusLed = TaurusLed(Form)
        self.taurusLed.setObjectName(_fromUtf8("taurusLed"))
        self.gridLayout.addWidget(self.taurusLed, 1, 1, 1, 1)
        self.taurusLed_8 = TaurusLed(Form)
        self.taurusLed_8.setObjectName(_fromUtf8("taurusLed_8"))
        self.gridLayout.addWidget(self.taurusLed_8, 1, 8, 1, 1)
        self.taurusLed_5 = TaurusLed(Form)
        self.taurusLed_5.setObjectName(_fromUtf8("taurusLed_5"))
        self.gridLayout.addWidget(self.taurusLed_5, 1, 5, 1, 1)
        self.taurusLed_6 = TaurusLed(Form)
        self.taurusLed_6.setObjectName(_fromUtf8("taurusLed_6"))
        self.gridLayout.addWidget(self.taurusLed_6, 1, 6, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.taurusLed_4 = TaurusLed(Form)
        self.taurusLed_4.setObjectName(_fromUtf8("taurusLed_4"))
        self.gridLayout.addWidget(self.taurusLed_4, 1, 4, 1, 1)
        self.taurusLed_2 = TaurusLed(Form)
        self.taurusLed_2.setObjectName(_fromUtf8("taurusLed_2"))
        self.gridLayout.addWidget(self.taurusLed_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.taurusLed_3 = TaurusLed(Form)
        self.taurusLed_3.setObjectName(_fromUtf8("taurusLed_3"))
        self.gridLayout.addWidget(self.taurusLed_3, 1, 3, 1, 1)
        self.taurusLed_9 = TaurusLed(Form)
        self.taurusLed_9.setObjectName(_fromUtf8("taurusLed_9"))
        self.gridLayout.addWidget(self.taurusLed_9, 1, 9, 1, 1)
        self.taurusLed_10 = TaurusLed(Form)
        self.taurusLed_10.setObjectName(_fromUtf8("taurusLed_10"))
        self.gridLayout.addWidget(self.taurusLed_10, 2, 1, 1, 1)
        self.taurusLed_11 = TaurusLed(Form)
        self.taurusLed_11.setObjectName(_fromUtf8("taurusLed_11"))
        self.gridLayout.addWidget(self.taurusLed_11, 2, 2, 1, 1)
        self.taurusLed_12 = TaurusLed(Form)
        self.taurusLed_12.setObjectName(_fromUtf8("taurusLed_12"))
        self.gridLayout.addWidget(self.taurusLed_12, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Linac", None))
        self.label.setText(_translate("Form", "VAC", None))
        self.label_3.setText(_translate("Form", "Ring", None))
        self.pushButton.setText(_translate("Form", "Close", None))

from taurus.qt.qtgui.display import TaurusLed
