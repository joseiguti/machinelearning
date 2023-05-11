import pandas as pd

productos_validos = ['Mouse', 'Teclado']

# Cargar datos
df = pd.read_csv("data.csv")

# Verificar valores perdidos
'''
Verificar si hay valores perdidos en las columnas y decidir cómo manejarlos 
(eliminar las filas, rellenar con valores por defecto, etc.).
'''
print("Valores perdidos:")
print(df.isnull().sum())

# Eliminar filas con valores perdidos
df = df.dropna()

# Tratar valores especiales. Elimino las filas que en estas columnas
# sus valores sean diferentes a numero positivos
df = df[(df["Cantidad"] > 0) & (df["Precio Unitario"] > 0)]

# Eliminar filas duplicadas
df = df.drop_duplicates()

# Corregir errores tipográficos
df["Producto"] = df["Producto"].str.strip()  # Eliminar espacios en blanco al inicio y final

# Verificar clases mal etiquetadas
print("Clases de estado de venta:")
print(df["Estado de la Venta"].value_counts())

# Filtrar valores que no están en la lista de nombres válidos
df_errores_tipograficos = df[~df['Producto'].isin(productos_validos)]

# Imprimir los valores que podrían ser errores tipográficos
print(df_errores_tipograficos['Producto'])

# Eliminar esos valores que no estaban en esa lista
df = df.drop(df_errores_tipograficos.index)

# Imprimir el DataFrame limpio
print("DataFrame limpio:")
print(df)
