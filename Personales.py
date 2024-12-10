import os
from random import randint
from entrada import Formulario
import pickle
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QAbstractItemView, QComboBox
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class personales(object):
    def __init__(self, codigo_org, ventana_personales):
        super().__init__()
        self.formulario = Formulario(codigo_org)
        self.nombres = []
        self.datos = []
        self.apellidos = []
        self.salarios = []
        self.deps = []
        self.CI = []
        self.numeros = []
        self.direcciones = []
        self.dependencias = []
        self.lista1 = []
        self.lista2 = []
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.codigo_org = codigo_org
        self.ventana_personales = ventana_personales

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalFrame_5 = QFrame(self.centralwidget)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setStyleSheet(u"background-color:#244434")
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.verticalFrame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(100000, 100000))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"font-size:80px;color:white;text-align:center;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.verticalLayout_3.addWidget(self.verticalFrame_5)

        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(1000, 0))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalWidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.horizontalWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color:#0887ac")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.vista_personas = QTableWidget(self.horizontalWidget)
        if (self.vista_personas.columnCount() < 7):
            self.vista_personas.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.vista_personas.setObjectName(u"vista_personas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vista_personas.sizePolicy().hasHeightForWidth())
        self.vista_personas.setSizePolicy(sizePolicy1)
        self.vista_personas.setMinimumSize(QSize(0, 200))
        self.vista_personas.setMaximumSize(QSize(632, 1999))
        self.vista_personas.setSizeIncrement(QSize(100, 0))
        self.vista_personas.setStyleSheet(
            u"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));qproperty-defaultAlignment: 'AlignHCenter';\n"
            "")
        self.vista_personas.setSortingEnabled(False)
        self.vista_personas.horizontalHeader().setMinimumSectionSize(39)
        self.vista_personas.horizontalHeader().setDefaultSectionSize(90)
        self.vista_personas.verticalHeader().setCascadingSectionResizes(False)

        # Deshabilitar edición
        self.vista_personas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.columna = self.vista_personas.horizontalHeader()
        self.fila = self.vista_personas.verticalHeader()

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.vista_personas.setDragDropOverwriteMode(False)
        self.vista_personas.setColumnCount(9)
        self.vista_personas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.vista_personas.setHorizontalHeaderItem(8, item)
        self.horizontalLayout.addWidget(self.vista_personas)

        self.horizontalLayout_3.addWidget(self.vista_personas)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.boton_agregar = QPushButton(self.horizontalWidget)
        self.boton_agregar.setObjectName(u"boton_agregar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.boton_agregar.sizePolicy().hasHeightForWidth())
        self.boton_agregar.setSizePolicy(sizePolicy2)
        self.boton_agregar.setMinimumSize(QSize(100, 70))
        self.boton_agregar.setMaximumSize(QSize(300, 16777215))
        self.boton_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_agregar.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.verticalLayout.addWidget(self.boton_agregar)

        self.boton_filtrar = QPushButton(self.horizontalWidget)
        self.boton_filtrar.setObjectName(u"boton_filtrar")
        sizePolicy2.setHeightForWidth(self.boton_filtrar.sizePolicy().hasHeightForWidth())
        self.boton_filtrar.setSizePolicy(sizePolicy2)
        self.boton_filtrar.setMinimumSize(QSize(100, 70))
        self.boton_filtrar.setMaximumSize(QSize(300, 16777215))
        self.boton_filtrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_filtrar.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.verticalLayout.addWidget(self.boton_filtrar)

        self.boton_editar = QPushButton(self.horizontalWidget)
        self.boton_editar.setObjectName(u"boton_editar")
        sizePolicy2.setHeightForWidth(self.boton_editar.sizePolicy().hasHeightForWidth())
        self.boton_editar.setSizePolicy(sizePolicy2)
        self.boton_editar.setMinimumSize(QSize(100, 70))
        self.boton_editar.setMaximumSize(QSize(300, 16777215))
        self.boton_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_editar.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.verticalLayout.addWidget(self.boton_editar)

        self.boton_eliminar = QPushButton(self.horizontalWidget)
        self.boton_eliminar.setObjectName(u"boton_eliminar")
        sizePolicy2.setHeightForWidth(self.boton_eliminar.sizePolicy().hasHeightForWidth())
        self.boton_eliminar.setSizePolicy(sizePolicy2)
        self.boton_eliminar.setMinimumSize(QSize(100, 70))
        self.boton_eliminar.setMaximumSize(QSize(300, 16777215))
        self.boton_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_eliminar.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.verticalLayout.addWidget(self.boton_eliminar)

        self.boton_mostrar = QPushButton(self.horizontalWidget)
        self.boton_mostrar.setObjectName(u"boton_mostrar")
        sizePolicy2.setHeightForWidth(self.boton_mostrar.sizePolicy().hasHeightForWidth())
        self.boton_mostrar.setSizePolicy(sizePolicy2)
        self.boton_mostrar.setMinimumSize(QSize(100, 70))
        self.boton_mostrar.setMaximumSize(QSize(300, 16777215))
        self.boton_mostrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_mostrar.setStyleSheet(u"QPushButton {font-size:20px;background-color:#0977A4;color:white;}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.verticalLayout.addWidget(self.boton_mostrar)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_3.addWidget(self.horizontalWidget)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

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
                           }
                       ''')

        layout.setSpacing(0)
        self.image_label.setStyleSheet("background-color: transparent;border-radius:35px")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(10, 0, 35, 0)
        self.text_label.setStyleSheet("background-color: transparent;")


        #########################################################
        self.boton_eliminar.clicked.connect(self.eliminar_personas)
        self.formulario.btn_enviar.clicked.connect(self.guardarTexto)
        self.boton_editar.clicked.connect(self.modificar_persona)
        self.boton_agregar.clicked.connect(self.conectar)
        self.boton_filtrar.clicked.connect(self.filtrar_campo)
        self.boton_mostrar.clicked.connect(self.mostrar_elementos)
        self.pushButton_5.clicked.connect(self.abrir_menu_principal)
        self.pushButton_2.clicked.connect(self.ventana_dependencia)

        self.cargar_conf_modo()
        self.pushButton_3.clicked.connect(self.modo_oscuro)
        self.aplicar_estilos()
        self.mostrar_personas_guardadas()
        #########################################################

        MainWindow.setWindowTitle("Personales")
        self.label_14.setText("Registro de Usuario")
        self.pushButton_2.setText("Ir a Dependencias")
        self.pushButton_5.setText("Ir al Menu Principal")
        self.boton_agregar.setText("Agregar")
        self.boton_eliminar.setText("Eliminar")
        self.boton_editar.setText("Editar")
        self.boton_filtrar.setText("Filtrar")
        self.boton_mostrar.setText("Mostrar")
        item = self.vista_personas.horizontalHeaderItem(0)
        item.setText("Nombres")
        item = self.vista_personas.horizontalHeaderItem(1)
        item.setText("Apellidos")
        item = self.vista_personas.horizontalHeaderItem(2)
        item.setText("C.I")
        item = self.vista_personas.horizontalHeaderItem(3)
        item.setText("Salario")
        item = self.vista_personas.horizontalHeaderItem(4)
        item.setText("Direccion")
        item = self.vista_personas.horizontalHeaderItem(5)
        item.setText("Numero")
        item = self.vista_personas.horizontalHeaderItem(6)
        item.setText("Dependencia")
        item = self.vista_personas.horizontalHeaderItem(7)
        item.setText("per_cod")
        item = self.vista_personas.horizontalHeaderItem(8)
        item.setText("dep_cod")
        self.vista_personas.setColumnHidden(7, True)
        self.vista_personas.setColumnHidden(8, True)

    def conectar(self):
        self.formulario.show()

    def guardarTexto(self):
        nombre = self.formulario.getName()
        apellido = self.formulario.getApe()
        CI = self.formulario.getCI()
        sal = self.formulario.get_salario()
        dir = self.formulario.get_direccion()
        num = self.formulario.get_numero()
        deps = self.formulario.text_dependencia.currentText()
        dep_cod = self.formulario.text_dependencia.currentData()
        per_cod = self.generar_cod_persona()
        self.guardar_listas_nombres(nombre, apellido, CI, sal, dir, num, deps, per_cod, dep_cod)
        self.agregar_persona_tabla(nombre, apellido, CI, sal, dir, num, deps, per_cod, dep_cod)

    def agregar_persona_tabla(self, nombre, apellido, CI, salario, direccion, numero, deps, per_cod, dep_cod):
        row_count = self.vista_personas.rowCount()
        self.vista_personas.insertRow(row_count)
        item = QtWidgets.QTableWidgetItem(nombre.title())
        item_ape = QtWidgets.QTableWidgetItem(apellido.title())
        item_CI = QtWidgets.QTableWidgetItem(CI)
        item_sal = QtWidgets.QTableWidgetItem(salario)
        item_dir = QtWidgets.QTableWidgetItem(direccion)
        item_num = QtWidgets.QTableWidgetItem(numero)
        item_deps = QtWidgets.QTableWidgetItem(deps)
        item_per_cod = QtWidgets.QTableWidgetItem(per_cod)
        item_dep_cod = QtWidgets.QTableWidgetItem(dep_cod)
        self.vista_personas.setItem(row_count, 0, item)
        self.vista_personas.setItem(row_count, 1, item_ape)
        self.vista_personas.setItem(row_count, 2, item_CI)
        self.vista_personas.setItem(row_count, 3, item_sal)
        self.vista_personas.setItem(row_count, 4, item_dir)
        self.vista_personas.setItem(row_count, 5, item_num)
        self.vista_personas.setItem(row_count, 6, item_deps)
        self.vista_personas.setItem(row_count, 7, item_per_cod)
        self.vista_personas.setItem(row_count, 8, item_dep_cod)

    def guardar_listas_nombres(self, nombre, apellido, CI, sal, dir, num, deps, per_cod, dep_cod):
        try:
            self.file_path = os.path.join("archivos_personas", f'organigrama{self.codigo_org}_personas')
            with open(self.file_path, 'rb') as archivo:
                self.datos = pickle.load(archivo)
        except FileNotFoundError:
            self.datos = []  # Inicializar como una lista vacía si el archivo no existe
        if self.datos is None:
            self.datos = []
        # Crear una lista llamada "fila" con los datos
        fila = [nombre.title(), apellido.title(), CI, sal, dir, num, deps, per_cod, dep_cod]
        self.datos.append(fila)  # Agregar la fila a la matriz

        file_path = os.path.join("archivos_personas", f'organigrama{self.codigo_org}_personas')
        # Verificar si la carpeta "archivos_personas" existe, de lo contrario, crearla
        if not os.path.exists("archivos_personas"):
            os.makedirs("archivos_personas")

        # Guardar la matriz en el archivo
        with open(file_path, "wb") as datos2:
            pickle.dump(self.datos, datos2)

        with open(file_path, 'ab') as archivo:
            pickle.dump(self.datos, archivo)

    def mostrar_personas_guardadas(self):
        try:
            self.file_path = os.path.join("archivos_personas", f'organigrama{self.codigo_org}_personas')
            with open(self.file_path, "rb") as cargar_datos:
                self.datos = pickle.load(cargar_datos)
        except FileNotFoundError:
            pass
        if self.datos is None:
            self.datos = []
        self.vista_personas.setRowCount(len(self.datos))

        for i, persona in enumerate(self.datos):
            for j, dato in enumerate(persona):
                item = QtWidgets.QTableWidgetItem(str(dato))  # Convertir el elemento individual a cadena
                self.vista_personas.setItem(i, j, item)

    def eliminar_personas(self):
        cantidad_filas = self.vista_personas.rowCount()
        fila_seleccionada = self.vista_personas.currentRow()

        if cantidad_filas != 0:
            if fila_seleccionada >= 0:
                # Obtener el texto de la celda en la columna deseada (por ejemplo, la primera columna)
                dependencia_lista = self.vista_personas.item(fila_seleccionada, 0).text()

                # Mostrar un cuadro de diálogo de confirmación
                respuesta = QMessageBox.question(None, "Confirmar Eliminación",
                                                 f"¿Estás seguro de que deseas eliminar la fila {fila_seleccionada + 1}?",
                                                 QMessageBox.Yes | QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    # Eliminar la fila correspondiente al índice seleccionado del QTableWidget
                    self.vista_personas.removeRow(fila_seleccionada)

                    # Eliminar la dependencia de la lista
                    try:
                        with open(self.file_path, "rb") as cargar_datos:
                            self.datos = pickle.load(cargar_datos)
                    except FileNotFoundError:
                        self.datos = []
                    try:
                        del self.datos[fila_seleccionada]  # La función `del` elimina un elemento de una lista
                    except ValueError:
                        pass

                    with open(self.file_path, "wb") as datoPersona:
                        pickle.dump(self.datos, datoPersona)
                else:
                    # El usuario canceló la eliminación
                    pass
            else:
                QMessageBox.critical(None, "ERROR", "No ha seleccionado una fila")
        else:
            QMessageBox.critical(None, "ERROR", "No hay filas para eliminar")

    def modificar_persona(self):
        # Obtener la fila seleccionada en el QTableWidget
        row = self.vista_personas.currentRow()
        column = self.vista_personas.currentColumn()

        if row >= 0:
            if column == 6:
                # Obtener el texto de la celda seleccionada
                texto = self.vista_personas.item(row, column).text()

                # Crear el combobox y establecer el valor actual
                combobox = QComboBox()
                for dependencia in self.formulario.name_deps:
                    combobox.addItem(dependencia[0], dependencia[1])
                # Crear el diálogo del combobox
                dialog = QtWidgets.QDialog()
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(combobox)

                # Agregar un botón de aceptar al diálogo
                button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
                layout.addWidget(button_box)

                dialog.setLayout(layout)

                # Conectar la señal de aceptar del botón al cierre del diálogo
                button_box.accepted.connect(dialog.accept)

                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                    # Obtener el nuevo texto seleccionado del combobox
                    nuevo_texto = combobox.currentText()
                    nuevo_cod = combobox.currentData()
                    # Actualizar el valor en la celda correspondiente
                    item = QtWidgets.QTableWidgetItem(nuevo_texto)
                    itemcod = QtWidgets.QTableWidgetItem(nuevo_cod)
                    self.vista_personas.setItem(row, column, item)
                    self.vista_personas.setItem(row, column + 2, itemcod)

                    # Actualizar la lista de personas
                    self.datos = []
                    for i in range(self.vista_personas.rowCount()):
                        fila = []
                        for j in range(self.vista_personas.columnCount()):
                            item = self.vista_personas.item(i, j)
                            if item is not None:
                                fila.append(item.text())

                        self.datos.append(fila)

                    # Guardar los cambios en el archivo
                    with open(self.file_path, "wb") as archivo:
                        pickle.dump(self.datos, archivo)
            else:
                # Obtener el texto de la celda seleccionada
                texto = self.vista_personas.item(row, column).text()

                nuevo_texto, ok = QtWidgets.QInputDialog.getText(self.vista_personas, "Modificar Persona",
                                                                 "Introduce el nuevo texto:", text=texto)

                if ok and nuevo_texto:
                    # Actualizar el valor en la celda correspondiente
                    item = QtWidgets.QTableWidgetItem(nuevo_texto.title())
                    self.vista_personas.setItem(row, column, item)

                    # Actualizar la lista de personas
                    self.datos = []
                    for i in range(self.vista_personas.rowCount()):
                        fila = []
                        for j in range(self.vista_personas.columnCount()):
                            item = self.vista_personas.item(i, j)
                            if item is not None:
                                fila.append(item.text())
                        self.datos.append(fila)

                    # Guardar los cambios en el archivo
                    with open(self.file_path, "wb") as archivo:
                        pickle.dump(self.datos, archivo)

    def filtrar_campo(self):
        """
        nuevo_texto, ok = QInputDialog.getText(self.vista_personas, "Filtrar Dependencia",
                                               "Seleccione una dependencia:")
        if ok and nuevo_texto:
            for row in range(self.vista_personas.rowCount()):
                hidden = all(nuevo_texto not in self.vista_personas.item(row, 6).text() for column in
                             range(self.vista_personas.columnCount()))
                self.vista_personas.setRowHidden(row, hidden)
        """
        # Crear el combobox y establecer el valor actual
        combobox = QComboBox()
        for dependencia in self.formulario.name_deps:
            combobox.addItem(dependencia[0], dependencia[1])
        # Crear el diálogo del combobox
        dialog = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(combobox)

        # Agregar un botón de aceptar al diálogo
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        layout.addWidget(button_box)

        dialog.setLayout(layout)

        # Conectar la señal de aceptar del botón al cierre del diálogo
        button_box.accepted.connect(dialog.accept)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            nuevo_texto=combobox.currentText()
            print(nuevo_texto)
            for row in range(self.vista_personas.rowCount()):
                hidden = all(nuevo_texto not in self.vista_personas.item(row, 6).text() for column in
                             range(self.vista_personas.columnCount()))
                self.vista_personas.setRowHidden(row, hidden)
        # Obtener el nuevo texto seleccionado del combobox

    def mostrar_elementos(self):
        for row in range(self.vista_personas.rowCount()):
            self.vista_personas.setRowHidden(row, False)

            ##asignar dependencias
    def generar_cod_persona(self):
        lista_codigos = []
        encontrado = 0
        for persona in self.datos:
            lista_codigos.append(persona)
        while encontrado == 0:
            codigo_aleatorio = randint(0, 999)
            if codigo_aleatorio not in lista_codigos:
                encontrado = 1
        codigo_aleatorio = str(codigo_aleatorio)
        while len(codigo_aleatorio) < 3:
            codigo_aleatorio = "0" + codigo_aleatorio
        return codigo_aleatorio

    def modo_oscuro(self):
        self.es_modo_oscuro = not self.es_modo_oscuro
        self.aplicar_estilos()
        self.guardar_conf()

    def aplicar_estilos(self):
        if self.es_modo_oscuro:
            self.centralwidget.setStyleSheet("background-color: #333333; color: #ffffff;")
            self.pushButton_3.setText("")
            self.columna.setStyleSheet("::section{background-color: #333333;}")
            self.fila.setStyleSheet("::section{background-color: #333333;}")
            self.image_label.setPixmap(QPixmap(
                "iconos/modo-de-luz.png"))
            self.font.setPointSize(15)
            self.text_label.setText("Claro")
            self.text_label.setFont(self.font)

        else:
            self.centralwidget.setStyleSheet("background-color: #ffffff; color: #333333;")
            self.columna.setStyleSheet("::section{background-color: #ffffff;}")
            self.fila.setStyleSheet("::section{background-color: #ffffff;}")
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

    def ventana_dependencia(self):
        from Crear_Dependencias import Dependencias
        self.ventana_personales.close()
        self.ventana_crear_dependencia = QMainWindow()
        self.ui = Dependencias(self.codigo_org, self.ventana_crear_dependencia)
        self.ui.setupUi(self.ventana_crear_dependencia)
        self.ventana_crear_dependencia.show()
        self.ui.generar_grafo()

    def abrir_menu_principal(self):
        from Menu_Principal import menu_principal
        self.ventana_personales.close()
        self.ventana_abrir_menu = QMainWindow()
        self.ui = menu_principal(self.ventana_abrir_menu)
        self.ui.setupUi(self.ventana_abrir_menu)
        self.ventana_abrir_menu.show()


    def guardar_conf(self):
        with open("modo_claro_oscuro_conf", "wb") as f:
            pickle.dump([self.es_modo_oscuro], f)

