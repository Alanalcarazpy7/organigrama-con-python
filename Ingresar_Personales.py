from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Funciones_Dependencias import *
from PyQt5.QtWidgets import QMainWindow


class personales(object):
    def __init__(self, ventana_abrir):
        self.ventana_abrir = ventana_abrir

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:30px")
        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(350, 40))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet(u"font-size:20px")

        self.verticalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(350, 40))
        self.comboBox.setStyleSheet(u"font-size:20px")

        self.verticalLayout_2.addWidget(self.comboBox, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(150, -1, 150, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(150, 35))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {font-size:20px;background-color:green;color:white}"
                                      "QPushButton:pressed { background-color: #004603; }"
                                      "QPushButton:checked { background-color: #004603; }")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QSize(350, 550))
        self.horizontalFrame.setMaximumSize(QSize(300, 16777215))
        self.horizontalFrame.setLayoutDirection(Qt.LeftToRight)
        self.horizontalFrame.setAutoFillBackground(False)
        self.horizontalFrame.setStyleSheet(u"background-color:#0887ac")
        self.horizontalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 40, 0, 40)
        self.pushButton_9 = QPushButton(self.horizontalFrame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMinimumSize(QSize(140, 120))
        self.pushButton_9.setMaximumSize(QSize(400, 400))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setTabletTracking(False)
        self.pushButton_9.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_9.setStyleSheet(
            u"QPushButton{image: url(iconos/abrir-agregar-carpeta.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")
        self.verticalLayout_3.addWidget(self.pushButton_9, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_10 = QPushButton(self.horizontalFrame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)
        self.pushButton_10.setMinimumSize(QSize(140, 120))
        self.pushButton_10.setMaximumSize(QSize(400, 400))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(
            u"QPushButton{image: url(iconos/carpeta-abierta.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")
        self.verticalLayout_3.addWidget(self.pushButton_10, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_11 = QPushButton(self.horizontalFrame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setMinimumSize(QSize(140, 120))
        self.pushButton_11.setMaximumSize(QSize(400, 400))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(
            u"QPushButton{image: url(iconos/grupo-de-usuarios.png)}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")
        self.verticalLayout_3.addWidget(self.pushButton_11, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_12 = QPushButton(self.horizontalFrame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)
        self.pushButton_12.setMinimumSize(QSize(140, 120))
        self.pushButton_12.setMaximumSize(QSize(400, 400))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(
            u"QPushButton{image: url(iconos/archivo-pdf.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")
        self.verticalLayout_3.addWidget(self.pushButton_12, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_7.addWidget(self.horizontalFrame)

        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy4)
        self.verticalFrame.setMinimumSize(QSize(0, 250))
        self.verticalFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalFrame.setStyleSheet(u"background-color:#244434")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.verticalFrame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMaximumSize(QSize(100000, 100000))
        self.label_11.setStyleSheet(u"font-size:80px;color:white;text-align:center;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.horizontalLayout_2.addWidget(self.verticalFrame)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        ############################################################
        self.lineEdit_2.setPlaceholderText("Filtrar por Organizacion o Fecha")
        self.cargar_organigramas()
        self.pushButton.clicked.connect(self.abrir_personales)

        self.pushButton_9.clicked.connect(self.abrir_ventana_crear_organigrama)
        self.pushButton_10.clicked.connect(self.abrir_ventana_abrir_organigrama)
        self.pushButton_12.clicked.connect(self.abrir_ventana_imprimir_organigrama)
        ############################################################

        MainWindow.setWindowTitle("Ingresar Personales")
        self.label_2.setText("Ingresar Personales")
        self.pushButton.setText("Abrir")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label_11.setText("Gestor de Organigramas")

    #Funcion para cargar la listas de organigramas
    def cargar_nombres_organigramas(self):
        try:
            with open('nombres_organigramas', 'rb') as archivo:
                organigramas = pickle.load(archivo)
            return organigramas
        except FileNotFoundError:
            return []  # Devolver lista vacía si no se encuentra el archivo
    #Funcion para cargar el organigrama en el combobox
    def cargar_organigramas(self):
        nombres_organigramas = self.cargar_nombres_organigramas()
        self.comboBox.clear()
        for nombres in nombres_organigramas:
            fila = ' - '.join(nombres[1:])  # Combina los dos elementos en una sola cadena
            self.comboBox.addItem(fila, nombres[0])

        # Centra los textos de los organigramas
        for i in range(self.comboBox.count()):
            self.comboBox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

        self.lineEdit_2.textChanged.connect(self.filtrar_nombres)  # Filtrar nombres

    #Funcion para filtrar el organigrama en el combobox
    def filtrar_nombres(self):
        filtro = self.lineEdit_2.text()
        nombres_organigramas = self.cargar_nombres_organigramas()
        self.comboBox.clear()

        for nombres in nombres_organigramas:
            fila = ' - '.join(nombres[1:])  # Combina los dos elementos en una sola cadena
            if filtro.lower() in fila.lower():
                self.comboBox.addItem(fila, nombres[0])

            # Centra los textos de los organigramas
            for i in range(self.comboBox.count()):
                self.comboBox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

    def abrir_personales(self):
        codigo_org_buscar = self.comboBox.currentData()
        if codigo_org_buscar is not None:
            self.codigo_org = codigo_org_buscar  # Al abrir un organigrama,accede a esa posicion
            self.abrir_ventana_personas()

    def abrir_ventana_personas(self):
        from Personales import personales
        self.ventana_abrir.close()
        self.ventana_crear_dependencia = QMainWindow()
        self.ui = personales(self.codigo_org, self.ventana_crear_dependencia)
        self.ui.setupUi(self.ventana_crear_dependencia)
        self.ventana_crear_dependencia.show()

    def abrir_ventana_crear_organigrama(self):
        from Crear_Organigramas import crear_organigramas
        self.ventana_abrir.close()
        self.ventana_crear_organigrama = crear_organigramas()
        self.ventana_crear_organigrama.setupUi(self.ventana_crear_organigrama)
        self.ventana_crear_organigrama.show()

    def abrir_ventana_imprimir_organigrama(self):
        from imprimir_organigrama import imprimir_organigrama
        self.ventana_abrir.close()
        self.ventana_imprimir_organigrama = QMainWindow()
        self.ui = imprimir_organigrama(self.ventana_imprimir_organigrama)
        self.ui.setupUi(self.ventana_imprimir_organigrama)
        self.ventana_imprimir_organigrama.show()

    def abrir_ventana_abrir_organigrama(self):
        from Abrir_Organigramas import abrir_organigrama
        self.ventana_abrir.close()
        self.ventana_abrir_organigrama = QMainWindow()
        self.ui = abrir_organigrama(self.ventana_abrir_organigrama)
        self.ui.setupUi(self.ventana_abrir_organigrama)
        self.ventana_abrir_organigrama.show()


