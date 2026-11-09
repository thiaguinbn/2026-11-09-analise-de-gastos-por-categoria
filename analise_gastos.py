import pandas as pd
import matplotlib.pyplot as plt

# Ler a tabela fictícia e mostrar suas cinco primeiras linhas.
gastos = pd.read_csv("gastos.csv")
print("Primeiras linhas do arquivo gastos.csv:")
print(gastos.head())

# Somar os valores e calcular o gasto médio por registro.
total = gastos["valor"].sum()
media = gastos["valor"].mean()
print(f"\nTotal gasto: R$ {total:.2f}")
print(f"Média por registro: R$ {media:.2f}")

# Agrupar os gastos por categoria e organizar do maior para o menor.
por_categoria = gastos.groupby("categoria")["valor"].sum()
por_categoria = por_categoria.sort_values(ascending=False)
print("\nTotal por categoria:")
print(por_categoria)
print(f"\nCategoria com maior gasto: {por_categoria.index[0]}")

# Comparar os totais em um gráfico de barras.
por_categoria.plot(kind="bar", color="#3568a8", rot=0)
plt.title("Gastos por categoria — dados fictícios")
plt.xlabel("Categoria")
plt.ylabel("Valor total (R$)")
plt.tight_layout()
plt.savefig("grafico_gastos.png", dpi=150)
plt.close()
print("\nGráfico salvo em grafico_gastos.png")
