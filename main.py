import pandas as pd

def analisis_analitico(edades):
    # Verificar si 'edades' es una lista de valores numéricos
    if not isinstance(edades, list) or not all(isinstance(x, (int, float)) for x in edades):
        raise ValueError("La entrada debe ser una lista de valores numéricos.")

# Lista de edades de los alumnos
edades_alumnos = [20, 22, 21, 23, 22, 24, 20, 21, 25, 23, 22, 21, 24, 22, 23, 20, 21, 24, 22, 23, 25, 20, 21, 24, 22, 23, 22, 21, 25, 23]

data_frame = pd.DataFrame()
data_frame['fi'] = edades_alumnos #fi es la frecuencia absoluta
data_frame['Fi'] = data_frame['fi'].cumsum() #comsum es la suma acumulada
data_frame['ri'] = data_frame['fi'] / data_frame["fi"].sum() #sum es la suma total
data_frame['Ri'] = data_frame['ri'].cumsum()
data_frame['pi%'] = data_frame['ri'] * 100
data_frame['Pi%'] = data_frame['pi%'].cumsum()

data_frame.to_csv('edades.csv', index=False)
print(data_frame)
