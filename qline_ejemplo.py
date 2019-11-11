 
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Icono en la ventana
        self.setWindowIcon(QIcon('save-impression.png')) 


        #self.setMinimumSize(QSize(320, 140))    
 
        ############  Etiquetas

        #label 
        label = QtWidgets.QLabel(self)
        label.setText("Parametros donde quedo la Impresion")
        label.setGeometry(10, 50, 300, 50)
        #label.move(10, 65)


        label2 = QtWidgets.QLabel(self)
        label2.setText("Altura de Capa:")
        label2.move(10, 100)
        
        
        label3 = QtWidgets.QLabel(self)
        label3.setText("N° de Capa:")
        label3.move(250, 100)
        
        #label informacion
#         self.linfo = QtWidgets.QLabel("Informacion:                                                     ")
#         self.linfo.move(10, 210)
        
                
        
        ############  Caja de Texto
        
        #Altura de Capa
        self.line = QLineEdit(self)
        self.line.setText("None") 
        self.line.move(110, 100)
        #self.line.resize(200, 32)

        #Numero de Capa
        self.line1 = QLineEdit(self)
        self.line1.setText("None") 
        self.line1.move(330, 100)

        
        
        
        ############  Botones
        
        #Boton Abrir Gcode
        button = QtWidgets.QPushButton("Abrir Gcode", self)
        button.move(10, 10)
        button.resize(120,32)
        button.clicked.connect(self.load_file_gcode)
        
        #Boton Guardar Gcode
        button1 = QtWidgets.QPushButton("Guardar Gcode", self)
        button1.move(370, 280)
        button1.resize(120,32)
        button1.clicked.connect(self.save_file_gcode)
        
        #Boton Ver Informacion 
        button2 = QtWidgets.QPushButton("Ver Informacion", self)
        button2.move(10, 170)
        button2.resize(110,32)
        button2.clicked.connect(self.button_Informacion)
        







############  FUNCIONES



    def load_file_gcode(self):

        fname = QtWidgets.QFileDialog.getOpenFileName(self,filter="GCODE Files (*.gcode)")

        ruta_load=fname[0]
        print(type(ruta_load))
        ruta_load_str=''.join(ruta_load)
        print(ruta_load)
        #leemos el archivo HEX
        leer_file=open(ruta_load,'r')
        texto=leer_file.read()
        leer_file.close()
        
        RUTA= open('ruta.txt', 'w+')
        RUTA.write(ruta_load_str)
        RUTA.close()

        
    def save_file_gcode(self):
        print (self.line1.text())
        N_capa=self.line1.text()
        #La Capa buscada es
        S_capa= ";LAYER:" + str(N_capa)
        print("La Capa buscada es" + str(S_capa))
        RUTA= open('ruta.txt', 'r+')
        ruta_gcode= RUTA.read()
        RUTA.close()
        print(ruta_gcode)
        contador=0 #contador de lineas
        count_caps=0 #contador de capas
        with open(ruta_gcode) as f: #funcion with cierra inteligentemente al archivo
           for line in f:
              contador=contador+1
              
              if S_capa in line:
                  print ( "N de Linea: " + str(contador))
                  count_caps=count_caps+1
                  print ( "N de Capas: " + str(count_caps))


    def button_Informacion(self):
        RUTA= open('ruta.txt', 'r+')
        ruta_gcode= RUTA.read()
        RUTA.close()
        print(ruta_gcode)
        contador=0 #contador de lineas
        count_caps=0 #contador de capas
        with open(ruta_gcode) as f: #funcion with cierra inteligentemente al archivo
           for line in f:
              contador=contador+1
              
              if ";LAYER:" in line:
                  print ( "N de Linea: " + str(contador))
                  count_caps=count_caps+1
                  print ( "N de Capas: " + str(count_caps))
        #informacion del GCODE
                  # ARREGLAR NO MUESTRA LA ETIQUETAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        self.linfo = QtWidgets.QLabel(self)
        self.linfo.setText(str(count_caps))
        self.linfo.move(250, 100)          
        #self.linfo = QtWidgets.QLabel(str(count_caps))
        #self.linfo.move(10, 210)     
        #self.linfo.setText( str(count_caps))


if __name__ == "__main__":
    # Creamos la aplicación, la ventana e iniciamos el bucle
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # Tamaño de la ventana
    window.resize(500,350)
    #NOmbre de la ventana
    window.setWindowTitle("Save Impression 3D") 
    window.show()
    sys.exit( app.exec_() )
    
    
    

    
  
    
    