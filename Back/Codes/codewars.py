import matplotlib.pyplot as plt
import numpy as np

# Definindo os pontos
x = np.array([0, 4])
y = np.array([0, 0])

# Criando o gráfico
plt.figure(figsize=(6,6))
plt.plot(x, y, marker='o') # Desenha a reta entre os pontos P1 e P2
plt.text(0, 0, 'P1(0,0)', verticalalignment='bottom', horizontalalignment='right')
plt.text(4, 0, 'P2(4,0)', verticalalignment='bottom', horizontalalignment='right')

# Definindo os limites do gráfico para melhor visualização
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Adicionando grade para facilitar a leitura
plt.grid(True)

# Adicionando títulos aos eixos e ao gráfico
plt.title('Reta entre P1(0,0) e P2(4,0) no Plano Cartesiano')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrando o gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()