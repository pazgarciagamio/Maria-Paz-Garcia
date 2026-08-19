# Clase 2 - Diccionario

import pandas as pd
import numpy as np

datos_caja = {
     "objeto_id": [1,2,3,4,5,6,7,8,9,10],
     "textura":["suave", "rugoso", "poroso", "suave", "rugoso", "suave", "poroso", "rugoso", "suave", "suave" ],
     "rigidez":["blando", "rigido", "medio", "blando", "rigido", "rigido", "blando", "medio", "medio", "medio" ],
     "num_aristas":[0,8,0,4,12,0,0,6,4,0],
     "peso_estimado_g": [ 45.0,120.5,15,0,85.0,210.0,35.0,18.5,95.0,70.0,22.0 ],
     "certeza_observador":[ 5,4,3,5,4,2,4,3,4,3 ]
}

#Chequear que realmente haya quedado bien el diccionario
print(datos_caja)
