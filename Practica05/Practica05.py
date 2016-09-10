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
		return QtGui.QApplication.translate(context,text,disambig,Encoding)
except AttributeError:
	def Traslate(context, text, disambig):
		return QtGui.QApplication.translate(context,text,disambig)

# Agregamos una clase para la interfaz

class MiVentana(object):
# Definimos la funcion principal donde estaran las Label, imagenes, etc.
	def ventana_Principal(self, Form):
		Form.setObjectName(CfromUtf8("Form"))
		Form.resize(640, 480)
		Form.setMinimumSize(QtCore.QSize(640, 480))
		Form.setMaximumSize(QtCore.QSize(640, 480))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(CfromUtf8("Recursos/bandera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowIcon(icon)
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
		self.label.setAlignment(QtCore.Qt.AlignCenter)
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
# Se agregaron Labe's para contener las imagenes
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 130, 40, 40))
        self.label_4.setText(CfromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(CfromUtf8("Recursos/metro-hidalgo.png")))
        self.label_4.setObjectName(CfromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 180, 40, 40))
        self.label_5.setText(CfromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(CfromUtf8("Recursos/metro-allende.png")))
        self.label_5.setObjectName(CfromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 230, 40, 40))
        self.label_6.setText(CfromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(CfromUtf8("Recursos/metro-morelos.png")))
        self.label_6.setObjectName(CfromUtf8("label_6"))
# Agregamos el boton el cual al precionarlo nos dira cuantos dias faltan para el
# proximo 15 de septiembre del siguiente año.
		self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 330, 500, 61))
        font = QtGui.QFont()
        font.setFamily(CfromUtf8("Arial"))
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(CfromUtf8("pushButton"))
        self.retranslateUi(Form)
        self.pushButton.setCheckable(True)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(CfromUtf8("clicked()")), self.btnstate)
        QtCore.QMetaObject.connectSlotsByName(Form)
# Definimos la funcion que nos dira los dias que faltan para una fecha
	def dias_transcurridos(self):
		hoy = date.today()
		quince_proximo = date(2017, 9, 15)
		faltan = quince_proximo - hoy
		return str(faltan.days)
# Definimos la funcion para que el boton sea dinamico
	def btnstate(self):
		if self.pushButton.isChecked():
			cadena = "Faltan " + self.dias_transcurridos() + " para el proximo 15 de Sep."
			self.pushButton.setText(cadena)
		else:
			self.pushButton.setText("Aprietame")
# Se agrega el texto a las label's
	def retranslateUi(self, Form):
        Form.setWindowTitle(Traslate("Form", "¡Viva Mexico!", None))
        self.label.setText(Traslate("Form", "Miguel Hidalgo y Costilla", None))
        self.label_2.setText(Traslate("Form", "Ignacio Allende", None))
        self.label_3.setText(Traslate("Form", "Jose Maria Morelos y Pavon", None))
        self.pushButton.setText(Traslate("Form", "Aprietame", None))

# Digamos que agregamos el main para que nos muestre todo
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ventana = MiVentana()
ventana.ventana_Principal(Form)
Form.show()
sys.exit(app.exec_())
