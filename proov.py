#!/usr/bin/env python3

# Simplest class


class Num(object):

    __cont = 0

    def __init__(self, content):
        self.__cont = content

    def __str__(self):
        return str(self.__cont)

    def __repr__(self):
        return "Num(" + str(self) + ")"

    def __eq__(self, other):
        return self.__cont == other.__cont

    def __gt__(self, other):
        return self.__cont > other.__cont

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def plus(self, b):
        return self.__cont + b.__cont


def main():
    """
    Main method.
    """
    a1 = Num(6)
    # a2 = a1
    a2 = Num(9)
    s = a1.plus(a2)
    print(s)
    print(a1 == a2)
    print(a1 != a2)
    print(a1 is a2)
    print(a1 > a2)
    print(a1 >= a2)
    print(a1 < a2)
    print(a1 <= a2)
    print(a1)
    print(repr(a1))


if __name__ == '__main__':
    main()
