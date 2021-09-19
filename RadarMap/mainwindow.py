#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:53:58 2021

@author: miller
"""

import sys
from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import  Ui_MainWindow

class MainWindow(QMainWindow):
    # Here define the constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        
    
        