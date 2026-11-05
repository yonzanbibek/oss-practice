import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="lama bibek")
args = parser.parse_args()

rows = [
    ["Student Name", args.name],
    ["ID","23120163"],
    ["Major", "Information Security"],
    ["Course", "Open Source Software"],
    ["Library Used", "tabulate"]
]

print(tabulate(rows, headers=["Field", "Information"], tablefmt="grid"))