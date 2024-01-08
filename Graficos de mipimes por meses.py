data = {
    "sep_2021" :{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 35
    },
    "oct_2021":{
        "Micro Empresa":0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 289
    },
    "nov_2021":{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 402
    },
    "dic_2021":{
        "Micro Empresa": 79,
        "Pequeña Empresa": 183,
        "Mediana Empresa": 124,
        "Cooperativa no agropecuaria": 2,
        "Total por mes": 388
    },
    "ene_2022":{
        "Micro Empresa": 99,
        "Pequeña Empresa": 188,
        "Mediana Empresa": 69,
        "Cooperativa no agropecuaria": 4,
        "Total por mes": 360
    },
    "feb_2022":{
        "Micro Empresa": 113,
        "Pequeña Empresa": 234,
        "Mediana Empresa": 177,
        "Cooperativa no agropecuaria": 6,
        "Total por mes": 470
    },
    "mar_2022":{
        "Micro Empresa": 142,
        "Pequeña Empresa": 276,
        "Mediana Empresa": 149,
        "Cooperativa no agropecuaria": 14,
        "Total por mes": 581
    },
    "abr_2022":{
        "Micro Empresa": 103,
        "Pequeña Empresa": 226,
        "Mediana Empresa": 100,
        "Cooperativa no agropecuaria": 7,
        "Total por mes": 436
    },
    "may_2022":{
        "Micro Empresa": 68,
        "Pequeña Empresa": 201,
        "Mediana Empresa": 100,
        "Cooperativa no agropecuaria": 2,
        "Total por mes": 371
    },
    "jun_2022":{
        "Micro Empresa": 117,
        "Pequeña Empresa": 273,
        "Mediana Empresa": 143,
        "Cooperativa no agropecuaria": 3,
        "Total por mes": 536
    },
    "jul_2022":{
        "Micro Empresa": 89,
        "Pequeña Empresa": 201,
        "Mediana Empresa": 85,
        "Cooperativa no agropecuaria": 1,
        "Total por mes": 376
    },
    "ago_2022":{
        "Micro Empresa": 110,
        "Pequeña Empresa": 246,
        "Mediana Empresa": 133,
        "Cooperativa no agropecuaria": 2,
        "Total por mes": 491
    },
    "sep_2022":{
        "Micro Empresa": 71,
        "Pequeña Empresa": 162,
        "Mediana Empresa": 44,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 277
    },
    "oct_2022":{
        "Micro Empresa": 71,
        "Pequeña Empresa": 207,
        "Mediana Empresa": 95,
        "Cooperativa no agropecuaria": 1,
        "Total por mes": 374
    },
    "nov_2022":{
        "Micro Empresa": 51,
        "Pequeña Empresa": 167,
        "Mediana Empresa": 62,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 280
    },
    "dic_2022":{
        "Micro Empresa": 87,
        "Pequeña Empresa": 138,
        "Mediana Empresa": 62,
        "Cooperativa no agropecuaria": 1,
        "Total por mes": 288
    },
    "ene_2023":{
        "Micro Empresa": 78,
        "Pequeña Empresa": 230,
        "Mediana Empresa": 76,
        "Cooperativa no agropecuaria": 1,
        "Total por mes": 385
    },
    "feb_2023":{
        "Micro Empresa": 56,
        "Pequeña Empresa": 161,
        "Mediana Empresa": 81,
        "Cooperativa no agropecuaria": 2,
        "Total por mes": 300
    },
    "mar_2023":{
        "Micro Empresa": 94,
        "Pequeña Empresa": 222,
        "Mediana Empresa": 114,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 430
    },
    "abr_2023":{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 273
    },
    "may_2023":{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 62,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 504
    },
    "jun_2023":{
        "Micro Empresa": 108,
        "Pequeña Empresa": 261,
        "Mediana Empresa": 102,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 471
    },
    "jul_2023":{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 0
    },
    "ago_2023":{
        "Micro Empresa": 34,
        "Pequeña Empresa": 98,
        "Mediana Empresa": 59,
        "Cooperativa no agropecuaria": 2,
        "Total por mes": 193
    },
    "sep_2023":{
        "Micro Empresa": 0,
        "Pequeña Empresa": 0,
        "Mediana Empresa": 0,
        "Cooperativa no agropecuaria": 0,
        "Total por mes": 93
    },
    "oct_2023":{
        "Micro Empresa": 52,
        "Pequeña Empresa": 125,
        "Mediana Empresa": 6,
        "Cooperativa no agropecuaria": 1,
        "Total por mes": 184
    }
}
import matplotlib.pyplot as plt

# Obtener las etiquetas para los meses
meses = list(data.keys())
#print(meses)

# Obtener los valores de cada tipo de empresa para cada mes
micro_valores = [data[mes].get("Micro Empresa", 0) for mes in meses]
pequeñas_valores = [data[mes].get("Pequeña Empresa", 0) for mes in meses]
medianas_valores = [data[mes].get("Mediana Empresa", 0) for mes in meses]
cna_valores = [data[mes].get("Cooperativa no agropecuaria", 0) for mes in meses]
total_valores = [data[mes].get("Total por mes", 0) for mes in meses]
#print(micro_valores)
#print(pequeñas_valores)
#print(medianas_valores)
#print(cna_valores)
#print(total_valores)

# Definir los indices de posición para cada barra
posiciones = range(len(meses))
#print(posiciones)

# Generar el gráfico de barras
plt.bar(posiciones, micro_valores, width=0.2, label="Micro")
plt.bar([p + 0.2 for p in posiciones], pequeñas_valores, width=0.2, label="Pequeñas")
plt.bar([p + 0.4 for p in posiciones], medianas_valores, width=0.2, label="Medianas")
plt.bar([p + 0.6 for p in posiciones], cna_valores, width=0.2, label="CNA")
plt.bar([p + 0.8 for p in posiciones], total_valores, width=0.2, label = "Total por mes")

# Personalizar el gráfico
plt.xticks(posiciones, meses, rotation = 60)
plt.xlabel("Meses")
plt.ylabel("Cantidad")
plt.title("Apariciones por mes de los tipos de empresas")
plt.legend()

# Mostrar el gráfico
plt.show()


# Calcular los promedios de cada tipo de empresa por meses
promedio_micro = sum(micro_valores) / len(micro_valores)
promedio_pequeñas = sum(pequeñas_valores) / len(pequeñas_valores)
promedio_medianas = sum(medianas_valores) / len(medianas_valores)
promedio_cna = sum(cna_valores) / len(cna_valores)
promedio_total = sum(total_valores) / len(total_valores)

# Definir los índices de posición para cada barra
posiciones = range(len(meses))

# Generar el gráfico de barras con los promedios
plt.bar(0, promedio_micro, width=0.2, label="Micro")
plt.bar(1, promedio_pequeñas, width=0.2, label="Pequeñas")
plt.bar(2, promedio_medianas, width=0.2, label="Medianas")
plt.bar(3, promedio_cna, width=0.2, label="CNA")
plt.bar(4, promedio_total, width=0.2, label="Total por mes")


# Personalizar el gráfico
plt.xticks([0, 1, 2, 3, 4], ["Micro", "Pequeñas", "Medianas", "CNA", "Total"])
plt.xlabel("Tipo de Empresa")
plt.ylabel("Promedio de Apariciones")
plt.title("Promedio de Apariciones por Tipo de Empresa y Mes")
plt.legend()

# Mostrar el gráfico
plt.show()