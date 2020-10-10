"""import pandas as pd

#pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False) #construtor da Series
dados1 = pd.Series(data=5) # Cria uma Series com o valor a
dados2 = pd.Series('Howard Ian Peter Jonah Kellie'.split()) # Cria uma Series com uma lista de nomes
#pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False) #construtor do DataFrame
dados3 = pd.DataFrame('Howard Ian Peter Jonah Kellie'.split(), columns=['nome']) # Cria um DataFrame, de uma coluna a partir de uma lista
print(dados1, "\n\n", dados2, "\n\n", dados3, "\n\n")

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]
dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas # Cria um DataFrame a partir de uma lista de tuplas
df = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])
print(df['idade'].mean())"""

import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np


# Corrigindo estado aleatório para reprodutibilidade
np.random.seed(18202020)

# criar dados aleatórios
xdata = np.random.random([3, 10])

# divide os dados em duas partes, usando o fatiamento
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# ordena os dados para que façam curvas limpas
xdata1.sort()
xdata2.sort()

# crie alguns pontos de dados y
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# plota os dados
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# cria os eventos marcando os x pontos de dados
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# cria os eventos marcando os pontos de dados y
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# adiciona os eventos ao eixo
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# define os limites
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title('Gráfico de linha com pontos de dados')

# mostra o grafico
plt.show()
