import torch
from transformers import pipeline
import csv

generate_text = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")


destinos = []

datos = "./Datos.csv"

with open(datos, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    
    for fila in lector_csv:
        destino = fila[1]
        if fila[0] == 'Barcelona':
            destinos.append(destino)

