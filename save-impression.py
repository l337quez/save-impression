# iconos
# https://material.io/resources/icons/?icon=bookmark_border&style=baseline
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


        #groupBox = QtGui.QGroupBox("E&xclusive Radio Buttons")

        #label titulo
        label = QtWidgets.QLabel(self)
        label.setText("Parametros donde quedo la Impresion")
        label.setGeometry(10, 60, 300, 20)
        label.setStyleSheet("QLabel { font-weight: bold;} ")
     


        #label altura
        label2 = QtWidgets.QLabel(self)
        label2.setText("Altura de Capa:")
        label2.move(10, 100)
        
        #label numero de capas
        label3 = QtWidgets.QLabel(self)
        label3.setText("N° de Capa:")
        label3.move(250, 100)
        
        #label licencia y autor
        lversion = QtWidgets.QLabel(self)
        lversion.setText("GNU Save I3D. Alpha 0.001     Developed by: Ronal Forero     GPL-V3")
        lversion.setGeometry(10, 427, 500, 20)
   
        
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

        
         #self.setWindowIcon(QIcon('save-impression.png'))        
        
        ############  Botones
        
        #Boton Abrir Gcode
        button = QtWidgets.QPushButton("Abrir Gcode", self)
        button.setIcon(QIcon('open.png'))
        button.setIconSize(QtCore.QSize(24,24))
        button.clicked.connect(self.load_file_gcode)
        button.move(10, 10)
        button.resize(120,32)
        #button.setIconSize(QtCore.QSize(24,24))
        
        #Boton Guardar Gcode
        button1 = QtWidgets.QPushButton("Guardar Gcode", self)
        button1.move(370, 380)
        button1.resize(120,32)
        button1.clicked.connect(self.save_file_gcode)
        
        #Boton Ver Informacion 
        button2 = QtWidgets.QPushButton("Ver Informacion", self)
        button2.move(10, 190)
        button2.resize(110,32)
        button2.clicked.connect(self.button_Informacion)
        
        #Boton Verificar Altura 
        button3 = QtWidgets.QPushButton("Verificar Altura", self)
        button3.move(10, 140)
        button3.resize(110,32)
        button3.clicked.connect(self.verificar_altura)






############  FUNCIONES


    def verificar_altura(self):
        pass
        
        
        
        
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
        A_capa=self.line.text()
        #La Capa buscada es
        S_Ncapa= ";LAYER:" + str(N_capa) #Search Number cap
        S_Acapa= "Z" + str(A_capa)
        
        print("La Capa buscada es: " + S_Acapa)
        print(type(S_Acapa))
        RUTA= open('ruta.txt', 'r+')
        ruta_gcode= RUTA.read()
        RUTA.close()
        print(ruta_gcode)
        contador=0 #contador de lineas
        count_caps=0 #contador de capas
        
        with open(ruta_gcode) as f: #funcion with cierra inteligentemente al archivo
           for line in f:
              contador=contador+1
              
              if ";LAYER_COUNT:" in line:
                  print ( "N de Linea marco: " + str(contador))
                  n_marco=contador
                  print(n_marco)
                  
              
#               if S_capa in line: # Buscando el Numero de Capa
#                   print ( "N de Linea: " + str(contador))
#                   n_capa=contador
#                   #Eliminar linas
#                   lines = f.readlines()
#                   a= lines[0:n_capa-1]
#                   b= lines[n_marco-1:]
                  #open('newfile.gcode', 'w').writelines([*a, *b] )          
                  
                  
                  
#               if S_capa in line: # Buscando Altura de Capa
#                   print ( "N de Linea: " + str(contador))
#                   n_capa=contador
#                   #Eliminar linas
#                   lines = f.readlines()
#                   a= lines[0:n_capa-1]
#                   b= lines[n_marco-1:]
#                   open('newfile.gcode', 'w').writelines([*a, *b] )  









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
    window.resize(500,450)
    #NOmbre de la ventana
    window.setWindowTitle("GNU Save  I3D") 
    window.show()
    sys.exit( app.exec_() )
    
    
    

    
  
    
    
