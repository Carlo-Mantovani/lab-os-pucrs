# Nomes
Nomes: Aloysio Winter, Carlo Mantovani, Felipe Elsner, Lucas Cunha

# Programa

## Descrição
O programa implementado cria um ambiente concorrente no qual um número específico de threads escreve em um buffer compartilhado, cada uma com seu caráctere específico. 

O programa utiliza barreiras para sincronizar as threads, garantindo que todas as threads iniciem a escrita no buffer simultaneamente, evitando assim que uma thread tenha vantagem sobre outra. Assim, cada thread escreve no buffer até que ele esteja completamente preenchido. Para evitar que ocorra problemas de data race, um semáforo binário (mutex) é usado para controlar o acesso concorrente ao buffer.

Por fim, após a conclusão das threads, o programa analisa o conteúdo do buffer para determinar a ordem de escalonamento das threads, contanto a frequência de escalonamento de cada uma delas. 

## Parâmetros
O programa possui apenas dois parâmetros:
- 1: Número de Threads
- 2: Tamanho do Buffer em Kilobytes  
Logo, um exemplo de como executar o programa seria:
```
./sched_profiler 4 10000
```

## Exemplo de Execução
O programa, ao ser executado, imprime a ordem de escalonamento que foi realizada no preenchimento do buffer, e imprime a frequência de cada thread especifica. Assim, segue um exemplo de execução em um núcleo de CPU para 4 threads e um buffer de 10mb:
```
./sched_profiler 4 10000

Threads created
Waiting for threads to finish...

Scheduling order: DCBDACBACDBADBA

Counter of each thread: 
A = 4
B = 4
C = 3
D = 4

```