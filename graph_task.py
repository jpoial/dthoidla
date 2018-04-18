#!/usr/bin/env python3

import random


class Graph(object):

    __name = "Graph object"
    __first_vertex = None
    __info = 0

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_first_vertex(self):
        return self.__first_vertex

    def set_first_vertex(self, vertex):
        self.__first_vertex = vertex

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def __str__(self):
        nl = "\n"
        res = nl + self.get_name()
        v = self.get_first_vertex()
        while v:
            res += nl + str(v) + " -->"
            a = v.get_first_out_arc()
            while a:
                res += " " + str(a)
                res += " (" + v.get_name() + "->" + a.get_target(). \
                    get_name() + ")"
                a = a.get_next()
            v = v.get_next()
        return res

    def matrix(self):
        v = self.get_first_vertex()
        n = 0
        while v:
            v.set_info(n)
            n += 1
            v = v.get_next()
        res = [[0] * n for row in range(n)]
        v = self.get_first_vertex()
        while v:
            a = v.get_first_out_arc()
            while a:
                i = v.get_info()
                j = a.get_target().get_info()
                res[i][j] += 1
                a = a.get_next()
            v = v.get_next()
        return res

    def create_vertex(self, name):
        res = Vertex(name)
        res.set_next(self.get_first_vertex())
        self.set_first_vertex(res)
        return res

    def create_arc(self, name, fr, to):
        res = Arc(name)
        res.set_next(fr.get_first_out_arc())
        fr.set_first_out_arc(res)
        res.set_target(to)
        return res

    def create_random_tree(self, number_of_vertices):
        if number_of_vertices < 1:
            return
        vlist = []
        for from_i in range(number_of_vertices):
            name = "v" + str(number_of_vertices - from_i)
            vlist.append(self.create_vertex(name))
            if from_i > 0:
                to_i = random.randint(0, from_i - 1)
                from_v = vlist[from_i]
                to_v = vlist[to_i]
                self.create_arc("a" + to_v.get_name() +
                                "_" + from_v.get_name(), to_v, from_v)
                self.create_arc("a" + from_v.get_name() +
                                "_" + to_v.get_name(), from_v, to_v)

    def create_random_simplegraph(self, number_of_vertices, number_of_edges):
        self.set_first_vertex(None)
        if number_of_vertices < 1:
            return
        if (number_of_edges < number_of_vertices - 1) or \
                (number_of_edges > number_of_vertices * (number_of_vertices - 1) / 2):
            raise ValueError("Wrong number of edges: " + str(number_of_edges))
        self.create_random_tree(number_of_vertices)
        connected = self.matrix()
        vlist = []
        v = self.get_first_vertex()
        while v:
            vlist.append(v)
            v = v.get_next()
        remaining_edges = number_of_edges - number_of_vertices + 1
        while remaining_edges > 0:
            i_v1 = random.randint(0, number_of_vertices - 1)
            i_v2 = random.randint(0, number_of_vertices - 1)
            if i_v1 == i_v2:
                continue
            if (connected[i_v1][i_v2] > 0) or (connected[i_v2][i_v1] > 0):
                continue
            v1 = vlist[i_v1]
            v2 = vlist[i_v2]
            self.create_arc("a" + v1.get_name() +
                            "_" + v2.get_name(), v1, v2)
            self.create_arc("a" + v2.get_name() +
                            "_" + v1.get_name(), v2, v1)
            connected[i_v1][i_v2] = 1
            connected[i_v2][i_v1] = 1
            remaining_edges -= 1


class Vertex(object):

    __name = "Vertex object"
    __first_out_arc = None
    __next = None
    __info = 0

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_first_out_arc(self):
        return self.__first_out_arc

    def set_first_out_arc(self, arc):
        self.__first_out_arc = arc

    def get_next(self):
        return self.__next

    def set_next(self, next_vertex):
        self.__next = next_vertex

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def __str__(self):
        return self.get_name() + " " + str(self.get_info())


class Arc(object):

    __name = "Arc object"
    __next = None
    __target = None
    __info = 0

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_next(self):
        return self.__next

    def set_next(self, next_arc):
        self.__next = next_arc

    def get_target(self):
        return self.__target

    def set_target(self, target):
        self.__target = target

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def __str__(self):
        return self.get_name() + " " + str(self.get_info())


def main():
    """
    Main method.
    """
    g1 = Graph("G")
    g1.create_random_simplegraph(6, 15)
    print(g1)
    m = g1.matrix()
    print(m)


if __name__ == '__main__':
    main()
