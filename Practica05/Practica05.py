# Practica05.py

# Autor: Misael Saenz Flores
# Fecha: 09/09/2016
#
# Programa para generar una interfaz con PyQt
#

# Importamos las libresas a usar
from PyQt4 import QtCore, QtGui
from datetime import datetime, date, time, timedelta

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