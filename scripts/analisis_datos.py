
# analisis_datos.py
# Autor: P2 - Paco
# Cátedra: Organización Empresarial - UTN TUPaD
# Propósito: analizar el dataset de ventas diarias 2024
# y generar indicadores clave para la toma de decisiones

import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta de resultados si no existe
# Usamos exist_ok=True para evitar errores si ya existe
os.makedirs("resultados", exist_ok=True)

# --- CARGA DE DATOS ---
# Ruta relativa para garantizar reproducibilidad en cualquier entorno
df = pd.read_csv("datos/ventas.csv", parse_dates=["sales_date"])

# --- INDICADORES BÁSICOS ---

# Ventas totales del período
ventas_totales = df["sales_amount"].sum()
print(f"Ventas totales 2024: ${ventas_totales:,.2f}")

# Promedio diario de ventas
promedio_diario = df["sales_amount"].mean()
print(f"Promedio diario de ventas: ${promedio_diario:,.2f}")

# Día con mayor venta registrada
dia_max = df.loc[df["sales_amount"].idxmax()]
print(f"Día con mayor venta: {dia_max['sales_date'].date()} - ${dia_max['sales_amount']:,.2f}")

# Día con menor venta registrada
dia_min = df.loc[df["sales_amount"].idxmin()]
print(f"Día con menor venta: {dia_min['sales_date'].date()} - ${dia_min['sales_amount']:,.2f}")

# --- VENTAS POR MES ---
# Agrupamos por mes para detectar tendencias estacionales
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# --- GRÁFICO: Evolución mensual de ventas ---
fig, ax = plt.subplots(figsize=(12, 5))
ventas_por_mes.plot(kind="bar", ax=ax, color="steelblue", edgecolor="black")
ax.set_title("Evolución Mensual de Ventas - 2024", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes")
ax.set_ylabel("Monto Total ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar en /resultados con ruta relativa
plt.savefig("resultados/grafico_ventas_mensuales.png", dpi=150)
print("\nGráfico guardado en resultados/grafico_ventas_mensuales.png")
plt.show()

# --- EXPORTAR RESUMEN EN CSV ---
resumen = pd.DataFrame({
    "indicador": ["Ventas totales", "Promedio diario", "Venta máxima", "Venta mínima"],
    "valor": [ventas_totales, promedio_diario, dia_max["sales_amount"], dia_min["sales_amount"]]
})
resumen.to_csv("resultados/resumen_indicadores.csv", index=False)
print("Resumen exportado en resultados/resumen_indicadores.csv")
