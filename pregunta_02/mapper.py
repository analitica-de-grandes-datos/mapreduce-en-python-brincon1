#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
   
    #for line in sys.stdin:
    for row in sys.stdin:
        dividir = row.split(",")
        segundaCol = dividir[3]
        terceraCol = dividir[4]
        
        
        #print(segundaCol)

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    

        #
        # escribe al flujo estandar de salida
    

        sys.stdout.write(f"{segundaCol}\t {terceraCol}\n")