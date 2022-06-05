#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
   
    #for line in sys.stdin:
    for row in sys.stdin:
        dividir = row.split(",")
        segundaCol = dividir[2]
        if segundaCol == "credit_history":
            continue
        else:
        
        
        #print(segundaCol)

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        #for word in segundaCol:

        #
        # escribe al flujo estandar de salida
        #for word in segundaCol:

            sys.stdout.write("{}\t1\n".format(segundaCol))