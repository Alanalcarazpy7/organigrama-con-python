from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from graphviz import Source
from Funciones_Dependencias import *


class Dependencias(object):
    def __init__(self, codigo_org, ventana_dependencia):
        super().__init__()
        self.MainWindow = None
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.codigo_org = codigo_org
        self.Organigrama_actual = cargar_dependencia_organigrama(self.codigo_org)
        self.personal = cargar_personas_organigrama(self.codigo_org)
        self.ventana_dependencia = ventana_dependencia
        self.proxy_model = QSortFilterProxyModel()
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.opcionesdep = QStackedWidget(self.centralwidget)
        self.opcionesdep.setObjectName(u"opcionesdep")
        self.opcionesdep.setMaximumSize(QSize(16777215, 300))
        self.opcionesdep.setStyleSheet(u"font-size:20px")
        self.Pag_agg = QWidget()
        self.Pag_agg.setObjectName(u"Pag_agg")
        self.gridLayout_4 = QGridLayout(self.Pag_agg)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.boton_confirmar = QPushButton(self.Pag_agg)
        self.boton_confirmar.setObjectName(u"boton_confirmar")
        self.boton_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_confirmar.setStyleSheet(u"QPushButton{font-size:20px;background-color:green;color:white}"
                                            "QPushButton:pressed { background-color: #004603; }"
                                            "QPushButton:checked { background-color: #004603; }")

        self.gridLayout_4.addWidget(self.boton_confirmar, 6, 2, 1, 1)

        self.label_6 = QLabel(self.Pag_agg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size:20px")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 3)

        self.Elegir_DPsup = QComboBox(self.Pag_agg)
        self.Elegir_DPsup.setObjectName(u"Elegir_DPsup")
        self.Elegir_DPsup.setStyleSheet(u"font-size:20px")

        self.gridLayout_4.addWidget(self.Elegir_DPsup, 3, 0, 1, 3)

        self.label_7 = QLabel(self.Pag_agg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size:20px")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 3)

        self.label_8 = QLabel(self.Pag_agg)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.Ingresar_nom_dep_crear = QLineEdit(self.Pag_agg)
        self.Ingresar_nom_dep_crear.setObjectName(u"Ingresar_nom_dep_crear")
        self.Ingresar_nom_dep_crear.setStyleSheet(u"font-size:20px")

        self.gridLayout_4.addWidget(self.Ingresar_nom_dep_crear, 1, 0, 1, 3)

        self.opcionesdep.addWidget(self.Pag_agg)
        self.Pag_edit = QWidget()
        self.Pag_edit.setObjectName(u"Pag_edit")
        self.gridLayout_3 = QGridLayout(self.Pag_edit)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.Pag_edit)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setStyleSheet(u"font-size:18px")

        self.gridLayout_3.addWidget(self.lineEdit, 6, 0, 1, 2)

        self.label_4 = QLabel(self.Pag_edit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:20px")

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

        self.boton_cambiar_nombre = QPushButton(self.Pag_edit)
        self.boton_cambiar_nombre.setObjectName(u"boton_cambiar_nombre")
        self.boton_cambiar_nombre.setMinimumSize(QSize(0, 30))
        self.boton_cambiar_nombre.setMaximumSize(QSize(550, 16777215))
        self.boton_cambiar_nombre.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_cambiar_nombre.setStyleSheet(u"QPushButton{font-size:20px;background-color:#0977A4;color:white}"
                                                "QPushButton:pressed { background-color: #003D57; }"
                                                "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_3.addWidget(self.boton_cambiar_nombre, 4, 1, 1, 1)

        self.label = QLabel(self.Pag_edit)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:20px")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.sel_dep_a_editar = QComboBox(self.Pag_edit)
        self.sel_dep_a_editar.setObjectName(u"sel_dep_a_editar")
        self.sel_dep_a_editar.setMinimumSize(QSize(0, 30))
        self.sel_dep_a_editar.setStyleSheet(u"font-size:20px")

        self.gridLayout_3.addWidget(self.sel_dep_a_editar, 1, 0, 1, 2)

        self.nuevo_jefe_CB = QComboBox(self.Pag_edit)
        self.nuevo_jefe_CB.setObjectName(u"nuevo_jefe_CB")
        self.nuevo_jefe_CB.setMinimumSize(QSize(0, 25))
        self.nuevo_jefe_CB.setStyleSheet(u"font-size:18px")

        self.gridLayout_3.addWidget(self.nuevo_jefe_CB, 7, 0, 1, 2)

        self.label_2 = QLabel(self.Pag_edit)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:20px")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.Pag_edit)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size:20px")

        self.gridLayout_3.addWidget(self.label_5, 9, 0, 1, 1)

        self.cedula_mostrada = QLabel(self.Pag_edit)
        self.cedula_mostrada.setObjectName(u"cedula_mostrada")
        self.cedula_mostrada.setStyleSheet(u"font-size:18px")

        self.gridLayout_3.addWidget(self.cedula_mostrada, 10, 0, 1, 1)

        self.lineanombre = QLineEdit(self.Pag_edit)
        self.lineanombre.setObjectName(u"lineanombre")
        self.lineanombre.setMinimumSize(QSize(0, 25))
        self.lineanombre.setStyleSheet(u"font-size:18px")

        self.gridLayout_3.addWidget(self.lineanombre, 3, 0, 1, 2)

        self.boton_act_jefe = QPushButton(self.Pag_edit)
        self.boton_act_jefe.setObjectName(u"boton_act_jefe")
        self.boton_act_jefe.setMinimumSize(QSize(200, 30))
        self.boton_act_jefe.setMaximumSize(QSize(600, 16777215))
        self.boton_act_jefe.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_act_jefe.setStyleSheet(u"QPushButton{font-size:20px;background-color:#0977A4;color:white}"
                                          "QPushButton:pressed { background-color: #003D57; }"
                                          "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_3.addWidget(self.boton_act_jefe, 9, 1, 1, 1)

        self.opcionesdep.addWidget(self.Pag_edit)
        self.label_2.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.cedula_mostrada.raise_()
        self.sel_dep_a_editar.raise_()
        self.lineanombre.raise_()
        self.nuevo_jefe_CB.raise_()
        self.lineEdit.raise_()
        self.boton_cambiar_nombre.raise_()
        self.boton_act_jefe.raise_()
        self.Pag_delete = QWidget()
        self.Pag_delete.setObjectName(u"Pag_delete")
        self.gridLayout_5 = QGridLayout(self.Pag_delete)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.Pag_delete)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.eliminarCB = QComboBox(self.Pag_delete)
        self.eliminarCB.setObjectName(u"comboBox")
        self.eliminarCB.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.eliminarCB, 1, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.Pag_delete)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{font-size:20px;background-color:#CB0808;color:white}"
                                        "QPushButton:pressed { background-color: #461700; }"
                                        "QPushButton:checked { background-color: #461700; }")


        self.gridLayout_5.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.label_11 = QLabel(self.Pag_delete)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)
        self.comboBox_2 = QComboBox(self.Pag_delete)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.comboBox_2, 4, 0, 1, 2)

        self.label_12 = QLabel(self.Pag_delete)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.label_12, 5, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.Pag_delete)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"font-size:20px")

        self.gridLayout_5.addWidget(self.comboBox_3, 6, 0, 1, 2)

        self.Button_move_D = QPushButton(self.Pag_delete)
        self.Button_move_D.setObjectName(u"Button_move_D")
        self.Button_move_D.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_move_D.setStyleSheet(u"QPushButton{font-size:20px;background-color:green;color:white}"
                                        "QPushButton:pressed { background-color: #004603; }"
                                        "QPushButton:checked { background-color: #004603; }")


        self.gridLayout_5.addWidget(self.Button_move_D, 7, 1, 1, 1)

        self.opcionesdep.addWidget(self.Pag_delete)

        self.verticalLayout_2.addWidget(self.opcionesdep)

        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 3)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font-size:20px")

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.Layout_graphicsel = QVBoxLayout()
        self.Layout_graphicsel.setObjectName(u"Layout_graphicsel")
        self.graphicselButton_D = QComboBox(self.centralwidget)
        self.graphicselButton_D.setObjectName(u"graphicselButton_D")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicselButton_D.sizePolicy().hasHeightForWidth())
        self.graphicselButton_D.setSizePolicy(sizePolicy)
        self.graphicselButton_D.setMinimumSize(QSize(0, 40))
        self.graphicselButton_D.setStyleSheet(u"font-size:20px")

        self.Layout_graphicsel.addWidget(self.graphicselButton_D)

        self.gridLayout.addLayout(self.Layout_graphicsel, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{font-size:20px;background-color:#0977A4;color:white}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_5, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 9, 0, 1, 1)

        self.CI_mostrado = QLabel(self.widget_2)
        self.CI_mostrado.setObjectName(u"CI_mostrado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CI_mostrado.sizePolicy().hasHeightForWidth())
        self.CI_mostrado.setSizePolicy(sizePolicy1)
        self.CI_mostrado.setMinimumSize(QSize(0, 0))
        self.CI_mostrado.setMaximumSize(QSize(250, 16777215))
        self.CI_mostrado.setAutoFillBackground(False)
        self.CI_mostrado.setStyleSheet(u"font-size:16px;width: 100px;height: 100px;")
        self.CI_mostrado.setFrameShape(QFrame.NoFrame)
        self.CI_mostrado.setFrameShadow(QFrame.Plain)
        self.CI_mostrado.setMidLineWidth(0)
        self.CI_mostrado.setTextFormat(Qt.AutoText)
        self.CI_mostrado.setScaledContents(True)
        self.CI_mostrado.setWordWrap(False)
        self.CI_mostrado.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.CI_mostrado, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 114, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{font-size:20px;background-color:#0977A4;color:white}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{font-size:20px;background-color:#0977A4;color:white}"
                                        "QPushButton:pressed { background-color: #003D57; }"
                                        "QPushButton:checked { background-color: #003D57; }")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.gridLayout.addLayout(self.verticalLayout_3, 3, 1, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_add_D = QPushButton(self.centralwidget)
        self.Button_add_D.setObjectName(u"Button_add_D")
        sizePolicy.setHeightForWidth(self.Button_add_D.sizePolicy().hasHeightForWidth())
        self.Button_add_D.setSizePolicy(sizePolicy)
        self.Button_add_D.setMinimumSize(QSize(0, 40))
        self.Button_add_D.setMaximumSize(QSize(16777215, 16777215))
        self.Button_add_D.setStyleSheet(u"QPushButton{font-size:20px;background-color:green;color:white}"
                                        "QPushButton:pressed { background-color: #004603; }"
                                        "QPushButton:checked { background-color: #004603; }")
        self.Button_add_D.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Button_add_D)

        self.Button_edit_D = QPushButton(self.centralwidget)
        self.Button_edit_D.setObjectName(u"Button_edit_D")
        sizePolicy.setHeightForWidth(self.Button_edit_D.sizePolicy().hasHeightForWidth())
        self.Button_edit_D.setSizePolicy(sizePolicy)
        self.Button_edit_D.setMinimumSize(QSize(0, 40))
        self.Button_edit_D.setStyleSheet(u"QPushButton{font-size:20px;background-color:#003049;color:white}"
                                         "QPushButton:pressed { background-color: #003D57; }"
                                         "QPushButton:checked { background-color: #003D57; }")
        self.Button_edit_D.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Button_edit_D)

        self.Button_delete_D = QPushButton(self.centralwidget)
        self.Button_delete_D.setObjectName(u"Button_delete_D")
        sizePolicy.setHeightForWidth(self.Button_delete_D.sizePolicy().hasHeightForWidth())
        self.Button_delete_D.setSizePolicy(sizePolicy)
        self.Button_delete_D.setMinimumSize(QSize(0, 40))
        self.Button_delete_D.setStyleSheet(u"QPushButton{font-size:20px;background-color:#461700;color:white}"
                                            "QPushButton:pressed { background-color: #461700; }"
                                            "QPushButton:checked { background-color: #461700; }")
        self.Button_delete_D.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Button_delete_D)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.textBrowser)

        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 2, 1)


        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        # Crear un layout horizontal
        self.layout = QHBoxLayout(self.pushButton_6)

        # Crear el QLabel para la imagen
        self.image_label = QLabel(self.pushButton_6)

        # Crear el QLabel para el texto
        self.text_label = QLabel()
        self.font = QFont()

        # Agregar los QLabel al layout
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.text_label)

        # Aplicar el estilo al QPushButton
        self.pushButton_6.setStyleSheet('''
            QPushButton {
                font-size: 20px;
                background-color: gray;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #0977A4;
            }

            QPushButton:pressed {
                background-color: #464646;
            }
        ''')

        self.layout.setSpacing(10)
        self.image_label.setStyleSheet("background-color: transparent;border-radius:35px")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(10, 0, 30, 0)
        self.text_label.setStyleSheet("background-color: transparent;")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.opcionesdep.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
        ############################################################
        self.boton_confirmar.setText("Confirmar")
        self.label_6.setText("Nombre de la dependencia")
        self.label_7.setText("Dependencia superior")
        self.label_8.setText("")
        self.lineEdit.setText("")
        self.label_4.setText("Jefe de Dependencia")
        self.boton_cambiar_nombre.setText("Modificar Nombre")
        self.label.setText("Nombre de Dependencia")
        self.label_2.setText("Dependencia a editar")
        self.label_5.setText("C.I.")
        self.cedula_mostrada.setText("")
        self.lineanombre.setText("")
        self.boton_act_jefe.setText("Actualizar Jefe")
        self.label_10.setText("Eliminar dependencia")
        self.pushButton_4.setText("Eliminar")
        self.label_11.setText("Mover dependencia")
        self.label_12.setText("Destino")
        self.Button_move_D.setText("Mover")
        self.label_14.setText("Dependencias a graficar")
        self.label_13.setText("")
        self.pushButton_5.setText("Ir al Menu Principal")
        self.CI_mostrado.setText(
            "<html><head/><body><p><img src=\"iconos/advertencia (1).png\"/> El Responsable se agregar\u00e1<br/>en la secci\u00f3n de Editar.</p></body></html>")
        self.pushButton_3.setText("Modificar Personal")
        self.label_9.setText("")
        self.pushButton_2.setText("Obtener Informes")
        self.Button_add_D.setText("añadir")
        self.Button_edit_D.setText("editar")
        self.Button_delete_D.setText("eliminar/mover")
        self.pushButton_6.setText("Cambiar de Color")
        ###########################################################################
        self.opcionesdep.setCurrentIndex(0)
        self.actualizar_nombre_mostrado()
        self.Button_add_D.clicked.connect(self.mostrar_pest_agregar)
        self.Button_edit_D.clicked.connect(self.mostrar_pest_editar)
        self.Button_delete_D.clicked.connect(self.mostrar_pest_eliminar)
        self.boton_cambiar_nombre.clicked.connect(self.editar_dependencia)
        self.boton_confirmar.clicked.connect(self.agg_dependencia)
        self.pushButton_4.clicked.connect(self.eliminar_dependencia)
        self.Button_move_D.clicked.connect(self.mover_destino)
        self.comboBox_2.currentIndexChanged.connect(self.obtener_destino)
        self.pushButton_2.clicked.connect(self.ventana_informes)

        self.graphicselButton_D.currentIndexChanged.connect(self.generar_grafo)
        self.lineEdit.setPlaceholderText("Buscar por nombre o apellido")
        self.pushButton_3.clicked.connect(self.ventana_personales)
        self.pushButton_5.clicked.connect(self.abrir_menu_principal)
        MainWindow.setWindowTitle(self.Organigrama_actual.ORG)
        self.cargar_conf_modo()
        self.pushButton_6.clicked.connect(self.modo_oscuro)
        self.aplicar_estilos()
        self.actualizar_lista_personas()
        self.nuevo_jefe_CB.model().sort(0, Qt.AscendingOrder)
        self.sel_dep_a_editar.currentIndexChanged.connect(self.actualizar_lista_personas)
        self.sel_dep_a_editar.currentIndexChanged.connect(self.mostrar_cedula)
        self.mostrar_cedula()
        self.nuevo_jefe_CB.currentIndexChanged.connect(self.mostrar_cedula)
        self.lineEdit.textChanged.connect(self.filtrar_lista_personas)
        self.boton_act_jefe.clicked.connect(self.cambiar_jefe)
        self.generar_grafo()
        ############################################################


    def mostrar_pest_agregar(self):
        self.opcionesdep.setCurrentIndex(0)
        self.Button_edit_D.setStyleSheet("font-size:20px;background-color:#003049;color:white")
        self.Button_delete_D.setStyleSheet("font-size:20px;background-color:#461700;color:white")
        self.Button_add_D.setStyleSheet("font-size:20px;background-color:green;color:white")


    def mostrar_pest_editar(self):
        self.opcionesdep.setCurrentIndex(1)
        self.Button_edit_D.setStyleSheet("font-size:20px;background-color:#0977A4;color:white")
        self.Button_delete_D.setStyleSheet("font-size:20px;background-color:#461700;color:white")
        self.Button_add_D.setStyleSheet("font-size:20px;background-color:#004603;color:white")


    def mostrar_pest_eliminar(self):
        self.opcionesdep.setCurrentIndex(2)
        self.Button_edit_D.setStyleSheet("font-size:20px;background-color:#003049;color:white")
        self.Button_delete_D.setStyleSheet("font-size:20px;background-color:#CB0808;color:white")
        self.Button_add_D.setStyleSheet("font-size:20px;background-color:#004603;color:white")


    # funcion para mostrar las listas de dependencias al usuario en los distintos combobox
    def actualizar_nombre_mostrado(self):
        try:
            file_path = os.path.join("archivos_organigramas", f'organigrama{self.codigo_org}_dependencias')
            with open(file_path, "rb") as archivo:
                organigrama = pickle.load(archivo)
                self.Organigrama_actual = organigrama
                matriz = matriz_nombre_codigo(self.Organigrama_actual.raiz, [])
        except FileNotFoundError:
            matriz = []
        # Limpiar y Colocar cada menu desplegable
        self.eliminarCB.clear()
        self.Elegir_DPsup.clear()
        self.sel_dep_a_editar.clear()
        self.comboBox_2.clear()
        self.graphicselButton_D.clear()
        for k in range(len(matriz)):
            self.sel_dep_a_editar.addItem(matriz[k][0], matriz[k][1])
            self.Elegir_DPsup.addItem(matriz[k][0], matriz[k][1])
            self.eliminarCB.addItem(matriz[k][0], matriz[k][1])
            self.comboBox_2.addItem(matriz[k][0], matriz[k][1])
            self.graphicselButton_D.addItem(matriz[k][0], matriz[k][1])

    # Funcion para colocar en la parte de editar una lista desplegable que permita seleccionar alguna opcion
    def editar_dependencia(self):
        cambio = False
        nueva_dependencia = self.lineanombre.text()
        obtener_dependencia = self.sel_dep_a_editar.currentData()
        if obtener_dependencia is not None:
            if nueva_dependencia != "":
                if self.sel_dep_a_editar.currentText() != nueva_dependencia:
                    cambio = True
                    dep_modificada = self.sel_dep_a_editar.currentText()
                    if obtener_dependencia != nueva_dependencia:
                        nueva_dependencia = modificar_nombre_dep(self.Organigrama_actual.raiz, obtener_dependencia,
                                                                 nueva_dependencia, self.codigo_org)
                guardar_dependencia_organigrama(self.codigo_org, self.Organigrama_actual)

                self.lineanombre.clear()
            else:
                QMessageBox.warning(self.MainWindow, "Error", "No se puede ingresar Dependencias vacías")
        else:
            QMessageBox.warning(self.MainWindow, "Error", "Se debe seleccionar alguna Dependencia")
        if cambio:
            if self.personal is not None:
                for personal in self.personal:
                    if personal[6] == dep_modificada:
                        personal[6] = nueva_dependencia
            guardar_personas_organigrama(self.codigo_org, self.personal)
        self.actualizar_nombre_mostrado()

    #Permite cargar los personales mediante su codigo del organigrama
    def cargar_personales(self):
        try:
            file_path = os.path.join("archivos_personas", f'organigrama{self.codigo_org}_personas')
            with open(file_path, 'rb') as archivo:
                nombres = pickle.load(archivo)
            return nombres
        except FileNotFoundError:
            nombres = []
            return nombres

    #Permite añadir las dependencias y luego guardarlas en un archivo
    def agg_dependencia(self):
        texto = self.Ingresar_nom_dep_crear.text()
        cod_sup = self.Elegir_DPsup.currentData()
        codigo_aleatorio = generar_codigo_dep(self.Organigrama_actual.raiz)
        if texto != "":
            self.Organigrama_actual.agregar_dependencia(codigo_aleatorio, cod_sup, texto, None)
            guardar_dependencia_organigrama(self.codigo_org, self.Organigrama_actual)
            self.actualizar_nombre_mostrado()
            # Limpiar lo que se ingreso
            self.Ingresar_nom_dep_crear.clear()
        else:
            QMessageBox.warning(self.MainWindow, "Error", "No se puede ingresar Dependencias vacías")

    #Permite eliminar las dependencias y todos los nodos sucesores
    def eliminar_dependencia(self):
        # Obtener la dependencia seleccionado en el menu de eliminar
        obtener_dependencia = self.eliminarCB.currentText()

        if obtener_dependencia != "":
            # Preguntar al usuario si está seguro de eliminar la dependencia
            confirmacion = QMessageBox.question(self.opcionesdep, 'Confirmación',
                                                f'¿Está seguro de eliminar la dependencia "{obtener_dependencia}"?',
                                                QMessageBox.Ok | QMessageBox.Cancel)
            if confirmacion == QMessageBox.Ok:
                cod_obtenido = self.eliminarCB.currentData()
                lista_subs = enlistar_cod_nodo(self.Organigrama_actual.raiz, self.eliminarCB.currentData(), [])
                self.Organigrama_actual.eliminar_dependencia(cod_obtenido)
                if self.personal is not None:
                    for personal in self.personal:
                        if personal[8] in lista_subs:
                            personal[6] = ""
                            personal[8] = None
                guardar_personas_organigrama(self.codigo_org, self.personal)
                guardar_dependencia_organigrama(self.codigo_org, self.Organigrama_actual)
                self.actualizar_nombre_mostrado()
        else:
            QMessageBox.warning(self.MainWindow, "Error", "Se debe seleccionar alguna Dependencia")

    #Al seleccionar alguna dependencia que se quiere mover,en el otro combobox se imprimira las dependencias disponibles a la cual se puede mover
    def obtener_destino(self):
        cod_mover = self.comboBox_2.currentData()
        superiores_disp = superiores_disponibles(self.Organigrama_actual.raiz, cod_mover)
        self.comboBox_3.clear()
        if not superiores_disp:
            self.comboBox_3.addItem("No se puede mover", None)
        else:
            for dependencia in superiores_disp:
                self.comboBox_3.addItem(dependencia[0], dependencia[1])

    #Permite mover las dependencias y todos los nodos sucesores
    def mover_destino(self):
        dep_mover = self.comboBox_2.currentText()
        dep_destino = self.comboBox_3.currentText()
        if dep_mover != "" and dep_destino != "":
            cod_mover = self.comboBox_2.currentData()
            cod_destino = self.comboBox_3.currentData()
            mover_dependencia(self.Organigrama_actual.raiz, cod_mover, cod_destino)
            guardar_dependencia_organigrama(self.codigo_org, self.Organigrama_actual)
            self.generar_grafo()
        else:
            QMessageBox.warning(self.MainWindow, "Error", "Se debe seleccionar alguna Dependencia")

    #Genera el grafo mediante el modulo de graphviz
    def generar_grafo(self):
        dep_mostrar = self.graphicselButton_D.currentText()
        cod_mostrar = self.graphicselButton_D.currentData()
        listas = gen_lista_grafica(cod_mostrar, self.Organigrama_actual.raiz, self.personal)
        jefe = obtener_jefe(self.Organigrama_actual.raiz, cod_mostrar, self.personal)

        if jefe == "":
            jefe = "(No asignado)"
        jefe = '\n' + jefe
        if self.es_modo_oscuro:
            flecha_color = "white"
            fondo_color = "#333333"
        else:
            flecha_color = "black"
            fondo_color = "white"

        contenido = [
            'digraph G {',
            '    node [shape=rectangle style=filled fontname="Helvetica" fontsize=14 width=1.5 height=0.6 penwidth=1.5 fillcolor="#948F8F" fontcolor=white];',
            f'    edge [penwidth=1.5 arrowhead=none arrowsize=1.5 color="{flecha_color}" dir=forward];',
            # Estilos de la Flecha
            f'    graph [splines=true overlap=false bgcolor="{fondo_color}"];',
        ]

        # Al editar dependencia me sale un error de None por eso coloco esto
        if listas is not None:
            lista1 = listas[0]
            lista2 = listas[1]

            # En el caso de que no exista nigun nodo inferior,estas condiciones sirven para que muestre en pantalla el unico nodo existente
            if lista1 or dep_mostrar == "":
                for i in range(len(lista1)):
                    concatenar = f'"{lista1[i]}" -> "{lista2[i]}";'  # "Departamento de Recursos Humanos" -> "Gerente de Recursos Humanos" Asi debe imprimir por eso hago esto,para que sepa donde poner la flecha al graficar
                    contenido.append(concatenar)

            else:
                concatenar = dep_mostrar  # "Departamento de Recursos Humanos" -> "Gerente de Recursos Humanos" Asi debe imprimir por eso hago esto,para que sepa donde poner la flecha al graficar
                contenido.append(f'"{concatenar+jefe}"')
            contenido.append("}")

            # Guarda la lista como un archivo de texto
            with open("grafo.txt", "w") as f:
                f.write('\n'.join(contenido))

            # Lee el archivo de texto con la definiciÃ³n del grafo
            with open("grafo.txt", "r") as f:
                contenido = f.read()

            # Genera el grafo a partir del archivo de texto
            grafo = Source(contenido, format="png")

            # Guarda el grafo como un archivo de imagen(imprime como png)
            grafo.render("grafo", view=False)
            pixmap = QPixmap("grafo.png")

            # Imprimir en el textBrowser
            self.textBrowser.setText(f"Organigrama generado.")

            # limpia el contenido anterior del textBrowser
            self.textBrowser.clear()
            # Agrega la imagen al textBrowser
            self.textBrowser.insertHtml(
                '<center style="display: flex; justify-content: center;"><img src="grafo.png"></center>')
            return pixmap

    #Funcion para actualizar las personas en el combobox y permitir elejir los jefes atravez de esta lista
    def actualizar_lista_personas(self):
        self.nuevo_jefe_CB.clear()
        if self.personal:
            for persona in self.personal:
                if persona[6] == self.sel_dep_a_editar.currentText():
                    self.nuevo_jefe_CB.addItem(persona[0] + " " + persona[1], persona[2])
        self.nuevo_jefe_CB.model().sort(0, Qt.AscendingOrder)

    #Permite cambiar el jefe de una dependencia
    def cambiar_jefe(self):
        nuevojefe_CI = self.nuevo_jefe_CB.currentData()
        dep_modificada_COD = self.sel_dep_a_editar.currentData()
        if nuevojefe_CI != "" and dep_modificada_COD is not None:
            cambiar_jefe_dep(self.Organigrama_actual.raiz, dep_modificada_COD, nuevojefe_CI)
        guardar_dependencia_organigrama(self.codigo_org, self.Organigrama_actual)
        self.generar_grafo()

    #Permite filtrar la lista de personas por nombre y apellido para seleccionar el jefe
    def filtrar_lista_personas(self):
        Filtro = self.lineEdit.text().lower()
        if Filtro == "":
            self.actualizar_lista_personas()
        else:
            self.nuevo_jefe_CB.clear()
            if self.personal:
                for persona in self.personal:
                    if persona[6] == self.sel_dep_a_editar.currentText():
                        nombre_apellido = (persona[0] + " " + persona[1]).lower()
                        if nombre_apellido.find(Filtro) != -1:
                            self.nuevo_jefe_CB.addItem(persona[0] + " " + persona[1], persona[2])
            self.nuevo_jefe_CB.model().sort(0, Qt.AscendingOrder)

    #Permite mostrar la cedula de la persona seleccionada en la seccion de editar jefe
    def mostrar_cedula(self):
        texto_cb_personas = self.nuevo_jefe_CB.currentText()
        if texto_cb_personas == "":
            self.cedula_mostrada.setText("No encontrado")
        else:
            self.cedula_mostrada.setText(self.nuevo_jefe_CB.currentData())

    def ventana_personales(self):
        from Personales import personales
        self.ventana_dependencia.close()
        self.ventana_abrir_organigrama = QMainWindow()
        self.ui = personales(self.codigo_org, self.ventana_abrir_organigrama)
        self.ui.setupUi(self.ventana_abrir_organigrama)
        self.ventana_abrir_organigrama.show()

    def abrir_menu_principal(self):
        from Menu_Principal import menu_principal
        self.ventana_dependencia.close()
        self.ventana_abrir_menu = QMainWindow()
        self.ui = menu_principal(self.ventana_abrir_menu)
        self.ui.setupUi(self.ventana_abrir_menu)
        self.ventana_abrir_menu.show()

    def ventana_informes(self):
        from mostrar_informes import Ui_Informes
        self.ventana_dependencia.close()
        self.ventana_abrir_informes = QMainWindow()
        self.ui = Ui_Informes(self.codigo_org,self.ventana_abrir_informes)
        self.ui.setupUi(self.ventana_abrir_informes)
        self.ventana_abrir_informes.show()

    #Funcion para colocar modo oscuro a la interfaz
    def modo_oscuro(self):
        print(self.es_modo_oscuro)
        self.es_modo_oscuro = not self.es_modo_oscuro
        self.aplicar_estilos()
        self.guardar_conf()

    #Aplica los estilos para el modo oscuro o modo claro
    def aplicar_estilos(self):
        self.generar_grafo()
        if self.es_modo_oscuro:
            self.centralwidget.setStyleSheet("background-color: #333333; color: #ffffff;")
            self.pushButton_6.setText("")
            self.image_label.setPixmap(QPixmap(
                "iconos/modo-de-luz.png"))
            self.font.setPointSize(15)
            self.text_label.setText("Claro")
            self.text_label.setFont(self.font)

        else:
            self.centralwidget.setStyleSheet("background-color: #ffffff; color: #333333;")
            self.pushButton_6.setText("")
            self.image_label.setPixmap(QPixmap(
                "iconos/luna (1).png"))
            self.font.setPointSize(15)
            self.text_label.setText("Oscuro")
            self.text_label.setFont(self.font)

        # Cambiar el color del texto según el fondo
        palette = self.pushButton_6.palette()
        if self.es_modo_oscuro:
            palette.setColor(self.pushButton_6.foregroundRole(), Qt.white)
            palette.setColor(self.centralwidget.foregroundRole(), Qt.white)
        else:
            palette.setColor(self.pushButton_6.foregroundRole(), Qt.black)
        self.pushButton_6.setPalette(palette)

    #Se carga la configuracion del modo claro o oscuro
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

    #Se guarda en un archivo la configuracion del modo claro/oscuro para cuando se vuelva a ingresar,siga estando ese modo seleccionado
    def guardar_conf(self):
        with open("modo_claro_oscuro_conf", "wb") as f:
            pickle.dump([self.es_modo_oscuro], f)


