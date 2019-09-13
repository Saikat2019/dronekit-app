# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import dronekit
import socket
import os
import time

import dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 10, 101, 299))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_connect = QtWidgets.QPushButton(self.layoutWidget)
        self.b_connect.setObjectName("b_connect")
        self.verticalLayout.addWidget(self.b_connect)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.b_arm = QtWidgets.QPushButton(self.layoutWidget)
        self.b_arm.setObjectName("b_arm")
        self.verticalLayout.addWidget(self.b_arm)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.b_disarm = QtWidgets.QPushButton(self.layoutWidget)
        self.b_disarm.setObjectName("b_disarm")
        self.verticalLayout.addWidget(self.b_disarm)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.b_takeoff = QtWidgets.QPushButton(self.layoutWidget)
        self.b_takeoff.setObjectName("b_takeoff")
        self.verticalLayout.addWidget(self.b_takeoff)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.b_fly = QtWidgets.QPushButton(self.layoutWidget)
        self.b_fly.setObjectName("b_fly")
        self.verticalLayout.addWidget(self.b_fly)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.b_rtl = QtWidgets.QPushButton(self.layoutWidget)
        self.b_rtl.setObjectName("b_rtl")
        self.verticalLayout.addWidget(self.b_rtl)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.b_land = QtWidgets.QPushButton(self.layoutWidget)
        self.b_land.setObjectName("b_land")
        self.verticalLayout.addWidget(self.b_land)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGo_to_Map = QtWidgets.QAction(MainWindow)
        self.actionGo_to_Map.setObjectName("actionGo_to_Map")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.b_arm, self.b_disarm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_connect.setText(_translate("MainWindow", "Connect"))
        self.b_arm.setText(_translate("MainWindow", "Arm"))
        self.b_disarm.setText(_translate("MainWindow", "Dis Arm"))
        self.b_takeoff.setText(_translate("MainWindow", "Take Off"))
        self.b_fly.setText(_translate("MainWindow", "GoTo"))
        self.b_rtl.setText(_translate("MainWindow", "RTL"))
        self.b_land.setText(_translate("MainWindow", "Land"))
        self.actionGo_to_Map.setText(_translate("MainWindow", "Go to Map"))

        self.b_connect.clicked.connect(self.conn)
        self.b_arm.clicked.connect(self.arm)
        self.b_disarm.clicked.connect(self.disarm)
        self.b_rtl.clicked.connect(self.rtl)
        self.b_takeoff.clicked.connect(self.takeoff)
        self.b_land.clicked.connect(self.land)
        self.b_fly.clicked.connect(self.getFrame)


    def getFrame(self):
        items = ("Global Frame", "Local Frame","Alt in local frame")

        item, ok = QInputDialog.getItem(self.centralwidget, "Frame", 
                                            "Choose Frame", items, 0, False)
            
        if ok and item:
            dialog = dialog.main()


    def arm(self):
        if self.vehicle.is_armable:
            self.vehicle.mode = dronekit.VehicleMode("GUIDED")
            self.vehicle.armed = True
            while not self.vehicle.armed:
                time.sleep(.1)
            print("armed!!")
        else:
            print("Not armmable!!")


    def disarm(self):
        self.vehicle.armed = False
        print("Disarmed!")

    def land(self):
        self.vehicle.mode = dronekit.VehicleMode("LAND")

        while not self.vehicle.location.global_relative_frame.alt==0:
            if self.vehicle.location.global_relative_frame.alt < 2:
                set_velocity_body(vehicle,0,0,0.1)

        self.vehicle.armed = False
        self.vehicle.close()
        print("landed")

    def rtl(self):
        self.vehicle.mode = dronekit.VehicleMode("RTL")
        print("returned to land!!")


    def takeoff(self):
        self.alt = self.getAlt()
        self.vehicle.simple_takeoff(self.alt)
        while True:
            print(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            #Break and return from function just below target altitude.
            if self.vehicle.location.global_relative_frame.alt>=self.alt*0.95:
                print("Took off :p")
                break
            time.sleep(1)


    def getAlt(self):
        text, okPressed = QInputDialog.getText(self.centralwidget, "Altitude","Enter Altitude in metres : ", QLineEdit.Normal, "10")
        if okPressed and text != '':
            return text


    def conn(self):
        self.connStr = self.getItem()
        if self.connStr == "-1":
            pass

        else:
            try:
                self.vehicle = dronekit.connect(self.connStr, heartbeat_timeout=15)
                print("connection setup")

            # Bad TCP connection
            except socket.error:
                print('No server exists!')

            # Bad TTY connection
            except os.error as e:
                print('No serial exists!')

            # API Error
            except dronekit.APIException:
                print('Timeout!')

            # Other error
            except:
                print('Some other error!')

    def getItem(self):
        items = ("udp", "tcp")

        item, ok = QInputDialog.getItem(self.centralwidget, "Type", 
                                            "Connection Type", items, 0, False)
            
        if ok and item:
            s = self.getText(item)
            return s
        else:
            print("cancelled")
            return "-1"



    def getText(self,item):
        text, okPressed = QInputDialog.getText(self.centralwidget, "Connection String","Enter IP:PORT ", QLineEdit.Normal, "IP address : PORT")
        if okPressed and text != '':
            return (str(item) + ':' + str(text))
        else:
            print("cancelled")
            return "-1"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())