# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.flag = False
        self.l_lat = QtWidgets.QLabel(Dialog)
        self.l_lat.setGeometry(QtCore.QRect(20, 10, 67, 17))
        self.l_lat.setObjectName("l_lat")
        self.l_lon = QtWidgets.QLabel(Dialog)
        self.l_lon.setGeometry(QtCore.QRect(150, 10, 71, 17))
        self.l_lon.setObjectName("l_lon")
        self.l_alt = QtWidgets.QLabel(Dialog)
        self.l_alt.setGeometry(QtCore.QRect(280, 10, 111, 20))
        self.l_alt.setObjectName("l_alt")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 40, 381, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t_lat = QtWidgets.QTextEdit(self.widget)
        self.t_lat.setObjectName("t_lat")
        self.horizontalLayout.addWidget(self.t_lat)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.t_lon = QtWidgets.QTextEdit(self.widget)
        self.t_lon.setObjectName("t_lon")
        self.horizontalLayout.addWidget(self.t_lon)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.t_alt = QtWidgets.QPlainTextEdit(self.widget)
        self.t_alt.setObjectName("t_alt")
        self.horizontalLayout.addWidget(self.t_alt)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(180, 150, 192, 29))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.b_fly = QtWidgets.QPushButton(self.widget1)
        self.b_fly.setObjectName("b_fly")
        self.horizontalLayout_2.addWidget(self.b_fly)
        self.l_lat.setBuddy(self.t_lat)
        self.l_lon.setBuddy(self.t_lon)
        self.l_alt.setBuddy(self.t_alt)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_lat.setText(_translate("Dialog", "Latitude"))
        self.l_lon.setText(_translate("Dialog", "Longitude"))
        self.l_alt.setText(_translate("Dialog", "Altitude(mtrs.)"))
        self.b_fly.setText(_translate("Dialog", "Fly!!"))

    def getButt(self):
        return self.b_fly.clicked.connect(self.getCords)

    def getCords(self):
        self.lat = self.t_lat.toPlainText()
        self.lon = self.t_lon.toPlainText()
        self.alt = self.t_alt.toPlainText()
        self.flag = True
        print(self.lat)
        print(self.lon)
        print(self.alt)
        return self.lat,self.lon,self.alt


def main():
    app1 = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    if ui.flag:
        return ui.lat,ui.lon,ui.alt
    sys.exit(app1.exec_())
    

if __name__ == "__main__":
    print(main())
    # app = QtWidgets.QApplication(sys.argv)
    # print(main())
    # k = app.exec_()
    # print("1")
    # sys.exit(k)
