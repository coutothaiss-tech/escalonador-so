# Simulador simples de escalonamento de processos

Trabalho 2 de Sistemas Operacionais (ADS) - Prof. Guibson Krause

## Integrantes

-Thaís Couto Henchen

## Linguagem

Python 3

## O que o programa faz

Simula quatro algoritmos de escalonamento de CPU (FCFS, SJF, Prioridade e Round Robin com quantum 2) em três cenários, todos com os processos chegando no instante 0. Para cada execução, mostra a sequência de execução, o tempo de espera e o turnaround de cada processo, além das médias.

## Como executar

1. Instale o Python 3 (https://www.python.org).
2. Baixe ou clone este repositório.
3. No terminal, dentro da pasta do projeto, execute:

```
python escalonador.py
```

O valor do quantum do Round Robin pode ser alterado na variável `QUANTUM`, no início do arquivo `escalonador.py`.

## Arquivos

- `escalonador.py`: código-fonte do simulador
- `resultados.txt`: saída do programa para os três cenários
- Relatório em PDF: entregue na atividade da NAV

## Uso de IA

Foi utilizada ajuda de IA (Claude, da Anthropic) na construção do código. O funcionamento foi conferido manualmente, e a lógica foi estudada para ser explicada pela integrante.
