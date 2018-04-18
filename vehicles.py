#!/usr/bin/env python3


class Vehicle(object):
    def __str__(self):
        return 'vehicle'


class Car(Vehicle):
    def __str__(self):
        return super().__str__() + ' named car'


class Boat(Vehicle):
    def __str__(self):
        return super().__str__() + ' named boat'


class Amphibian(Car, Boat):
    def __str__(self):
        return super().__str__() + ' named amphibian'


def main():
    """
    Main method.
    """
    v1 = Vehicle()
    print(v1)
    c1 = Car()
    print(c1)
    b1 = Boat()
    print(b1)
    a1 = Amphibian()
    print(a1)


if __name__ == '__main__':
    main()

