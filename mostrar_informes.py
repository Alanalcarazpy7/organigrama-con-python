from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout
from Informes import *

class Ui_Informes(object):
    def __init__(self, codigo_org, ventana_informes):
        self.ventana_informes = ventana_informes
        self.codigo_org = codigo_org

    def setupUi(self, Informes):
        self.nom_deps = []
        self.Organigramas = cargar_dependencia_organigrama(self.codigo_org)
        self.seleccion = []
        self.informe = informes(self.codigo_org)
        self.informe.cargar_datos()
        self.aux_nom_ape = []
        self.aux_nom_ape_ext = []
        self.aux_salario = []
        self.aux_salario_ext = []

        Informes.setObjectName("Informes")
        Informes.setWindowState(Qt.WindowMaximized)
        self.centralwidget = QtWidgets.QWidget(Informes)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalFrame_5 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_5.setStyleSheet("background-color:#244434")
        self.verticalFrame_5.setObjectName("verticalFrame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.verticalFrame_5)
        self.label_14.setMaximumSize(QtCore.QSize(100000, 100000))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font-size:80px;color:white;text-align:center;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.gridLayout_3.addWidget(self.verticalFrame_5, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(2, 10, -1, -1)
        self.horizontalLayout_8.setSpacing(17)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.selecciontipo = QtWidgets.QLabel(self.centralwidget)
        self.selecciontipo.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.selecciontipo.setFont(font)
        self.selecciontipo.setStyleSheet("font-size:20px;\n"
                                         "")
        self.selecciontipo.setObjectName("selecciontipo")
        self.horizontalLayout_8.addWidget(self.selecciontipo, 0, QtCore.Qt.AlignRight)

        self.comboBoxinfor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxinfor.setGeometry(QtCore.QRect(310, 70, 261, 31))
        self.comboBoxinfor.setObjectName("comboBoxinfor")
        self.comboBoxinfor.setMinimumSize(QtCore.QSize(200, 27))
        self.comboBoxinfor.setStyleSheet(u"font-size:18px")
        self.seleccion.append("Personal por Dependencia")
        self.seleccion.append("Salario por Dependencia")
        self.comboBoxinfor.addItems(self.seleccion)

        self.horizontalLayout_8.addWidget(self.comboBoxinfor, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(18)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.selecciondpn = QtWidgets.QLabel(self.centralwidget)
        self.selecciondpn.setMaximumSize(QtCore.QSize(16777215, 16777214))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.selecciondpn.setFont(font)
        self.selecciondpn.setStyleSheet("font-size:20px;\n"
                                        "")
        self.selecciondpn.setObjectName("selecciondpn")
        self.horizontalLayout_9.addWidget(self.selecciondpn, 0, QtCore.Qt.AlignRight)
        self.comboBox_depend = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_depend.setMinimumSize(QtCore.QSize(200, 27))
        self.comboBox_depend.setObjectName("comboBox_depend")
        self.comboBox_depend.setStyleSheet(u"font-size:18px")
        self.horizontalLayout_9.addWidget(self.comboBox_depend, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Switchextnd = QtWidgets.QPushButton(self.centralwidget)
        self.Switchextnd.setStyleSheet("QPushButton {font-size:20px;background-color:#0977A4;color:white;}\n"
                                       "QPushButton:pressed {background-color: #003D57;}\n"
                                       "QPushButton:checked {background-color: #003D57;}")
        self.Switchextnd.setObjectName("Switchextnd")
        self.horizontalLayout.addWidget(self.Switchextnd)
        self.Switchextnd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("background-color:#0887ac")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("font-size:20px;background-color:#0977A4;color:white")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        # Crear un layout horizontal
        layout = QHBoxLayout(self.pushButton_3)

        # Crear el QLabel para la imagen
        self.image_label = QLabel(self.pushButton_3)

        # Crear el QLabel para el texto
        self.text_label = QLabel()
        self.font = QFont()

        # Agregar los QLabel al layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)

        # Aplicar el estilo al QPushButton
        self.pushButton_3.setStyleSheet('''
                           QPushButton {
                               font-size: 20px;
                               background-color: #0977A4;
                               color: white;
                               border: none;
                               border-radius: 20px;
                               padding: 10px;
                           }

                           QPushButton:hover {
                               background-color: #005189;
                           }

                           QPushButton:pressed {
                               background-color: #003D57;
                       ''')

        layout.setSpacing(10)
        self.image_label.setStyleSheet("background-color: transparent;border-radius:35px")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(10, 0, 30, 0)
        self.text_label.setStyleSheet("background-color: transparent;")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))


        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("font-size:20px;background-color:#0977A4;color:white")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font-size:20px;background-color:#0977A4;color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.lista_visualizar = QtWidgets.QListWidget(self.centralwidget)
        self.lista_visualizar.setObjectName("lista_visualizar")
        self.lista_visualizar.setStyleSheet(u"font-size:18px")
        self.gridLayout_3.addWidget(self.lista_visualizar, 2, 1, 1, 1)
        Informes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Informes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1253, 21))
        self.menubar.setObjectName("menubar")
        Informes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Informes)
        self.statusbar.setObjectName("statusbar")
        Informes.setStatusBar(self.statusbar)

        self.cargar_dpn()
        self.mostrar_informe_personal(self.comboBox_depend.currentIndex())
        self.comboBoxinfor.currentIndexChanged.connect(self.mostrar_informe)
        self.Switchextnd.clicked.connect(self.mostrar_informe_extendido)

        QtCore.QMetaObject.connectSlotsByName(Informes)

        ####################################################
        self.cargar_conf_modo()
        self.pushButton_5.clicked.connect(self.abrir_menu_principal)
        self.pushButton_2.clicked.connect(self.ventana_dependencia)
        self.pushButton_3.clicked.connect(self.modo_oscuro)
        self.aplicar_estilos()
        ###################################################

        Informes.setWindowTitle("Informes")
        self.label_14.setText("INFORMES")
        self.selecciontipo.setText("Seleccionar tipo de informe:")
        self.selecciondpn.setText("Seleccionar dependencia:")
        self.Switchextnd.setText("Ver Version Extendida")
        self.pushButton_2.setText("Ir a Dependencias")
        self.pushButton_5.setText("Ir al Menu Principal")

        # Cargar los comboBox

    def cargar_dpn(self):
        try:
            file_path = os.path.join("archivos_organigramas", f'organigrama{self.codigo_org}_dependencias')
            with open(file_path, "rb") as archivo:
                self.Organigramas = pickle.load(archivo)
                self.nom_deps = matriz_nombre_codigo(self.Organigramas.raiz, [])
        except FileNotFoundError:
            self.nom_deps = []
        for dependencia in self.nom_deps:
            self.comboBox_depend.addItem(dependencia[0])

    def mostrar_informe_personal(self, index):
        self.aux_nom_ape = []
        self.lista_visualizar.clear()  # Borra los elementos existentes en la lista visual
        self.aux_nom_ape = self.informe.get_nom_ape(self.comboBox_depend.itemText(index))
        if self.aux_nom_ape:
            self.lista_visualizar.addItems(self.aux_nom_ape)
        else:
            self.lista_visualizar.addItem("No hay información disponible.")

        # Conectar la señal currentIndexChanged
        self.comboBox_depend.currentIndexChanged.connect(self.mostrar_informe_personal)

    def mostrar_salario_dependencia(self, index):
        self.aux_salario = []
        self.lista_visualizar.clear()  # Borra los elementos existentes en la lista visual
        self.aux_salario = self.informe.salario_por_dep(self.comboBox_depend.itemText(index))
        self.lista_visualizar.addItem(self.comboBox_depend.itemText(index))
        if self.aux_salario[0] > 0:
            self.lista_visualizar.addItem(f"La cantidad de personal es: {self.aux_salario[0]}")
            self.lista_visualizar.addItem(" ")
            self.lista_visualizar.addItem(f"El total de salarios es: {self.aux_salario[1]}")
        else:
            self.lista_visualizar.addItem("No hay información disponible.")

        # Conectar la señal currentIndexChanged
        self.comboBox_depend.currentIndexChanged.connect(self.mostrar_salario_dependencia)

    def mostrar_nom_extendido(self, index):
        self.aux_nom_ape_ext = []
        self.lista_visualizar.clear()
        self.aux_nom_ape_ext = self.informe.get_nom_ape_extend(self.comboBox_depend.itemText(index))
        if len(self.aux_nom_ape_ext) != 0:
            self.lista_visualizar.addItems(self.aux_nom_ape_ext)
        else:
            self.lista_visualizar.addItem("No hay personal registrado en esta dependencia")

    def mostrar_sal_extendido(self, index):
        self.aux_salario_ext = []
        self.lista_visualizar.clear()
        self.aux_salario_ext = self.informe.salario_por_dep_extend(self.comboBox_depend.itemText(index))
        self.lista_visualizar.addItems(self.aux_salario_ext)



    def mostrar_informe(self):
        if self.comboBoxinfor.currentIndex() == 0:
            self.mostrar_informe_personal(self.comboBox_depend.currentIndex())
            # Connect the signal currentIndexChanged to mostrar_informe_personal
            self.comboBox_depend.currentIndexChanged.connect(self.mostrar_informe_personal)
            # Disconnect the signal currentIndexChanged from mostrar_salario_dependencia
            self.comboBox_depend.currentIndexChanged.disconnect(self.mostrar_salario_dependencia)
        elif self.comboBoxinfor.currentIndex() == 1:
            self.mostrar_salario_dependencia(self.comboBox_depend.currentIndex())
            # Connect the signal currentIndexChanged to mostrar_salario_dependencia
            self.comboBox_depend.currentIndexChanged.connect(self.mostrar_salario_dependencia)
            # Disconnect the signal currentIndexChanged from mostrar_informe_personal
            self.comboBox_depend.currentIndexChanged.disconnect(self.mostrar_informe_personal)

    def mostrar_informe_extendido(self):
        index = self.comboBox_depend.currentIndex()
        if self.comboBoxinfor.currentIndex() == 0:
            self.mostrar_nom_extendido(index)
            if len(self.aux_nom_ape_ext) == 0:
                self.lista_visualizar.addItem("No hay personal extendido registrado en esta dependencia")
        else:
            self.mostrar_sal_extendido(index)
            if len(self.aux_salario_ext) == 0:
                self.lista_visualizar.addItem("No hay información de salario para esta dependencia")

    def abrir_menu_principal(self):
        from Menu_Principal import menu_principal
        self.ventana_informes.close()
        self.ventana_abrir_menu = QMainWindow()
        self.ui = menu_principal(self.ventana_abrir_menu)
        self.ui.setupUi(self.ventana_abrir_menu)
        self.ventana_abrir_menu.show()

    def ventana_dependencia(self):
        from Crear_Dependencias import Dependencias
        self.ventana_informes.close()
        self.ventana_crear_dependencia = QMainWindow()
        self.ui = Dependencias(self.codigo_org, self.ventana_crear_dependencia)
        self.ui.setupUi(self.ventana_crear_dependencia)
        self.ventana_crear_dependencia.show()
        self.ui.generar_grafo()

    def modo_oscuro(self):
        self.es_modo_oscuro = not self.es_modo_oscuro
        self.aplicar_estilos()
        self.guardar_conf()

    def aplicar_estilos(self):

        if self.es_modo_oscuro:
            self.centralwidget.setStyleSheet("background-color: #333333; color: #ffffff;")
            self.pushButton_3.setText("")
            self.image_label.setPixmap(QPixmap(
                "iconos/modo-de-luz.png"))
            self.font.setPointSize(15)
            self.text_label.setText("Claro")
            self.text_label.setFont(self.font)

        else:
            self.centralwidget.setStyleSheet("background-color: #ffffff; color: #333333;")
            self.pushButton_3.setText("")
            self.pushButton_3.setStyleSheet('''
                                           font-size: 20px;
                                           background-color: #0977A4;
                                           color: white;
                                           border: none;
                                           border-radius: 20px;
                                           padding: 10px;
                                       }

                                       QPushButton:hover {
                                           background-color: #005189;
                                       }

                                       QPushButton:pressed {
                                           background-color: #003D57;
                                   ''')
            self.image_label.setPixmap(QPixmap(
                "iconos/luna (1).png"))
            self.font.setPointSize(15)
            self.text_label.setText("Oscuro")
            self.text_label.setFont(self.font)

        # Cambiar el color del texto según el fondo
        palette = self.pushButton_3.palette()
        if self.es_modo_oscuro:
            palette.setColor(self.pushButton_3.foregroundRole(), Qt.white)
            palette.setColor(self.centralwidget.foregroundRole(), Qt.white)
        else:
            palette.setColor(self.pushButton_3.foregroundRole(), Qt.black)
        self.pushButton_3.setPalette(palette)

    def cargar_conf_modo(self):
        if os.path.exists("modo_claro_oscuro_conf"):
            with open("modo_claro_oscuro_conf", "rb") as f:
                try:
                    data = pickle.load(f)
                    self.es_modo_oscuro = data[0]
                except (pickle.PickleError, EOFError):
                    self.es_modo_oscuro = False
        else:
            self.es_modo_oscuro = False

    def guardar_conf(self):
        with open("modo_claro_oscuro_conf", "wb") as f:
            pickle.dump([self.es_modo_oscuro], f)

