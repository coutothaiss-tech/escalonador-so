"""
Simulador simples de escalonamento de processos
Disciplina: Sistemas Operacionais (ADS) - Trabalho 2

Algoritmos: FCFS, SJF, Prioridade e Round Robin.
Uma única CPU, todos os processos chegam no instante 0.
Cada processo é uma tupla: (nome, tempo_de_cpu, prioridade)
"""

# Valor do quantum do Round Robin. Pode ser alterado aqui.
QUANTUM = 2

# Os três cenários do enunciado (ordem de entrada: P1, P2, P3)
CENARIOS = {
    1: ("Processos curtos",        [("P1", 3, 1), ("P2", 1, 1), ("P3", 2, 1)]),
    2: ("Curtos e longos",         [("P1", 8, 1), ("P2", 2, 1), ("P3", 1, 1)]),
    3: ("Prioridades diferentes",  [("P1", 4, 3), ("P2", 2, 1), ("P3", 3, 2)]),
}


# ---------------------------------------------------------------
# ALGORITMOS
# Cada função devolve uma lista de "trechos": (nome, inicio, fim)
# ---------------------------------------------------------------

def executar_em_ordem(processos):
    """Executa os processos na ordem recebida, cada um até terminar."""
    trechos = []
    tempo = 0
    for nome, cpu, prioridade in processos:
        trechos.append((nome, tempo, tempo + cpu))
        tempo += cpu
    return trechos


def fcfs(processos):
    # Ordem da lista, sem mudar nada
    return executar_em_ordem(processos)


def sjf(processos):
    # Ordena pelo menor tempo de CPU.
    # O sorted() é estável: em caso de empate, mantém a ordem original.
    ordenados = sorted(processos, key=lambda p: p[1])
    return executar_em_ordem(ordenados)


def prioridade(processos):
    # Ordena pelo menor número de prioridade (1 vem antes de 2).
    # Em caso de empate, mantém a ordem original.
    ordenados = sorted(processos, key=lambda p: p[2])
    return executar_em_ordem(ordenados)


def round_robin(processos, quantum=QUANTUM):
    # A fila guarda [nome, tempo_restante]
    fila = [[nome, cpu] for nome, cpu, prio in processos]
    trechos = []
    tempo = 0
    while fila:
        nome, restante = fila.pop(0)          # pega o primeiro da fila
        fatia = min(quantum, restante)        # usa no máximo um quantum
        trechos.append((nome, tempo, tempo + fatia))
        tempo += fatia
        restante -= fatia
        if restante > 0:                      # ainda falta tempo?
            fila.append([nome, restante])     # volta para o fim da fila
    return trechos


# ---------------------------------------------------------------
# CÁLCULOS E EXIBIÇÃO
# ---------------------------------------------------------------

def mostrar_resultado(titulo, trechos, processos):
    print(f"\n--- {titulo} ---")

    # Sequência de execução
    sequencia = "; ".join(f"{n} de {i} a {f}" for n, i, f in trechos)
    print("Sequência:", sequencia)

    # Instante em que cada processo terminou = fim do seu último trecho
    termino = {}
    for nome, inicio, fim in trechos:
        termino[nome] = fim

    # Tabela por processo
    print(f"{'Processo':<10}{'CPU':<6}{'Turnaround':<12}{'Espera':<8}")
    soma_turnaround = 0
    soma_espera = 0
    for nome, cpu, prio in processos:
        turnaround = termino[nome]       # turnaround = instante de término
        espera = turnaround - cpu        # espera = turnaround - tempo de CPU
        soma_turnaround += turnaround
        soma_espera += espera
        print(f"{nome:<10}{cpu:<6}{turnaround:<12}{espera:<8}")

    # Médias do conjunto
    quantidade = len(processos)
    print(f"Espera média: {soma_espera / quantidade:.2f}")
    print(f"Turnaround médio: {soma_turnaround / quantidade:.2f}")


def main():
    for numero, (descricao, processos) in CENARIOS.items():
        print("\n" + "=" * 50)
        print(f"CENÁRIO {numero}: {descricao}")
        print("Processos (nome, CPU, prioridade):", processos)

        mostrar_resultado("FCFS", fcfs(processos), processos)
        mostrar_resultado("SJF", sjf(processos), processos)
        mostrar_resultado("Prioridade", prioridade(processos), processos)
        mostrar_resultado(f"Round Robin (quantum {QUANTUM})",
                          round_robin(processos), processos)


main()