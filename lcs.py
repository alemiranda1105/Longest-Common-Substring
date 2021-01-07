from argparse import ArgumentParser
from Greedy import *
from Memoization import *
from Tabulation import *
import DataReader as dr
import time


def args_creator():
    parser = ArgumentParser()

    parser.add_argument("-d", "--directory", action="store", dest="directory", default="", help="directory (process many files)", metavar="[DIRECTORY]")
    parser.add_argument("-f", "--file", action="store", dest="file", default="", help="file (process a single file)", metavar="[FILE]")

    parser.add_argument("-t", "--time", action="store_true", dest="timer", default=False, help="Display time")
    parser.add_argument("-v", "--value", action="store_true", dest="showValue", default=False, help="Display value")

    parser.add_argument("-sg", "--greedy", action="store_true", dest="greedy", default=False, help="Solve it with Greedy")
    parser.add_argument("-sm", "--memoization", action="store_true", dest="memoization", default=False, help="Solve it with Memoization")
    parser.add_argument("-st", "--tabulation", action="store_true", dest="tabulation", default=False, help="Solve it with Tabulation")

    parser.add_argument("-check", "--check", action="store_true", dest="check", default=False, help="Check if memoization and tabulation return the same value")

    return parser.parse_args()


def withDirectory(files):
    t = time.time()
    for f in files:
        print("----------" + f + "----------")
        withFile(f)
    print("<<<< END >>>>")
    if args.timer:
        t = time.time() - t
        print("Total execution time = ", t, "s")
    exit(0)


def withFile(file):
    s1, s2 = dr.readFile(file)
    t0 = 0
    t1 = 0
    if args.greedy:
        print("Solving it with Greedy")
        t0 = time.time()
        value = greedy(s1, s2)
        t1 = time.time()
    elif args.memoization:
        print("Solving it with Memoization")
        t0 = time.time()
        value = memoization(s1, s2)
        t1 = time.time()
    elif args.tabulation:
        print("Solving it with Tabulation")
        t0 = time.time()
        value = tabulation(s1, s2)
        t1 = time.time()
    elif args.check:
        mem = memoization(s1, s2)
        tab = tabulation(s1, s2)
        print("Check:", (mem == tab))
        print("Memoization =", mem)
        print("Tabulation =", tab)
    else:
        print("Introduzca un metodo, por favor")
        exit(-1)

    if args.showValue and not args.check:
        print(value)
    if args.timer:
        t = (t1 - t0)
        print("Time =", round(t, 3), "s")


if __name__ == '__main__':
    args = args_creator()
    if args.directory != "":
        files = dr.readAllFiles(args.directory)
        withDirectory(files)
    elif args.file != "":
        withFile(args.file)
    else:
        print("Introduzca un fichero, por favor")
        exit(-1)