#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:58:44 2021

@author: miller
"""
import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
w   = MainWindow()
w.show()
sys.exit(app.exec_())
