#!/usr/bin/env python3

import atexit
import concurrent.futures
import os
import shutil


def create_big_files(n=os.cpu_count(), prefix='bigfile'):
    print("Creating {} big files".format(n))
    numbs = list(range(n))
    first = numbs.pop(0)

    def get_fn(number):
        return '{}{}.con.txt'.format(prefix, number)

    basefile = get_fn(first)

    # This will delete file when script exits
    atexit.register(os.remove, basefile)

    with open(basefile, 'w') as f:
        for i in range(30000000):
            f.write("{}\n".format(i))

    for n in numbs:
        dest = get_fn(n)
        shutil.copyfile(basefile, dest)

        atexit.register(os.remove, dest)


def count(fn):
    cntr = 0
    with open(fn) as f:
        for l in f:
            cntr += 1
    return cntr


def main():
    print("Running in concurrent mode")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        files = os.listdir()
        txts = [f for f in files if f.endswith('.con.txt')]
        for fn, c in zip(txts, executor.map(count, txts)):
            print(fn, c)


def sequential():
    print("Running in sequential mode")
    files = os.listdir()
    txts = [f for f in files if f.endswith('.txt')]
    for f in txts:
        print(f, count(f))


if __name__ == "__main__":
    print("This machine has {} CPUs".format(os.cpu_count()))

    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('-s', help='Sequential mode')
    argp.add_argument('-c', help='Concurrent mode')
    argp.add_argument('-i', help='Create files')
    argp.add_argument('-a', help='Run all')
    args = argp.parse_args()

    if args.s:
        sequential()
    elif args.c:
        main()
    elif args.i:
        create_big_files()
    else:
        import time
        create_big_files()
        start = time.time()
        sequential()
        print('Took {} seconds'.format(time.time() - start))
        start = time.time()
        main()
        print('Took {} seconds'.format(time.time() - start))
