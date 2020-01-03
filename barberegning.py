#!/usr/bin/python3
import argparse
from datetime import date
import csv
import os

vals = {}

def main():
    parser = argparse.ArgumentParser(description="Før lister")
    parser.add_argument('gjeng')
    args = parser.parse_args()

    print("Legg inn tall for "+args.gjeng+"\n")

    while(True):
        try:
            readVal()
        except KeyboardInterrupt:
            print("\nLagrer...")
            saveVals(args.gjeng)
            exit()


def readVal():
    name = input("Navn: ")
    value = eval(input("Beløp: "))
    if name in vals:
        print("Feil! Du har allerede ført for denne personen")
    else:
        print("Beregnet verdi:", value)
        vals[name] = value
    print()


def saveVals(gjeng):
    if not os.path.exists(gjeng):
        os.makedirs(gjeng)
    datestr = date.today().isoformat()
    basename = os.path.join(gjeng,datestr)
    filename = basename + ".csv"
    index = 1
    while os.path.exists(filename):
        index = index + 1
        filename = basename + "_" + str(index) + ".csv"
    with open(filename, 'w') as f:
        w = csv.writer(f)
        w.writerows(vals.items())


if __name__ == '__main__':
    main()
