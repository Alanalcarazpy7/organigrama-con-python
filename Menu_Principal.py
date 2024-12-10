from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class menu_principal(object):
    def __init__(self,ventana_menu_principal):
        self.ventana_menu_principal=ventana_menu_principal
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
        self.gridWidget = QWidget(self.horizontalFrame)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setMinimumSize(QSize(200, 200))
        self.gridWidget.setMaximumSize(QSize(330, 330))
        self.gridWidget.setStyleSheet(u"image: url(iconos/logotipo-de-python-language.png);")



        self.verticalLayout_5.addWidget(self.gridWidget, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.horizontalFrame)

        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(400, 400))
        self.label_10.setStyleSheet(u"font-size:45px;\n")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(140, 140))
        self.pushButton_7.setMaximumSize(QSize(400, 400))
        self.pushButton_7.setStyleSheet(u"QPushButton{image: url(iconos/carpeta-abierta.png);}"
                                        "QPushButton:pressed { background-color: #525252; }"
                                        "QPushButton:checked { background-color: #525252; }")

        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_7, 0, 2, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(400, 400))
        self.label_13.setStyleSheet(u"font-size:45px;\n")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 1, 2, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(140, 140))
        self.pushButton_5.setMaximumSize(QSize(400, 400))
        self.pushButton_5.setStyleSheet(u"QPushButton{image: url(iconos/abrir-agregar-carpeta.png);}"
                                        "QPushButton:pressed { background-color: #525252; }"
                                        "QPushButton:checked { background-color: #525252; }")

        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_5, 0, 1, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(140, 140))
        self.pushButton_6.setMaximumSize(QSize(400, 400))
        self.pushButton_6.setStyleSheet(u"QPushButton{image: url(iconos/archivo-pdf.png)}"
                                        "QPushButton:pressed { background-color: #525252; }"
                                        "QPushButton:checked { background-color: #525252; }")

        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_6, 0, 5, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(400, 400))
        self.label_12.setStyleSheet(u"font-size:45px;\n"
                                    "")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 1, 5, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(400, 400))
        self.label_14.setStyleSheet(u"font-size:45px;\n"
                                    "")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 4, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(140, 140))
        self.pushButton_8.setMaximumSize(QSize(400, 400))
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(u"QPushButton{image: url(iconos/grupo-de-usuarios.png)}"
                                        "QPushButton:pressed { background-color: #525252; }"
                                        "QPushButton:checked { background-color: #525252; }")

        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_8, 0, 4, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.frame)

        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        ##################################
        self.pushButton_5.clicked.connect(self.abrir_ventana_crear_organigrama)
        self.pushButton_7.clicked.connect(self.abrir_ventana_abrir_organigrama)
        self.pushButton_6.clicked.connect(self.abrir_ventana_imprimir_organigrama)
        self.pushButton_8.clicked.connect(self.abrir_ventana_personales)

        ##################################
        MainWindow.setWindowTitle("Menu Principal")
        self.label_11.setText("Gestor de Organigramas")
        self.label_10.setText("Crear")
        self.pushButton_7.setText("")
        self.label_13.setText("Abrir")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.label_12.setText("Imprimir")
        self.label_14.setText("Personal")
        self.pushButton_8.setText("")

    #Abre las distintas ventanas en el menu principal
    def abrir_ventana_crear_organigrama(self):
        from Crear_Organigramas import crear_organigramas
        self.ventana_menu_principal.close()
        self.ventana_crear_organigrama = crear_organigramas()
        self.ventana_crear_organigrama.setupUi(self.ventana_crear_organigrama)
        self.ventana_crear_organigrama.show()

    def abrir_ventana_abrir_organigrama(self):
        from Abrir_Organigramas import abrir_organigrama
        self.ventana_menu_principal.close()
        self.ventana_abrir_organigrama = QMainWindow()
        self.ui = abrir_organigrama(self.ventana_abrir_organigrama)
        self.ui.setupUi(self.ventana_abrir_organigrama)
        self.ventana_abrir_organigrama.show()

    def abrir_ventana_imprimir_organigrama(self):
        from imprimir_organigrama import imprimir_organigrama
        self.ventana_menu_principal.close()
        self.ventana_imprimir_organigrama = QMainWindow()
        self.ui = imprimir_organigrama(self.ventana_imprimir_organigrama)
        self.ui.setupUi(self.ventana_imprimir_organigrama)
        self.ventana_imprimir_organigrama.show()

    def abrir_ventana_personales(self):
        from Ingresar_Personales import personales
        self.ventana_menu_principal.close()
        self.ventana_personales = QMainWindow()
        self.ui = personales(self.ventana_personales)
        self.ui.setupUi(self.ventana_personales)
        self.ventana_personales.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = menu_principal(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

