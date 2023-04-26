import sys
import mysql.connector
import random
import datetime

def transportes():
    # Criar conexão com o banco de dados
    mydb = mysql.connector.connect(
        host="34.236.133.247",
        user="root",
        password="urubu100"
    )

    # Criar cursor para executar consultas no banco de dados
    cursor = mydb.cursor()

    # Criar banco de dados se ele não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS transportePublico")

    # Selecionar o banco de dados
    cursor.execute("USE transportePublico")

    # Criar tabela de fluxo de deficientes
    cursor.execute("CREATE TABLE IF NOT EXISTS fluxo_deficientes (id INT AUTO_INCREMENT PRIMARY KEY, fluxo_deficientes INT, total_deficientes INT, horario TIME, mem INT, velocidade_deficientes DECIMAL(10,4), sensor varchar(45))")

    # Gerar 1000 dados por minuto
    contador=0
    horario = datetime.datetime(2023,2,random.randint(1,28),0,0,0)
    sensor = input("Qual o nome desse sensor?\n")
    while True:
        # Gerar dados aleatórios
        fluxo_deficientes = random.randint(1, 50)
        total_deficientes = random.randint(1, 100)
    
        # Inserir dados na tabela
        cursor.execute("INSERT INTO fluxo_deficientes (fluxo_deficientes, total_deficientes, horario, mem, velocidade_deficientes, sensor) VALUES (%s, %s, %s, %s, %s, %s)",
                       (fluxo_deficientes, total_deficientes, horario, sys.getsizeof(str(fluxo_deficientes)) + sys.getsizeof(str(total_deficientes)) + sys.getsizeof(str(horario.strftime('%H:%M:%S'))), 0), sensor)
        horario+=datetime.timedelta(minutes=10)
        # Esperar um segundo antes de gerar o próximo conjunto de dados
        #time.sleep(1)
        contador+=1

        print(contador)
    
        # Se já tivermos gerado 1000 dados, sair do loop
        if contador >= 1000:
            break
    mydb.commit()
transportes()
