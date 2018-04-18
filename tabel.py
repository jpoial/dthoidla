for i in range(1, 10):
    # print(str(i) + " " + str(i*i) + " " + str(i*i*i))
    print("{0:>2} {1:>3} {2:>4} {3:>5}".format(i, i*i, i*i*i, i*i*i*i))
for i in range(1, 0x10):
    print()
    for j in range(1, 0x10):
        print("{0:>4x}".format(i*j), end='')
