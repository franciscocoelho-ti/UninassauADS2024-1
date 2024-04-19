# Importe a função sleep do pacote time. Essa função permite suspender a execução do programa
# por um determinado período de tempo, especificado em segundos.
from time import sleep

# O valor True passado na repetição while, gera uma repetição continua (sem condição lógica),
# até que algo faça a tarefa de interromper essa ação.
while True:
    try:
        # Foi colocado o bloco try para capturar eventuais exceções que gerem a interrupção
        # da execução natural.
        
        dividendo = int(input('Informe o valor do dividendo: '))
        divisor = int(input('Informe o valor do divisor: '))
        quociente = dividendo / divisor
        print('O resultado foi ', quociente) 
        break 
        # Caso a execução ocorra normalmente, o algoritmo vai fazer as instruções acima e o
        # comando break vai interromper a execução da repetição while, colocando fim a execução
        # do algoritmo.

    except ValueError:
        # Se houver uma exceção (erro) por eventual valor incorreto informado pelo usuário,
        # é exibido a mensagem abaixo, e uma função sleep() gera um intervalo de 3 segundos
        # para iniciar uma nova repetição do while.
        print('Erro. Você não informou números inteiros')
        sleep(3)
        
    except ZeroDivisionError:
        # Mesma lógica do except acima, a diferença que nesse bloco a execução ocorrerá se
        # o usuário informaro valor zero na variável divisor.
        print('Erro. Impossível dividir por ZERO.')
        sleep(3)

 