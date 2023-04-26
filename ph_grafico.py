import time
import sys
import mysql.connector
import random
import matplotlib.pyplot as plt
import datetime

def transportes():
    # Criar conexão com o banco de dados
    mydb = mysql.connector.connect(
        host="34.236.133.247",
        user="root",
        password="urubu100",
        database='transportePublico'
    )

    # Criar cursor para executar consultas no banco de dados
    cursor = mydb.cursor()

    # Selecionar todos os dados da tabela e agrupar por hora
    cursor.execute("SELECT SUBSTRING(horario, 1, 2) as hora, SUM(fluxo_deficientes) FROM fluxo_deficientes GROUP BY hora ORDER BY hora")

    # Extrair os dados do cursor
    dados = cursor.fetchall()
    print(dados)

    # Criar lista com as horas e outra com os fluxos
    horas = [int(d[0]) for d in dados]
    fluxos = [d[1] for d in dados]

    # Plotar gráfico de barras
    plt.bar(horas, fluxos)
    plt.xlabel('Horário')
    plt.ylabel('Fluxo de deficientes')
    plt.title('Fluxo de Deficientes por Hora')
    plt.show()

transportes()
