#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from __future__ import division
import sys

if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
   
    #for line in sys.stdin:
    for row in sys.stdin:
        
        reemplazo = row.replace("\r", "").replace("\n", "")
       
        letra, numero = reemplazo.split(",")
        
        

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    

        #
        # escribe al flujo estandar de salida
    

        sys.stdout.write(f"{letra}\t {numero}\n")