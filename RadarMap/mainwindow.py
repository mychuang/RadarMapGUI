#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:53:58 2021

@author: miller
"""

from PyQt5.QtCore import QObject, qDebug, pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import  Ui_MainWindow

class MainWindow(QMainWindow, QObject):
    
    # Here define the constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        
        #var setting
        self.__radarList = ["RCCG", "RCKT", "RCHL", "RCWF"]
        
        #ui setting
        self.__iniUI()
        
        #ui connect
        self.__ui.singleRadBtn.clicked.connect(self.__singleRadarModeOn)
        self.__ui.multiRadBtn.clicked.connect(self.__multiRadarModeOn)
        
    
    def __iniUI(self):
        self.__ui.singleRadBtn.setChecked(True)
        for index in range(len(self.__radarList)):
            self.__ui.radComboBox.addItem(self.__radarList[index])

    
    @pyqtSlot()
    def __singleRadarModeOn(self):
        qDebug('MainWindow::singleRadarModeOn')
        self.__ui.radComboBox.setStyleSheet(\
            "background-color: rgb(247, 240, 188);"
			"font: 87 12pt Arial Black;"
			"color: rgb(150, 39, 230)")
        self.__ui.radComboBox.setEnabled(True)
    
    def __multiRadarModeOn(self):
        qDebug('MainWindow::multiRadarModeOn')
        self.__ui.radComboBox.setStyleSheet(\
            "background-color: rgb(189, 189, 189);"
			"font: 87 12pt Arial Black;"
			"color: rgb(255, 255, 255)")
        self.__ui.radComboBox.setEnabled(False)
       
        
        
    
    
        