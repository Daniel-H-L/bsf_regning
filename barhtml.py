#!/usr/bin/python3
import csv
import argparse
from datetime import date
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

vals = {}

def main():
    parser = argparse.ArgumentParser(description="Lag regninger")
    parser.add_argument('bsf_dato')
    args = parser.parse_args()

    env = Environment(
        loader = FileSystemLoader('C:\users\Daniel\documents\ovefiler\\')
        autoescape = select_autoescape('html')
    )
    template = env.get_template("regning.html")
    for entry in os.scandir('.'):
        if entry.is_dir():
            print("Gjeng", entry.name)
            bill = gen_bill(entry.path)
            ordered_bill = sorted([(k, bill[k]) for k in bill], key=lambda x: x[0])
            total = sum(bill[k] for k in bill)
            html = template.render(
                    gjeng = entry.name,
                    rows = ordered_bill,
                    total = total,
                    date = args.bsf_dato
                )
            with open(entry.name + ".html", 'w') as f:
                f.write(html)

def gen_html(bill):
    return ""

def gen_bill(gjeng):
    bill = {}
    for entry in os.scandir(gjeng):
        if entry.is_file() and entry.name.split(".")[1] == "csv":
            with open(entry.path) as f:
                reader = csv.reader(f)
                for k, v in reader:
                    bill[k] = bill.get(k, 0) + int(v)
    return bill

if __name__ == '__main__':
    main()
