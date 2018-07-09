# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

from taurus.qt.qtgui.display import TaurusLed

from ui_ctl_widget import Ui_Form as ctl_ui
from ui_dia_widget import Ui_Form as dia_ui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1394, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusLed_DL = TaurusLed(self.centralwidget)
        self.taurusLed_DL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_DL.setMouseTracking(True)
        self.taurusLed_DL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_DL.setObjectName(_fromUtf8("taurusLed_DL"))
        self.gridLayout.addWidget(self.taurusLed_DL, 2, 1, 1, 1)
        self.label_Linac = QtGui.QLabel(self.centralwidget)
        self.label_Linac.setMaximumSize(QtCore.QSize(100, 50))
        self.label_Linac.setFrameShape(QtGui.QFrame.Panel)
        self.label_Linac.setObjectName(_fromUtf8("label_Linac"))
        self.gridLayout.addWidget(self.label_Linac, 2, 0, 1, 1)
        self.taurusLed_ML = TaurusLed(self.centralwidget)
        self.taurusLed_ML.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_ML.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_ML.setObjectName(_fromUtf8("taurusLed_ML"))
        self.gridLayout.addWidget(self.taurusLed_ML, 2, 2, 1, 1)
        self.taurusLed_CL = TaurusLed(self.centralwidget)
        self.taurusLed_CL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_CL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_CL.setObjectName(_fromUtf8("taurusLed_CL"))
        self.gridLayout.addWidget(self.taurusLed_CL, 2, 8, 1, 1)
        self.label_DIA = QtGui.QLabel(self.centralwidget)
        self.label_DIA.setFrameShape(QtGui.QFrame.Panel)
        self.label_DIA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DIA.setObjectName(_fromUtf8("label_DIA"))
        self.gridLayout.addWidget(self.label_DIA, 0, 1, 1, 1)
        self.taurusLed_DR = TaurusLed(self.centralwidget)
        self.taurusLed_DR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_DR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_DR.setObjectName(_fromUtf8("taurusLed_DR"))
        self.gridLayout.addWidget(self.taurusLed_DR, 3, 1, 1, 1)
        self.taurusLed_RFL = TaurusLed(self.centralwidget)
        self.taurusLed_RFL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_RFL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_RFL.setObjectName(_fromUtf8("taurusLed_RFL"))
        self.gridLayout.addWidget(self.taurusLed_RFL, 2, 4, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(100, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_MAG = QtGui.QLabel(self.centralwidget)
        self.label_MAG.setFrameShape(QtGui.QFrame.Panel)
        self.label_MAG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MAG.setObjectName(_fromUtf8("label_MAG"))
        self.gridLayout.addWidget(self.label_MAG, 0, 2, 1, 1)
        self.label_RF = QtGui.QLabel(self.centralwidget)
        self.label_RF.setFrameShape(QtGui.QFrame.Panel)
        self.label_RF.setAlignment(QtCore.Qt.AlignCenter)
        self.label_RF.setObjectName(_fromUtf8("label_RF"))
        self.gridLayout.addWidget(self.label_RF, 0, 4, 1, 1)
        self.taurusLed_I_VAC_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_I_VAC_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_VAC_PYALARM02.setObjectName(_fromUtf8("taurusLed_I_VAC_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_I_VAC_PYALARM02, 7, 5, 1, 1)
        self.taurusLed_R1_RAD_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_RAD_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_RAD_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_RAD_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_RAD_PYALARM02, 9, 7, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 8, 5, 1, 1)
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 10, 7, 1, 1)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 10, 8, 1, 1)
        self.label_PSS = QtGui.QLabel(self.centralwidget)
        self.label_PSS.setFrameShape(QtGui.QFrame.Panel)
        self.label_PSS.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PSS.setObjectName(_fromUtf8("label_PSS"))
        self.gridLayout.addWidget(self.label_PSS, 0, 3, 1, 1)
        self.label_VAC = QtGui.QLabel(self.centralwidget)
        self.label_VAC.setFrameShape(QtGui.QFrame.Panel)
        self.label_VAC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VAC.setObjectName(_fromUtf8("label_VAC"))
        self.gridLayout.addWidget(self.label_VAC, 0, 5, 1, 1)
        self.label_Ring = QtGui.QLabel(self.centralwidget)
        self.label_Ring.setMaximumSize(QtCore.QSize(100, 50))
        self.label_Ring.setFrameShape(QtGui.QFrame.Panel)
        self.label_Ring.setObjectName(_fromUtf8("label_Ring"))
        self.gridLayout.addWidget(self.label_Ring, 3, 0, 1, 1)
        self.taurusLed_WL = TaurusLed(self.centralwidget)
        self.taurusLed_WL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_WL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_WL.setObjectName(_fromUtf8("taurusLed_WL"))
        self.gridLayout.addWidget(self.taurusLed_WL, 2, 6, 1, 1)
        self.taurusLed_VL = TaurusLed(self.centralwidget)
        self.taurusLed_VL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_VL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_VL.setObjectName(_fromUtf8("taurusLed_VL"))
        self.gridLayout.addWidget(self.taurusLed_VL, 2, 5, 1, 1)
        self.taurusLed_RE = TaurusLed(self.centralwidget)
        self.taurusLed_RE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_RE.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_RE.setObjectName(_fromUtf8("taurusLed_RE"))
        self.gridLayout.addWidget(self.taurusLed_RE, 3, 7, 1, 1)
        self.taurusLed_PL = TaurusLed(self.centralwidget)
        self.taurusLed_PL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_PL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_PL.setObjectName(_fromUtf8("taurusLed_PL"))
        self.gridLayout.addWidget(self.taurusLed_PL, 2, 3, 1, 1)
        self.taurusLed_CR = TaurusLed(self.centralwidget)
        self.taurusLed_CR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_CR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_CR.setObjectName(_fromUtf8("taurusLed_CR"))
        self.gridLayout.addWidget(self.taurusLed_CR, 3, 8, 1, 1)
        self.label_WAT = QtGui.QLabel(self.centralwidget)
        self.label_WAT.setFrameShape(QtGui.QFrame.Panel)
        self.label_WAT.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WAT.setObjectName(_fromUtf8("label_WAT"))
        self.gridLayout.addWidget(self.label_WAT, 0, 6, 1, 1)
        self.label_CTL = QtGui.QLabel(self.centralwidget)
        self.label_CTL.setFrameShape(QtGui.QFrame.Panel)
        self.label_CTL.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CTL.setObjectName(_fromUtf8("label_CTL"))
        self.gridLayout.addWidget(self.label_CTL, 0, 8, 1, 1)
        self.label_RAD = QtGui.QLabel(self.centralwidget)
        self.label_RAD.setFrameShape(QtGui.QFrame.Panel)
        self.label_RAD.setAlignment(QtCore.Qt.AlignCenter)
        self.label_RAD.setObjectName(_fromUtf8("label_RAD"))
        self.gridLayout.addWidget(self.label_RAD, 0, 7, 1, 1)
        self.taurusLed_R1_RF_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_RF_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_RF_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_RF_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_RF_PYALARM02, 9, 4, 1, 1)
        self.taurusLed_MR = TaurusLed(self.centralwidget)
        self.taurusLed_MR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_MR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_MR.setObjectName(_fromUtf8("taurusLed_MR"))
        self.gridLayout.addWidget(self.taurusLed_MR, 3, 2, 1, 1)
        self.taurusLed_PR = TaurusLed(self.centralwidget)
        self.taurusLed_PR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_PR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_PR.setObjectName(_fromUtf8("taurusLed_PR"))
        self.gridLayout.addWidget(self.taurusLed_PR, 3, 3, 1, 1)
        self.taurusLed_RFR = TaurusLed(self.centralwidget)
        self.taurusLed_RFR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_RFR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_RFR.setObjectName(_fromUtf8("taurusLed_RFR"))
        self.gridLayout.addWidget(self.taurusLed_RFR, 3, 4, 1, 1)
        self.taurusLed_VR = TaurusLed(self.centralwidget)
        self.taurusLed_VR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_VR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_VR.setObjectName(_fromUtf8("taurusLed_VR"))
        self.gridLayout.addWidget(self.taurusLed_VR, 3, 5, 1, 1)
        self.taurusLed_WR = TaurusLed(self.centralwidget)
        self.taurusLed_WR.setEnabled(False)
        self.taurusLed_WR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_WR.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_WR.setLedInverted(False)
        self.taurusLed_WR.setModel(_fromUtf8(""))
        self.taurusLed_WR.setObjectName(_fromUtf8("taurusLed_WR"))
        self.gridLayout.addWidget(self.taurusLed_WR, 3, 6, 1, 1)
        self.taurusLed_RL = TaurusLed(self.centralwidget)
        self.taurusLed_RL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taurusLed_RL.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_RL.setObjectName(_fromUtf8("taurusLed_RL"))
        self.gridLayout.addWidget(self.taurusLed_RL, 2, 7, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 8, 1, 1)
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 10, 5, 1, 1)
        self.taurusLed_R1_PSS_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_PSS_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_PSS_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_PSS_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_PSS_PYALARM02, 9, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setFrameShape(QtGui.QFrame.Box)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 10, 6, 1, 1)
        self.taurusLed_R1_PLC_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_PLC_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_PLC_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_PLC_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_PLC_PYALARM02, 9, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.taurusLed_R1_MAG_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_MAG_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_MAG_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_MAG_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_MAG_PYALARM02, 9, 2, 1, 1)
        self.taurusLed_I_DIA_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_DIA_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_DIA_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_DIA_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_DIA_PYALARM01, 5, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 10, 3, 1, 1)
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 10, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 10, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 12, 5, 1, 1)
        self.taurusLed_R1_CTL_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_CTL_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_CTL_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_CTL_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_CTL_PYALARM02, 9, 8, 1, 1)
        self.taurusLed_I_PSS_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_PSS_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_PSS_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_PSS_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_PSS_PYALARM01, 5, 3, 1, 1)
        self.taurusLed_I_MAG_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_MAG_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_MAG_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_MAG_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_MAG_PYALARM01, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 12, 2, 1, 1)
        self.taurusLed_R1_VAC_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_VAC_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_VAC_PYALARM01.setObjectName(_fromUtf8("taurusLed_R1_VAC_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_R1_VAC_PYALARM01, 9, 5, 1, 1)
        self.taurusLed_I_VAC_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_VAC_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_VAC_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_VAC_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_VAC_PYALARM01, 5, 5, 1, 1)
        self.taurusLed_I_RF_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_RF_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_RF_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_RF_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_RF_PYALARM01, 5, 4, 1, 1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 10, 1, 1, 1)
        self.taurusLed_R1_MAG_PYALARM03 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_MAG_PYALARM03.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_MAG_PYALARM03.setObjectName(_fromUtf8("taurusLed_R1_MAG_PYALARM03"))
        self.gridLayout.addWidget(self.taurusLed_R1_MAG_PYALARM03, 11, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 6, 6, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 6, 7, 1, 1)
        self.taurusLed_R1_DIA_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_DIA_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_DIA_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_DIA_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_DIA_PYALARM02, 9, 1, 1, 1)
        self.taurusLed_I_CTL_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_CTL_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_CTL_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_CTL_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_CTL_PYALARM01, 5, 8, 1, 1)
        self.taurusLed_I_RAD_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_RAD_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_RAD_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_RAD_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_RAD_PYALARM01, 5, 7, 1, 1)
        self.taurusLed_I_PLC_PYALARM01 = TaurusLed(self.centralwidget)
        self.taurusLed_I_PLC_PYALARM01.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_I_PLC_PYALARM01.setObjectName(_fromUtf8("taurusLed_I_PLC_PYALARM01"))
        self.gridLayout.addWidget(self.taurusLed_I_PLC_PYALARM01, 5, 6, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 4, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.taurusLed_R1_VAC_PYALARM02 = TaurusLed(self.centralwidget)
        self.taurusLed_R1_VAC_PYALARM02.setAlignment(QtCore.Qt.AlignCenter)
        self.taurusLed_R1_VAC_PYALARM02.setObjectName(_fromUtf8("taurusLed_R1_VAC_PYALARM02"))
        self.gridLayout.addWidget(self.taurusLed_R1_VAC_PYALARM02, 11, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 9, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 9, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 9, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 9, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 9, 9, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 11, 9, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 9, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 4, 3, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 4, 4, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 4, 5, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 4, 6, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 4, 7, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 4, 8, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem7 = QtGui.QSpacerItem(20, 143, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1394, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAlarmGui = QtGui.QMenu(self.menubar)
        self.menuAlarmGui.setObjectName(_fromUtf8("menuAlarmGui"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPanic = QtGui.QAction(MainWindow)
        self.actionPanic.setObjectName(_fromUtf8("actionPanic"))
        self.actionWebPanicGui = QtGui.QAction(MainWindow)
        self.actionWebPanicGui.setObjectName(_fromUtf8("actionWebPanicGui"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuAlarmGui.addAction(self.actionPanic)
        self.menuAlarmGui.addAction(self.actionWebPanicGui)
        self.menuAlarmGui.addAction(self.actionClose)
        self.menubar.addAction(self.menuAlarmGui.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.hide)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_Linac.setText(_translate("MainWindow", "Linac", None))
        self.label_DIA.setText(_translate("MainWindow", "DIA", None))
        self.label.setText(_translate("MainWindow", "SubSytem:", None))
        self.label_MAG.setText(_translate("MainWindow", "MAG", None))
        self.label_RF.setText(_translate("MainWindow", "RF", None))
        self.label_13.setText(_translate("MainWindow", "I_VAC_PYALARM02", None))
        self.label_20.setText(_translate("MainWindow", "R1_RAD_PYALARM02", None))
        self.label_21.setText(_translate("MainWindow", "R1_CTL_PYALARM02", None))
        self.label_PSS.setText(_translate("MainWindow", "PSS", None))
        self.label_VAC.setText(_translate("MainWindow", "VAC", None))
        self.label_Ring.setText(_translate("MainWindow", "Ring", None))
        self.label_WAT.setText(_translate("MainWindow", "WAT", None))
        self.label_CTL.setText(_translate("MainWindow", "CTL", None))
        self.label_RAD.setText(_translate("MainWindow", "RAD", None))
        self.taurusLed_WR.setOnColor(_translate("MainWindow", "red", None))
        self.taurusLed_WR.setOffColor(_translate("MainWindow", "green", None))
        self.label_7.setText(_translate("MainWindow", "I_PSS_PYALARM01", None))
        self.label_12.setText(_translate("MainWindow", "I_CTL_PYALARM01", None))
        self.label_18.setText(_translate("MainWindow", "R1_VAC_PYALARM01", None))
        self.label_4.setText(_translate("MainWindow", "Ring DSs", None))
        self.label_19.setText(_translate("MainWindow", "R1_PLC_PYALARM02", None))
        self.label_3.setText(_translate("MainWindow", "Linac DSs", None))
        self.label_16.setText(_translate("MainWindow", "R1_PSS_PYALARM02", None))
        self.label_17.setText(_translate("MainWindow", "R1_RF_PYALARM02", None))
        self.label_14.setText(_translate("MainWindow", "R1_MAG_PYALARM02", None))
        self.label_23.setText(_translate("MainWindow", "R1_VAC_PYALARM02", None))
        self.label_2.setText(_translate("MainWindow", "Alarms:", None))
        self.label_24.setText(_translate("MainWindow", "R1_MAG_PYALARM03", None))
        self.label_15.setText(_translate("MainWindow", "R1_DIA_PYALARM02", None))
        self.label_10.setText(_translate("MainWindow", "I_PLC_PYALARM01", None))
        self.label_11.setText(_translate("MainWindow", "I_RAD_PYALARM01", None))
        self.label_8.setText(_translate("MainWindow", "I_RF_PYALARM01", None))
        self.label_9.setText(_translate("MainWindow", "I_VAC_PYALARM01", None))
        self.label_5.setText(_translate("MainWindow", "I_DIA_PYALARM01", None))
        self.label_6.setText(_translate("MainWindow", "I_MAG_PYALARM01", None))
        self.pushButton_3.setText(_translate("MainWindow", "DIA", None))
        self.pushButton_4.setText(_translate("MainWindow", "MAG", None))
        self.pushButton_5.setText(_translate("MainWindow", "PSS", None))
        self.pushButton_6.setText(_translate("MainWindow", "RF", None))
        self.pushButton_7.setText(_translate("MainWindow", "VAC", None))
        self.pushButton_8.setText(_translate("MainWindow", "WAT", None))
        self.pushButton_9.setText(_translate("MainWindow", "RAD", None))
        self.pushButton_10.setText(_translate("MainWindow", "CTL", None))
        self.pushButton.setText(_translate("MainWindow", "Close", None))
        self.pushButton_2.setText(_translate("MainWindow", "Panic", None))
        self.menuAlarmGui.setTitle(_translate("MainWindow", "More", None))
        self.actionPanic.setText(_translate("MainWindow", "Panic", None))
        self.actionWebPanicGui.setText(_translate("MainWindow", "WebPanicGui", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))

        self.taurusLed_I_CTL_PYALARM01.setModel('sys/tg_test/1')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

