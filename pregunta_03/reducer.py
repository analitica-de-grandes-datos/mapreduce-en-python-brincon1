#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import operator
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    dict = {}
    
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:  
        division = line.replace(" ", "").split("\t")
        key = division[0]
        valor = division[1]
        dict[key] = valor
    
      
    sortedDict = sorted(dict.items(), key=operator.itemgetter(1))
    for linea in sortedDict:

        
        
        sys.stdout.write("{}\t{}\n".format(linea[0], linea[1]))