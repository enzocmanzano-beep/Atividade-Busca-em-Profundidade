
# ==========================================
# ATIVIDADE: BUSCA EM PROFUNDIDADE
#
# INTEGRANTES DO GRUPO:
# Enzo Casagrande Manzano - RA: 2074819
# Guilherme Doretto - RA: 2029940
# Giovanni Escórcio - RA: 2061814
# ==========================================


class Grafo:
    # Representacao do grafo por lista de adjacencia
    def __init__(self):
        self.grafo = {}

    def inserir_vertice(self, v):
        if v not in self.grafo:
            self.grafo[v] = []

    def inserir_aresta(self, x, y):
        self.inserir_vertice(x)
        self.inserir_vertice(y)

        if y not in self.grafo[x]:
            self.grafo[x].append(y)

        if x not in self.grafo[y]:
            self.grafo[y].append(x)

    # Busca em profundidade utilizando pilha (LIFO)
    def dfs(self, inicio):
        if inicio not in self.grafo:
            return []

        pilha = [inicio]
        visitados = []

        while pilha:
            vertice = pilha.pop()

            if vertice not in visitados:
                visitados.append(vertice)

                for vizinho in self.grafo[vertice]:
                    if vizinho not in pilha and vizinho not in visitados:
                        pilha.append(vizinho)

        return visitados

    # Detecta ciclos utilizando busca em profundidade
    def detectar_ciclo(self):
        visitados = set()

        # Percorre todos os componentes do grafo
        for inicio in self.grafo:
            if inicio not in visitados:
                pilha = [{
                    "vertice": inicio,
                    "pai": None
                }]

                while pilha:
                    atual = pilha.pop()
                    vertice = atual["vertice"]
                    pai = atual["pai"]

                    # Evita processar novamente um vertice
                    if vertice in visitados:
                        continue

                    visitados.add(vertice)

                    for vizinho in self.grafo[vertice]:

                        # Ignora a aresta que volta ao pai
                        if vizinho == pai:
                            continue

                        # Verifica se o vizinho ja foi visitado
                        if vizinho in visitados:
                            return True

                        # Verifica se o vizinho ja esta na pilha
                        na_pilha = any(
                            item["vertice"] == vizinho
                            for item in pilha
                        )

                        if na_pilha:
                            return True

                        pilha.append({
                            "vertice": vizinho,
                            "pai": vertice
                        })

        return False

    def exibir_grafo(self):
        print("\n===== LISTA DE ADJACENCIA =====")

        for vertice in self.grafo:
            print(f"{vertice}: {self.grafo[vertice]}")


def executar_testes():
    print("\n===== TESTES =====")

    # Teste 1: grafo sem ciclos
    g1 = Grafo()
    g1.inserir_aresta("A", "B")
    g1.inserir_aresta("A", "C")
    g1.inserir_aresta("B", "D")

    assert g1.detectar_ciclo() is False
    print("Grafo sem ciclos: OK")

    # Teste 2: grafo com ciclo
    g2 = Grafo()
    g2.inserir_aresta("A", "B")
    g2.inserir_aresta("B", "C")
    g2.inserir_aresta("C", "A")

    assert g2.detectar_ciclo() is True
    print("Grafo com ciclos: OK")

    # Teste 3: grafo desconexo sem ciclos
    g3 = Grafo()
    g3.inserir_aresta("A", "B")
    g3.inserir_aresta("C", "D")
    g3.inserir_vertice("E")

    assert g3.detectar_ciclo() is False
    print("Grafo desconexo sem ciclos: OK")

    # Teste 4: grafo desconexo com ciclo
    g4 = Grafo()
    g4.inserir_aresta("A", "B")
    g4.inserir_aresta("C", "D")
    g4.inserir_aresta("D", "E")
    g4.inserir_aresta("E", "C")

    assert g4.detectar_ciclo() is True
    print("Grafo desconexo com ciclo: OK")

    # Teste 5: busca em profundidade
    resultado = g1.dfs("A")

    assert len(resultado) == 4
    assert "A" in resultado
    assert "B" in resultado
    assert "C" in resultado
    assert "D" in resultado
    print("Busca em profundidade: OK")

    # Teste 6: vertice inexistente
    assert g1.dfs("X") == []
    print("Vertice inexistente: OK")

    print("Todos os testes foram executados com sucesso!")


if __name__ == "__main__":

    g = Grafo()

    vertices = ["A", "B", "C", "D", "E", "F"]

    for vertice in vertices:
        g.inserir_vertice(vertice)

    arestas = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("D", "E"),
        ("E", "F")
    ]

    for x, y in arestas:
        g.inserir_aresta(x, y)

    g.exibir_grafo()

    print("\n===== BUSCA EM PROFUNDIDADE =====")
    print("DFS a partir de A:", g.dfs("A"))

    print("\n===== DETECCAO DE CICLOS =====")

    if g.detectar_ciclo():
        print("O grafo possui ciclo!")
    else:
        print("O grafo nao possui ciclo!")

    executar_testes()
