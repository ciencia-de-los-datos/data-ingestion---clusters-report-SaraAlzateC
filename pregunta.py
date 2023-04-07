"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    df = pd.read_csv("clusters_report.txt")
    df = df.rename(columns=lambda x: x.lower().replace(" ", "_"))
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace("\s+"," ").str.replace(",\s+", ", ").str.strip().str.rstrip(".")
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].str.replace("%", "").str.replace(",", ".")
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype(float)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
    return df
