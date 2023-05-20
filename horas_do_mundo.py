# importar as bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pytz

# Lista com os fusos horários desejados
fusos_horarios = ['America/Sao_Paulo', 'America/New_York',
                  'Europe/London', 'America/Lima',
                  'Europe/Rome', 'Australia/Sydney',
                  'Europe/Paris', 'Asia/Tokyo'
                  ]

# Obtém a hora atual para cada fuso horário
horas = []
for fuso_horario in fusos_horarios:
    # Cria um objeto de fuso horário com base na string do fuso horário
    tz = pytz.timezone(fuso_horario)
    # Obtém a hora atual no fuso horário especificado e
    # Adiciona à lista de horas
    horas.append(datetime.now(tz).time())

# Cria uma lista com os nomes dos fusos horários
nomes_fusos = [tz.split('/')[1].replace('_', ' ') for tz in fusos_horarios]

# A linha acima faz o seguinte:
#  - Para cada string de fuso horário em fusos_horarios, realizamos as seguintes etapas:
#     - Usamos o método split('/') para dividir a string do fuso horário em duas partes, por exemplo, 'America/Sao_Paulo' se torna ['America', 'Sao_Paulo']
#     - Selecionamos a segunda parte, que é o nome do fuso horário, usando [1]
#     - Usamos o método replace('_', ' ') para substituir os underscores (_) por espaços em branco, por exemplo, 'Sao_Paulo' se torna 'Sao Paulo'
#     - O resultado final é adicionado à lista nomes_fusos

# Plota o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Removendo as linhas ao redor do gráfico
sns.set_style("whitegrid")  # Define o estilo para "whitegrid" (com grade branca)

# Remove as bordas e eixos extras
sns.despine(right=True, top=True, bottom=True, left=True)

# Remove xticks do eixo x
plt.tick_params(bottom=False, labelbottom=False)

ax.set(ylabel='Fuso Horário')
ax = sns.barplot(x=[hora.hour for hora in horas], y=nomes_fusos, color='#3498db')

# Adiciona os valores das horas ao lado das barras
for i, hora in enumerate(horas):
    ax.text(hora.hour + 0.5, i, hora.strftime('%I:%M %p'), ha='left', va='center')  # posição do texto das horas

# Configurações do gráfico
plt.title('Horas do Mundo')
# plt.xlabel('Hora (AM/PM)')
# plt.ylabel('Fuso Horário')

# Exibe o gráfico
plt.show()
