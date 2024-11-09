from graph import *


def complete_graph(n: int):
    complete = Graph(False)
    complete.create_random(n, n * (n - 1) // 2)
    return complete


def custom_graph():
    custom = Graph(False)

    vertexes = [0, 1, 2, 3, 4]

    for _ in range(len(vertexes)):
        custom.add_vertex()

    edges = [[0, 1], [1, 2], [3, 4]]

    for edge in edges:
        custom.add_edge(edge)

    print(str(custom) + "\n")
    return custom


def check_homeomorphism(gr1, gr2, f):
    # check if function assigns to each value
    for v in f:
        if v == -1:
            return False

    # gr1 vertexes (gr1 has more vertexes)
    for v1 in range(len(gr1.graph)):
        for v2 in range(len(gr1.graph)):
            # if(g1[v1][v2]) exists
            if (gr1.graph[v1][v2] != 0):
                # check if g2[f(v1)][f(v2)] exists
                if (gr2.graph[f[v1]][f[v2]] == 0):
                    return False

    return True


def print_function(gr1, f):
    for v1 in range(len(gr1.graph)):
        string = str(v1) + " " + str(f[v1])
        print(string)


def genereate_translation(trans: list, curr: list, pos: int, interval: int, gr1, gr2):
    if pos == len(curr):
        trans.append(curr)
    else:
        for i in range(interval):
            curr[pos] = i

            ok = True

            for v1 in curr:
                for v2 in curr:
                    if (gr1.graph[v1][v2] != 0):
                        # check if g2[f(v1)][f(v2)] exists
                        if (gr2.graph[curr[v1]][curr[v2]] == 0):
                            ok = False
                            break

            if ok == True:
                genereate_translation(trans, curr[:], pos + 1, interval, gr1, gr2)

            curr[pos] = -1


if __name__ == "__main__":
    gr1 = custom_graph()
    gr2 = complete_graph(4)

    f = []

    if len(gr2.graph) > len(gr1.graph):
        switch_gr = gr1
        gr1 = gr2
        gr2 = switch_gr

    for i in range(len(gr1.graph)):
        f.append(-1)

    translations = []
    genereate_translation(translations, f, 0, len(gr2.graph), gr1, gr2)

    for translation in translations:
        if (check_homeomorphism(gr1, gr2, translation) == True):
            print_function(gr1, translation)
            exit()
