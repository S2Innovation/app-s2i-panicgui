# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mag_widget.ui'
#
# Created: Sun Jul  8 23:08:05 2018
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
        Form.resize(381, 190)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusLed = TaurusLed(Form)
        self.taurusLed.setObjectName(_fromUtf8("taurusLed"))
        self.gridLayout.addWidget(self.taurusLed, 1, 1, 1, 1)
        self.taurusLed_5 = TaurusLed(Form)
        self.taurusLed_5.setObjectName(_fromUtf8("taurusLed_5"))
        self.gridLayout.addWidget(self.taurusLed_5, 1, 5, 1, 1)
        self.taurusLed_3 = TaurusLed(Form)
        self.taurusLed_3.setObjectName(_fromUtf8("taurusLed_3"))
        self.gridLayout.addWidget(self.taurusLed_3, 1, 3, 1, 1)
        self.taurusLed_4 = TaurusLed(Form)
        self.taurusLed_4.setObjectName(_fromUtf8("taurusLed_4"))
        self.gridLayout.addWidget(self.taurusLed_4, 1, 4, 1, 1)
        self.taurusLed_2 = TaurusLed(Form)
        self.taurusLed_2.setObjectName(_fromUtf8("taurusLed_2"))
        self.gridLayout.addWidget(self.taurusLed_2, 1, 2, 1, 1)
        self.taurusLed_6 = TaurusLed(Form)
        self.taurusLed_6.setObjectName(_fromUtf8("taurusLed_6"))
        self.gridLayout.addWidget(self.taurusLed_6, 1, 6, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setFrameShape(QtGui.QFrame.Panel)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.taurusLed_7 = TaurusLed(Form)
        self.taurusLed_7.setObjectName(_fromUtf8("taurusLed_7"))
        self.gridLayout.addWidget(self.taurusLed_7, 1, 7, 1, 1)
        self.taurusLed_8 = TaurusLed(Form)
        self.taurusLed_8.setObjectName(_fromUtf8("taurusLed_8"))
        self.gridLayout.addWidget(self.taurusLed_8, 1, 8, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.taurusLed_9 = TaurusLed(Form)
        self.taurusLed_9.setObjectName(_fromUtf8("taurusLed_9"))
        self.gridLayout.addWidget(self.taurusLed_9, 1, 9, 1, 1)
        self.taurusLed_10 = TaurusLed(Form)
        self.taurusLed_10.setObjectName(_fromUtf8("taurusLed_10"))
        self.gridLayout.addWidget(self.taurusLed_10, 1, 10, 1, 1)
        self.taurusLed_11 = TaurusLed(Form)
        self.taurusLed_11.setObjectName(_fromUtf8("taurusLed_11"))
        self.gridLayout.addWidget(self.taurusLed_11, 2, 1, 1, 1)
        self.taurusLed_12 = TaurusLed(Form)
        self.taurusLed_12.setObjectName(_fromUtf8("taurusLed_12"))
        self.gridLayout.addWidget(self.taurusLed_12, 2, 2, 1, 1)
        self.taurusLed_13 = TaurusLed(Form)
        self.taurusLed_13.setObjectName(_fromUtf8("taurusLed_13"))
        self.gridLayout.addWidget(self.taurusLed_13, 2, 3, 1, 1)
        self.taurusLed_14 = TaurusLed(Form)
        self.taurusLed_14.setObjectName(_fromUtf8("taurusLed_14"))
        self.gridLayout.addWidget(self.taurusLed_14, 2, 4, 1, 1)
        self.taurusLed_15 = TaurusLed(Form)
        self.taurusLed_15.setObjectName(_fromUtf8("taurusLed_15"))
        self.gridLayout.addWidget(self.taurusLed_15, 2, 5, 1, 1)
        self.taurusLed_16 = TaurusLed(Form)
        self.taurusLed_16.setObjectName(_fromUtf8("taurusLed_16"))
        self.gridLayout.addWidget(self.taurusLed_16, 2, 6, 1, 1)
        self.taurusLed_17 = TaurusLed(Form)
        self.taurusLed_17.setObjectName(_fromUtf8("taurusLed_17"))
        self.gridLayout.addWidget(self.taurusLed_17, 2, 7, 1, 1)
        self.taurusLed_18 = TaurusLed(Form)
        self.taurusLed_18.setObjectName(_fromUtf8("taurusLed_18"))
        self.gridLayout.addWidget(self.taurusLed_18, 2, 8, 1, 1)
        self.taurusLed_19 = TaurusLed(Form)
        self.taurusLed_19.setObjectName(_fromUtf8("taurusLed_19"))
        self.gridLayout.addWidget(self.taurusLed_19, 2, 9, 1, 1)
        self.taurusLed_20 = TaurusLed(Form)
        self.taurusLed_20.setObjectName(_fromUtf8("taurusLed_20"))
        self.gridLayout.addWidget(self.taurusLed_20, 2, 10, 1, 1)
        self.taurusLed_21 = TaurusLed(Form)
        self.taurusLed_21.setObjectName(_fromUtf8("taurusLed_21"))
        self.gridLayout.addWidget(self.taurusLed_21, 3, 1, 1, 1)
        self.taurusLed_22 = TaurusLed(Form)
        self.taurusLed_22.setObjectName(_fromUtf8("taurusLed_22"))
        self.gridLayout.addWidget(self.taurusLed_22, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "MAG", None))
        self.label_3.setText(_translate("Form", "Ring", None))
        self.pushButton.setText(_translate("Form", "Close", None))

from taurus.qt.qtgui.display import TaurusLed
