from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime
from Funciones_Dependencias import *


class crear_organigramas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lista_organigramas=[]
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QSize(300, 550))
        self.horizontalFrame.setMaximumSize(QSize(350, 16777215))
        self.horizontalFrame.setLayoutDirection(Qt.LeftToRight)
        self.horizontalFrame.setAutoFillBackground(False)
        self.horizontalFrame.setStyleSheet(u"background-color:#0887ac")
        self.horizontalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 40, 0, 40)
        self.pushButton_8 = QPushButton(self.horizontalFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(140, 120))
        self.pushButton_8.setMaximumSize(QSize(400, 400))
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(
            u"QPushButton{image: url(iconos/abrir-agregar-carpeta.png);}")
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_8, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_6 = QPushButton(self.horizontalFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(140, 120))
        self.pushButton_6.setMaximumSize(QSize(400, 400))
        self.pushButton_6.setStyleSheet(
            u"QPushButton{image: url(iconos/carpeta-abierta.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_6, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.horizontalFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(140, 120))
        self.pushButton_5.setMaximumSize(QSize(400, 400))
        self.pushButton_5.setStyleSheet(
            u"QPushButton{image: url(iconos/grupo-de-usuarios.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_5, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_7 = QPushButton(self.horizontalFrame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(140, 120))
        self.pushButton_7.setMaximumSize(QSize(400, 400))
        self.pushButton_7.setStyleSheet(
            u"QPushButton{image: url(iconos/archivo-pdf.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_7, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_7.addWidget(self.horizontalFrame)

        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:30px")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet(u"font-size:20px")

        self.verticalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:18px;color:red;")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:30px")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setStyleSheet(u"font-size:20px")

        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:18px;color:red;")

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(140, 30))
        self.pushButton.setStyleSheet(
            u"QPushButton{font-size:20px;background-color:green;color:white}"
            "QPushButton:pressed { background-color: #004603; }"
            "QPushButton:checked { background-color: #004603; }")

        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(0, 250))
        self.verticalFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalFrame.setStyleSheet(u"background-color:#244434")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.verticalFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(100000, 100000))
        self.label_11.setStyleSheet(u"font-size:80px;color:white;text-align:center;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.horizontalLayout_2.addWidget(self.verticalFrame)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi


        ######################################
        self.label_3.setObjectName("l_error_apellido")
        self.pushButton.clicked.connect(self.organigramas)
        self.lineEdit.setPlaceholderText("DD/MM/AAAA")
        self.lineEdit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lineEdit_2.setPlaceholderText("Nombre del Organigrama")
        self.lineEdit_2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.pushButton_6.clicked.connect(self.abrir_ventana_abrir_organigrama)
        self.pushButton_7.clicked.connect(self.abrir_ventana_imprimir_organigrama)
        self.pushButton_5.clicked.connect(self.abrir_ventana_personales)
        ######################################


        MainWindow.setWindowTitle("Crear Organigramas")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText("Organizacion Representada")
        self.label.setText("Fecha de Vigencia")
        self.pushButton.setText("Crear")
        self.label_11.setText("Gestor de Organigramas")

    #Permite crear un organigrama validando la fecha y el nombre ingresado
    def organigramas(self):
        nom = self.lineEdit_2.text()
        nom_organigrama = nom.strip()
        fecha = self.lineEdit.text()
        self.codigo = generar_codigo_ORG(cargar_nombres_organigramas())
        if self.validar(nom_organigrama, fecha):
            lista_datos_organigramas = cargar_nombres_organigramas()  # Cargar la lista de datos de organigramas
            org = Organigrama(self.codigo, nom_organigrama, fecha)
            codigo_org = self.codigo
            guardar_dependencia_organigrama(codigo_org, org)  # Guarda el archivo de organigrama
            datos_organigrama = [self.codigo, nom_organigrama, fecha]  # Crear el organigrama actual
            lista_datos_organigramas.append(datos_organigrama)  # Agregar el organigrama a la lista de datos
            guardar_nombres_organigrama(lista_datos_organigramas)  # Guarda el organigrama creado
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.abrir_dependencia()

    #Valida la fecha y nombre que se ingresan
    def validar(self, organizacion, fecha):
        contador = 0
        if len(organizacion) == 0:
            self.label_3.setText("Por favor, ingrese un nombre de Organizacion")
            contador += 1
        for caracter in organizacion:
            if not caracter.isalnum() and caracter != ' ' and caracter!=".":
                self.label_3.setText("Por favor, ingrese un nombre sin caracteres especiales")
                contador += 1
        if contador==0:
            self.label_3.clear()

        if len(fecha) == 0 or self.fecha_valida(fecha)==False:
            self.label_4.setText("Por favor, ingrese una Fecha valida")
            contador += 1
        else:
            self.label_4.clear()
        if contador > 0:
            return False
        else:
            return True

    def fecha_valida(self,fecha):
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    #Permite abrir la ventana de dependencia cuando se crea el organigrama
    def abrir_dependencia(self):
        from Crear_Dependencias import Dependencias
        self.close()
        self.ventana_crear_dependencia = QMainWindow()
        self.codigo_org = self.codigo
        self.ui = Dependencias(self.codigo_org, self.ventana_crear_dependencia)
        self.ui.setupUi(self.ventana_crear_dependencia)
        self.ventana_crear_dependencia.show()

    #Permite abrir la ventana de abrir organigrama del menu en el ladi izquierdo de la interfaz
    def abrir_ventana_abrir_organigrama(self):
        from Abrir_Organigramas import abrir_organigrama
        self.close()
        self.ventana_abrir_organigrama = QMainWindow()
        self.ui = abrir_organigrama(self.ventana_abrir_organigrama)
        self.ui.setupUi(self.ventana_abrir_organigrama)
        self.ventana_abrir_organigrama.show()

    # Permite abrir la ventana de imprimir organigrama del menu en el ladi izquierdo de la interfaz
    def abrir_ventana_imprimir_organigrama(self):
        from imprimir_organigrama import imprimir_organigrama
        self.close()
        self.ventana_imprimir_organigrama = QMainWindow()
        self.ui = imprimir_organigrama(self.ventana_imprimir_organigrama)
        self.ui.setupUi(self.ventana_imprimir_organigrama)
        self.ventana_imprimir_organigrama.show()

    # Permite abrir la ventana de personales del menu en el ladi izquierdo de la interfaz
    def abrir_ventana_personales(self):
        from Ingresar_Personales import personales
        self.close()
        self.ventana_personales = QMainWindow()
        self.ui = personales(self.ventana_personales)
        self.ui.setupUi(self.ventana_personales)
        self.ventana_personales.show()

