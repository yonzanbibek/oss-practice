import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["Developer", "lama bibek"],
    ["Library", "tabulate"],
    ["Status", "Complete"]
]
print(tabulate(rows, tablefmt="grid"))