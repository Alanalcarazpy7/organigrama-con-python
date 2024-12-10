import graphviz
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from graphviz import Source
from Funciones_Dependencias import *


class imprimir_organigrama(object):
    def __init__(self, ventana_imprimir):
        self.ventana_imprimir = ventana_imprimir

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
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(140, 120))
        self.pushButton_9.setMaximumSize(QSize(400, 400))
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_9.setStyleSheet(
            u"QPushButton{image: url(iconos/abrir-agregar-carpeta.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_9, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_10 = QPushButton(self.horizontalFrame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setMinimumSize(QSize(140, 120))
        self.pushButton_10.setMaximumSize(QSize(400, 400))
        self.pushButton_10.setStyleSheet(
            u"QPushButton{image: url(iconos/carpeta-abierta.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_10, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_11 = QPushButton(self.horizontalFrame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setMinimumSize(QSize(140, 120))
        self.pushButton_11.setMaximumSize(QSize(400, 400))
        self.pushButton_11.setStyleSheet(
            u"QPushButton{image: url(iconos/grupo-de-usuarios.png);background-color:#005B75}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_11, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_12 = QPushButton(self.horizontalFrame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setMinimumSize(QSize(140, 120))
        self.pushButton_12.setMaximumSize(QSize(400, 400))
        self.pushButton_12.setStyleSheet(
            u"QPushButton{image: url(iconos/archivo-pdf.png)}"
            "QPushButton:pressed { background-color: #003D57; }"
            "QPushButton:checked { background-color: #003D57; }")

        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_12, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_7.addWidget(self.horizontalFrame)

        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:30px")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.linea_filtro = QLineEdit(self.centralwidget)
        self.linea_filtro.setObjectName(u"linea_filtro")
        self.linea_filtro.setMinimumSize(QSize(350, 40))
        self.linea_filtro.setMaximumSize(QSize(16777215, 16777215))
        self.linea_filtro.setStyleSheet(u"font-size:20px")

        self.verticalLayout_2.addWidget(self.linea_filtro, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.sel_org_a_imprimir = QComboBox(self.centralwidget)
        self.sel_org_a_imprimir.setObjectName(u"sel_org_a_imprimir")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sel_org_a_imprimir.sizePolicy().hasHeightForWidth())
        self.sel_org_a_imprimir.setSizePolicy(sizePolicy2)
        self.sel_org_a_imprimir.setMinimumSize(QSize(350, 40))
        self.sel_org_a_imprimir.setStyleSheet("font-size:20px")

        self.verticalLayout_2.addWidget(self.sel_org_a_imprimir, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:30px")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.sel_dep_a_imprimir = QComboBox(self.centralwidget)
        self.sel_dep_a_imprimir.setObjectName(u"sel_dep_a_imprimir")
        sizePolicy2.setHeightForWidth(self.sel_dep_a_imprimir.sizePolicy().hasHeightForWidth())
        self.sel_dep_a_imprimir.setSizePolicy(sizePolicy2)
        self.sel_dep_a_imprimir.setMinimumSize(QSize(350, 40))
        self.sel_dep_a_imprimir.setStyleSheet(u"font-size:20px;")

        self.verticalLayout_2.addWidget(self.sel_dep_a_imprimir, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:30px")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(200, -1, 200, -1)
        self.guardarpdf = QPushButton(self.centralwidget)
        self.guardarpdf.setObjectName(u"guardarpdf")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.guardarpdf.sizePolicy().hasHeightForWidth())
        self.guardarpdf.setSizePolicy(sizePolicy3)
        self.guardarpdf.setMinimumSize(QSize(150, 35))
        self.guardarpdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.guardarpdf.setStyleSheet(u"QPushButton{font-size:20px;background-color:red;color:white}"
                                      "QPushButton:pressed { background-color: #461700; }"
                                      "QPushButton:checked { background-color: #461700; }")

        self.horizontalLayout.addWidget(self.guardarpdf)

        self.guardarjpg = QPushButton(self.centralwidget)
        self.guardarjpg.setObjectName(u"guardarjpg")
        sizePolicy3.setHeightForWidth(self.guardarjpg.sizePolicy().hasHeightForWidth())
        self.guardarjpg.setSizePolicy(sizePolicy3)
        self.guardarjpg.setMinimumSize(QSize(150, 35))
        self.guardarjpg.setCursor(QCursor(Qt.PointingHandCursor))
        self.guardarjpg.setStyleSheet(u"QPushButton {font-size:20px;background-color:green;color:white}"
                                      "QPushButton:pressed { background-color: #004603; }"
                                      "QPushButton:checked { background-color: #004603; }")

        self.horizontalLayout.addWidget(self.guardarjpg)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy4)
        self.verticalFrame.setMinimumSize(QSize(0, 250))
        self.verticalFrame.setMaximumSize(QSize(1550, 16777215))
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

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        ############################################################
        self.cargar_dependencia_organigramas()
        self.linea_filtro.textChanged.connect(self.filtrar_imp)
        self.linea_filtro.setPlaceholderText("Filtrar por Organizacion o Fecha")
        self.guardarpdf.clicked.connect(lambda: self.imprimir("pdf"))
        self.guardarjpg.clicked.connect(lambda: self.imprimir("jpg"))

        self.pushButton_9.clicked.connect(self.abrir_ventana_crear_organigrama)
        self.pushButton_10.clicked.connect(self.abrir_ventana_abrir_organigrama)
        self.pushButton_11.clicked.connect(self.ventana_personales)
        self.actualizar_lista_dependencia()
        self.sel_org_a_imprimir.currentIndexChanged.connect(self.actualizar_lista_dependencia)
        ############################################################
        MainWindow.setWindowTitle("Guardar Organigrama Como")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label_11.setText("Gestor de Organigramas")
        self.label_2.setText("Seleccione un organigrama:")
        self.label_3.setText("Seleccione una dependencia")
        self.label.setText("Guardar como:")
        self.guardarpdf.setText("PDF")
        self.guardarjpg.setText("JPG")

    #Carga las dependencias que existen en el organigrama
    def cargar_dependencia_organigramas(self):
        nombres_organigramas = cargar_nombres_organigramas()
        self.sel_org_a_imprimir.clear()
        for nombres in nombres_organigramas:
            fila = ' - '.join(nombres[1:])  # Combina los dos elementos en una sola cadena
            self.sel_org_a_imprimir.addItem(fila, nombres[0])

        # Centra los textos de los organigramas
        for i in range(self.sel_org_a_imprimir.count()):
            self.sel_org_a_imprimir.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

    #Filtra los organigramas en la seccion de imprimir
    def filtrar_imp(self):
        filtro = self.linea_filtro.text()
        self.sel_org_a_imprimir.clear()
        nom_cod_org = cargar_nombres_organigramas()
        for nombres in nom_cod_org:
            if filtro.lower() in (nombres[1] + " - " + nombres[2]).lower():
                self.sel_org_a_imprimir.addItem(nombres[1] + " - " + nombres[2], nombres[0])

    #Funcion para imprimir un organigrama completo, el parametro que se le pase debera ser "jpg" o "pdf"
    def imprimir(self, parametro):
        codigo_org_buscar = self.sel_org_a_imprimir.currentData()
        codigo_dep_buscar = self.sel_dep_a_imprimir.currentData()
        if codigo_org_buscar is not None:
            self.personal = cargar_personas_organigrama(codigo_org_buscar)
            Org_a_imprimir = cargar_dependencia_organigrama(codigo_org_buscar)
            if Org_a_imprimir.raiz is not None:
                try:
                    listas = gen_lista_grafica(codigo_dep_buscar, Org_a_imprimir.raiz, self.personal)

                    contenido = [
                        'digraph G {',
                        '    node [shape=rectangle style=filled fontname="Helvetica" fontsize=14 width=1.5 height=0.6 penwidth=1.5 fillcolor="#948F8F" fontcolor=white];',
                        f'    edge [penwidth=1.5 arrowhead=none arrowsize=1.5 dir=forward];',
                        # Estilos de la Flecha
                        f'    graph [splines=true overlap=false];',
                    ]

                    # Al editar dependencia me sale un error de None por eso coloco esto
                    if listas is not None:
                        lista1 = listas[0]
                        lista2 = listas[1]

                        # En el caso de que no exista nigun nodo inferior,estas condiciones sirven para que muestre en pantalla el unico nodo existente
                        if lista1:
                            for i in range(len(lista1)):
                                concatenar = f'"{lista1[i]}" -> "{lista2[i]}"'  # "Departamento de Recursos Humanos" -> "Gerente de Recursos Humanos" Asi debe imprimir por eso hago esto,para que sepa donde poner la flecha al graficar
                                contenido.append(concatenar)

                        else:
                            nombre_dep = self.sel_dep_a_imprimir.currentText()  # "Departamento de Recursos Humanos" -> "Gerente de Recursos Humanos" Asi debe imprimir por eso hago esto,para que sepa donde poner la flecha al graficar
                            jefe_dep = obtener_jefe(Org_a_imprimir.raiz, codigo_dep_buscar, self.personal)
                            if jefe_dep == "":
                                jefe_dep = "\n(No asignado)"
                            else:
                                jefe_dep = '\n' + jefe_dep
                            concatenar = nombre_dep + jefe_dep
                            contenido.append(f'"{concatenar}"')
                        contenido.append("}")

                    # Guarda la lista como un archivo de texto
                    with open("grafo.txt", "w") as f:
                        f.write('\n'.join(contenido))

                    # Lee el archivo de texto con la definición del grafo
                    with open("grafo.txt", "r") as f:
                        contenido = f.read()

                    # Abrir el diálogo de selección de archivo
                    file_dialog = QFileDialog()
                    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
                    file_dialog.setWindowTitle("Guardar Organigrama")

                    if parametro == "pdf":
                        file_dialog.setNameFilters(["PDF (*.pdf)"])
                        if file_dialog.exec_() == QFileDialog.Accepted:
                            ruta_guardado = file_dialog.selectedFiles()[0]  # Obtiene la ruta seleccionada
                            ruta_guardado = os.path.splitext(ruta_guardado)[0]  # Elimina el .pdf repetido
                            # Genera el grafo a partir del archivo de texto
                            grafo = Source(contenido, format="pdf")

                            # Guarda el grafo como un archivo de imagen(imprime como png)
                            grafo.render(ruta_guardado, view=True)
                            pixmap = QPixmap(ruta_guardado)
                            os.remove(ruta_guardado)
                            return pixmap
                    else:
                        file_dialog.setNameFilters(["JPEG (*.jpg)"])
                        if file_dialog.exec_() == QFileDialog.Accepted:
                            ruta_guardado = file_dialog.selectedFiles()[0]
                            ruta_guardado = os.path.splitext(ruta_guardado)[0]  # Elimina el .jpg repetido
                            # Genera el grafo a partir del archivo de texto
                            grafo = Source(contenido, format="jpg")
                            # Guarda el grafo como un archivo de imagen(imprime como png)
                            grafo.render(ruta_guardado, view=True)
                            pixmap = QPixmap(ruta_guardado)
                            os.remove(ruta_guardado)
                            return pixmap

                except graphviz.backend.CalledProcessError:
                    pass

    #Permite actualizar la lista de dependencias para colocarlos en el combobox
    def actualizar_lista_dependencia(self):
        self.sel_dep_a_imprimir.clear()
        codigo_org_buscar = self.sel_org_a_imprimir.currentData()
        Dependencias = []
        Organigrama_a_imprimir = cargar_dependencia_organigrama(codigo_org_buscar)
        if Organigrama_a_imprimir is not None:
            if Organigrama_a_imprimir is not None:
                Dependencias = matriz_nombre_codigo(Organigrama_a_imprimir.raiz, Dependencias)
            for dependencia in Dependencias:
                self.sel_dep_a_imprimir.addItem(dependencia[0], dependencia[1])

    #Abre las distintas ventanas en el menu del lado izquierdo
    def abrir_ventana_crear_organigrama(self):
        from Crear_Organigramas import crear_organigramas
        self.ventana_imprimir.close()
        self.ventana_crear_organigrama = crear_organigramas()
        self.ventana_crear_organigrama.setupUi(self.ventana_crear_organigrama)
        self.ventana_crear_organigrama.show()

    def abrir_ventana_abrir_organigrama(self):
        from Abrir_Organigramas import abrir_organigrama
        self.ventana_imprimir.close()
        self.ventana_abrir_organigrama = QMainWindow()
        self.ui = abrir_organigrama(self.ventana_abrir_organigrama)
        self.ui.setupUi(self.ventana_abrir_organigrama)
        self.ventana_abrir_organigrama.show()

    def ventana_personales(self):
        from Ingresar_Personales import personales
        self.ventana_imprimir.close()
        self.ventana_personales = QMainWindow()
        self.ui = personales(self.ventana_personales)
        self.ui.setupUi(self.ventana_personales)
        self.ventana_personales.show()


