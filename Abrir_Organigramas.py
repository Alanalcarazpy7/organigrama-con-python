from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Funciones_Dependencias import *
from PyQt5.QtWidgets import QMainWindow


class abrir_organigrama(object):
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

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(150, 35))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0887ac;color:white}"
                                      "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(150, 35))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0887ac;color:white}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(150, 35))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{font-size:20px;background-color:#CB0808;color:white}"
                                        "QPushButton:pressed { background-color: #461700; }"
                                        "QPushButton:checked { background-color: #461700; }")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1, Qt.AlignVCenter)

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
            u"image: url(iconos/carpeta-abierta.png)")

        self.verticalLayout_3.addWidget(self.pushButton_10, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.pushButton_11 = QPushButton(self.horizontalFrame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setMinimumSize(QSize(140, 120))
        self.pushButton_11.setMaximumSize(QSize(400, 400))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(
            u"QPushButton{image: url(iconos/grupo-de-usuarios.png);background-color:#005B75}"
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
        self.pushButton.clicked.connect(self.abrir_org)
        self.pushButton_2.clicked.connect(self.editar_org)
        self.pushButton_3.clicked.connect(self.copiar_organigrama)
        self.pushButton_4.clicked.connect(self.eliminar_organigrama)
        self.pushButton_9.clicked.connect(self.abrir_ventana_crear_organigrama)
        self.pushButton_12.clicked.connect(self.abrir_ventana_imprimir_organigrama)
        self.pushButton_11.clicked.connect(self.abrir_ventana_personales)
        self.lineEdit_2.textChanged.connect(self.filtrar_nombres)  # Filtrar nombres
        ############################################################

        MainWindow.setWindowTitle("Abrir Organigramas")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label_11.setText("Gestor de Organigramas")
        self.label_2.setText(u"Abrir Organigramas")
        self.pushButton.setText("Abrir")
        self.pushButton_2.setText("Editar")
        self.pushButton_3.setText("Copiar")
        self.pushButton_4.setText("Eliminar")

    def guardar_nombres_organigrama(self, organigramas):
        with open('nombres_organigramas', 'wb') as archivo:
            pickle.dump(organigramas, archivo)  # Guardar la lista completa

    #Carga los Organigramas leidos en el combobox
    def cargar_organigramas(self):
        nombres_organigramas = cargar_nombres_organigramas()
        self.comboBox.clear()
        for nombres in nombres_organigramas:
            fila = ' - '.join(nombres[1:])  # Combina los dos elementos en una sola cadena
            self.comboBox.addItem(fila, nombres[0])
        # Centra los textos de los organigramas
        for i in range(self.comboBox.count()):
            self.comboBox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)


    #Filtrar Organigramas por nombre y fecha
    def filtrar_nombres(self):
        filtro = self.lineEdit_2.text()
        nombres_organigramas = cargar_nombres_organigramas()

        self.comboBox.clear()
        for nombres in nombres_organigramas:
            fila = ' - '.join(nombres[1:])  # Combina los dos elementos en una sola cadena
            if filtro.lower() in fila.lower():
                self.comboBox.addItem(fila, nombres[0])

            # Centra los textos de los organigramas
            for i in range(self.comboBox.count()):
                self.comboBox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

    #Selecciona el codigo y llama a la funcion abrir dependencia para que se abra esa dependencia
    def abrir_org(self):
        codigo_org_buscar = self.comboBox.currentData()
        if codigo_org_buscar is not None:
            self.codigo_org = codigo_org_buscar  # Al abrir un organigrama,accede a esa posicion
            self.abrir_dependencia()

    # Abrir la dependencia de ese organigrama seleccionado mediante su codigo leido
    def abrir_dependencia(self):
        from Crear_Dependencias import Dependencias
        self.ventana_abrir.close()
        self.ventana_crear_dependencia = QMainWindow()
        self.ui = Dependencias(self.codigo_org, self.ventana_crear_dependencia)
        self.ui.setupUi(self.ventana_crear_dependencia)
        self.ventana_crear_dependencia.show()
        self.ui.generar_grafo()

    #Abre la ventana de crear organigramas, seleccionada en el menu del lado izquierdo
    def abrir_ventana_crear_organigrama(self):
        from Crear_Organigramas import crear_organigramas
        self.ventana_abrir.close()
        self.ventana_crear_organigrama = crear_organigramas()
        self.ventana_crear_organigrama.setupUi(self.ventana_crear_organigrama)
        self.ventana_crear_organigrama.show()

    #Abre la ventana de imprimir organigramas, seleccionada en el menu del lado izquierdo
    def abrir_ventana_imprimir_organigrama(self):
        from imprimir_organigrama import imprimir_organigrama
        self.ventana_abrir.close()
        self.ventana_imprimir_organigrama = QMainWindow()
        self.ui = imprimir_organigrama(self.ventana_imprimir_organigrama)
        self.ui.setupUi(self.ventana_imprimir_organigrama)
        self.ventana_imprimir_organigrama.show()

    #Abre la ventana de personales, seleccionada en el menu del lado izquierdo
    def abrir_ventana_personales(self):
        from Ingresar_Personales import personales
        self.ventana_abrir.close()
        self.ventana_personales = QMainWindow()
        self.ui = personales(self.ventana_personales)
        self.ui.setupUi(self.ventana_personales)
        self.ventana_personales.show()

    #Permite editar el organigrama,por el nombre y la fecha
    def editar_org(self):
        org_seleccionado = self.comboBox.currentText()
        nombres_organigramas = cargar_nombres_organigramas()  # Cargar listas organigramas
        codigo_org_buscar = self.comboBox.currentData()
        contador = 0
        for nombres in nombres_organigramas:
            cod_org = nombres[0]
            if codigo_org_buscar != cod_org:
                contador+=1
            else:
                self.codigo_org = codigo_org_buscar
                nombre_original = nombres[1]
                fecha_original = nombres[2]

                dialogo = EditarOrganigramaDialog(nombre_original, fecha_original)

                if dialogo.exec_() == QDialog.Accepted:
                    nuevo_nombre, nueva_fecha = dialogo.obtener_datos_editados()
                    if nuevo_nombre != "" and nueva_fecha != "":
                        organigrama = cargar_dependencia_organigrama(self.codigo_org)
                        organigrama.ORG=nuevo_nombre
                        guardar_dependencia_organigrama(self.codigo_org,organigrama)

                        organigramas = nombres_organigramas[contador]

                        organigramas[1] = nuevo_nombre
                        organigramas[2] = nueva_fecha
                        guardar_nombres_organigrama(nombres_organigramas) # Guardar la lista actualizada en el archivo
                        cargar_nombres_organigramas()  # Actualizar la lista en el combobox
                        self.cargar_organigramas()
                    else:
                        QMessageBox.warning(None, "Error", "No se puede dejar campos vacíos")

    #Permite copiar el organigrama y las dependencias de ese organigrama,cambiando el nombre y la fecha de la misma
    def copiar_organigrama(self):
        org_seleccionado = self.comboBox.currentText()
        nombres_organigramas = cargar_nombres_organigramas()  # Cargar listas organigramas
        codigo_org_buscar = self.comboBox.currentData()

        if codigo_org_buscar is not None:
            organigrama_copiado=cargar_dependencia_organigrama(codigo_org_buscar)
            nombre_original=organigrama_copiado.ORG
            fecha_original=organigrama_copiado.FEC
            dialogo = EditarOrganigramaDialog(nombre_original, fecha_original)

            if dialogo.exec_() == QDialog.Accepted:
                nuevo_nombre, nueva_fecha = dialogo.obtener_datos_editados()
                if nuevo_nombre != "" and nueva_fecha != "":
                    organigrama_copiado.COD=generar_codigo_ORG(nombres_organigramas)
                    organigrama_copiado.ORG=nuevo_nombre
                    nombres_organigramas.append([organigrama_copiado.COD,organigrama_copiado.ORG,nueva_fecha])
                    guardar_nombres_organigrama(nombres_organigramas)
                    guardar_dependencia_organigrama(organigrama_copiado.COD,organigrama_copiado)
                    self.cargar_organigramas()

    #Permite elimina el organigrama atravez de su codigo,y elimina tambien los archivos de la dependencia y personas
    def eliminar_organigrama(self):
        org_seleccionado = self.comboBox.currentText()
        nombres_organigramas = cargar_nombres_organigramas()  # Cargar listas organigramas
        codigo_org_buscar = self.comboBox.currentData()
        indice = 0
        for nombres in nombres_organigramas:
            if nombres[0] != codigo_org_buscar:
                indice += 1
            else:
                # Preguntar al usuario si está seguro de eliminar la dependencia
                confirmacion = QMessageBox.question(self.ventana_abrir, 'Confirmación',
                                                    f'¿Está seguro de eliminar la dependencia "{nombres[1]}"?',
                                                    QMessageBox.Ok | QMessageBox.Cancel)
                if confirmacion == QMessageBox.Ok:
                    nombres_organigramas.pop(indice)
                    guardar_nombres_organigrama(nombres_organigramas)
                    self.cargar_organigramas()
                    eliminar_archivo_organigrama(codigo_org_buscar)
                    eliminar_archivo_personas(codigo_org_buscar)

#Ventana de Dialogo para que permita ingresar un nuevo nombre y fecha para el organigrama cuando se quiere modificar o copiar el organigrama
class EditarOrganigramaDialog(QDialog):
    def __init__(self, nombre_actual, fecha_actual, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Organigrama")

        self.nombre_label = QLabel("Nombre:")
        self.nombre_edit = QLineEdit(nombre_actual)

        self.fecha_label = QLabel("Fecha:")
        self.fecha_edit = QLineEdit(fecha_actual)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_edit)
        layout.addWidget(self.fecha_label)
        layout.addWidget(self.fecha_edit)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def obtener_datos_editados(self):
        nuevo_nombre = self.nombre_edit.text().strip()
        nueva_fecha = self.fecha_edit.text().strip()
        return nuevo_nombre, nueva_fecha




