 

#Eliminar linas
lines = open('archivo_prueba.txt').readlines()
a= lines[0:45]
b= lines[65-1:]
open('newfile.txt', 'w').writelines([*a, *b] )
#open('newfile1.txt', 'w').writelines(lines[65-1:] )


#Unimos los Archivos


#open('newfile.txt', 'w').writelines(lines[0:45] )
#open('newfile.txt', 'w').writelines(lines[65:-1]  )

#buscar palabra
contador=0
with open("archivo_prueba.txt") as f:
   for line in f:
      contador=contador+1
      if "LAYER" in line:
          print ("Encontrada")
          print (contador)
