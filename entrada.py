from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from Funciones_Dependencias import *
import pickle


class Formulario(QWidget):
    def __init__(self, codigo_org):
        super().__init__()
        self.codigo_org = codigo_org
        self.name_deps = []
        self.Organigramas = cargar_dependencia_organigrama(self.codigo_org)
        self.initUI()
        self.nombre = ""
        self.apellido = ""
        self.ci = ""
        self.direccion = ""
        self.dependencia = ""
        self.numero = ""
        self.salario = ""

    def initUI(self):

        # Etiquetas
        self.label_nombre = QLabel('Nombre:')
        self.label_apellido = QLabel('Apellido:')
        self.label_ci = QLabel('CI:')
        self.label_direccion = QLabel('Dirección:')
        self.label_dependencia = QLabel('dependencia:')
        self.label_numero = QLabel('Número:')
        self.label_salario = QLabel('Salario:')
        # Campos de texto
        self.text_nombre = QLineEdit()
        self.text_apellido = QLineEdit()
        self.text_ci = QLineEdit()
        self.text_direccion = QLineEdit()
        self.text_dependencia = QComboBox()
        self.actualizar_nombre_mostrado()
        self.text_numero = QLineEdit()
        self.text_salario = QLineEdit()
        # Botón Enviar
        self.btn_enviar = QPushButton('Enviar')
        self.btn_enviar.clicked.connect(self.enviar_datos)
        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_nombre)
        vbox.addWidget(self.text_nombre)
        vbox.addWidget(self.label_apellido)
        vbox.addWidget(self.text_apellido)
        vbox.addWidget(self.label_ci)
        vbox.addWidget(self.text_ci)
        vbox.addWidget(self.label_direccion)
        vbox.addWidget(self.text_direccion)
        vbox.addWidget(self.label_dependencia)
        vbox.addWidget(self.text_dependencia)
        vbox.addWidget(self.label_salario)
        vbox.addWidget(self.text_salario)
        vbox.addWidget(self.label_numero)
        vbox.addWidget(self.text_numero)
        vbox.addWidget(self.btn_enviar)

        self.setLayout(vbox)
        self.setWindowTitle('Formulario')

    #Funcion para obtener los datos que se vayan ingresando de las personas
    def enviar_datos(self):
        self.nombre = self.text_nombre.text()
        self.apellido = self.text_apellido.text()
        self.ci = self.text_ci.text()
        self.direccion = self.text_direccion.text()
        self.dependencia = self.text_dependencia.currentText()
        self.numero = self.text_numero.text()
        self.salario = self.text_salario.text()
        self.text_salario.clear()
        self.text_apellido.clear()
        self.text_nombre.clear()
        self.text_ci.clear()
        self.text_direccion.clear()
        self.text_numero.clear()

    def getName(self):
        return self.nombre

    def getApe(self):
        return self.apellido

    def getCI(self):
        return self.ci

    def get_direccion(self):
        return self.direccion

    def get_numero(self):
        return self.numero

    def get_dependencia(self):
        return self.dependencia

    def get_salario(self):
        return self.salario;

    #Permite actualizar las dependencias que se muestran en el combobox
    def actualizar_nombre_mostrado(self):
        try:
            file_path = os.path.join("archivos_organigramas", f'organigrama{self.codigo_org}_dependencias')
            with open(file_path, "rb") as archivo:
                self.Organigramas = pickle.load(archivo)
                self.name_deps = matriz_nombre_codigo(self.Organigramas.raiz, [])
        except FileNotFoundError:
            self.name_deps = []
        for dependencia in self.name_deps:
            self.text_dependencia.addItem(dependencia[0], dependencia[1])


