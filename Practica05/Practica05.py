# Practica05.py

# Autor: Misael Saenz Flores
# Fecha: 09/09/2016
#
# Programa para generar una interfaz con PyQt
#

# Importamos las libresas a usar
from PyQt4 import QtCore, QtGui
from datetime import datetime, date, time, timedelta
import sys

# Agregamos algunas excepciones para no tener problemas
# con la codificacion.

try:
	CfromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def CfromUtf8(s):
		return s

try:
	Encoding = QtGui.QApplication.UnicodeUTF8
	def Traslate(context, text, disambig):
		return QtGui.QApplication.traslate(context,text,disambig,Encoding)
except AttributeError:
	def Traslate(context, text, disambig):
		return QtGui.QApplication.traslate(context,text,disambig)

# Agregamos una clase para la interfaz

class MiVentana(object):

# Definimos la funcion principal donde estaran las Label, imagenes, etc.
	def principal_Ventana(self, Form):
		Form.setObjectName(CfromUtf8("Form"))
		Form.resize(640, 480)
		Form.setMinimumSize(QtCore.QSize(640, 480))
		Form.setMaximumSize(QtCore.QSize(640, 480))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(CfromUtf8("Recursos/bandera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowsIcon(icon)
		Form.setLayoutDirection(QtCore.Qt.LeftToRight)
# Definimos las label's a usar para agregar el texto
		self.label = QtGui.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(185, 140, 271, 31))
		font = QtGui.QFont()
		font.setFamily(CfromUtf8("Arial"))
		font.setPointSize(18)
		font.setItalic(False)
		self.label.setFont(font)
		self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label.setAlignment(QtCore.Qt.AlingCenter)
		self.label.setWordWrap(True)
		self.label.setObjectName(CfromUtf8("label"))
		self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 181, 31))
        font = QtGui.QFont()
        font.setFamily(CfromUtf8("Arial"))
        font.setPointSize(18)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(CfromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(185, 240, 311, 31))
        font = QtGui.QFont()
        font.setFamily(CfromUtf8("Arial"))
        font.setPointSize(18)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(CfromUtf8("label_3"))