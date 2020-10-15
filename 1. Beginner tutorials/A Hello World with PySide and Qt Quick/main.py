#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
 
# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
view = QQuickView()
# Create an URL to the QML file
url = QUrl('message.qml')
# Set the QML file and show
view.setSource(url)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())