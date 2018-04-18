#!/usr/bin/env python3
# num.py - Simplest class Num with one integer field


class Num(object):
    
    __cont = 0

    def __init__(self, content):
        self.__cont = content

    def value(self):
        return self.__cont

    def __str__(self):
        return str(self.value())

    def __repr__(self):
        return "Num(" + str(self) + ")"

    def __eq__(self, other):
        return self.value() == other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __bool__(self):
        return self.value() != 0

    def __hash__(self):
        return hash(self.value())

    def plus(self, b):
        return Num(self.value() + b.value())

    def divide_by(self, b):
        return Num(self.value()//b.value())


def main():
    """
    Main method.
    """
    a1 = Num(-6)
    # a2 = a1
    a2 = Num(9)
    s = a1.plus(a2)
    print(str(s))
    print(a1 == a2)
    print(a1 != a2)
    print(a1 is a2)
    print(a1 > a2)
    print(a1 >= a2)
    print(a1 < a2)
    print(a1 <= a2)
    print(a1)
    print(repr(a1))
    print(bool(a1))
    print(hash(a1))
    print(Num(5).divide_by(Num(2)))


if __name__ == '__main__':
    main()
