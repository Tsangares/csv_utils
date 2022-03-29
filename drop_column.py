#!/usr/bin/env python3
import argparse,csv

parser = argparse.ArgumentParser(description="Drop specified columns of csv")
parser.add_argument('inputFile', type=str, help="Input CSV File")
parser.add_argument('outputFile', type=str, help="Output CSV File")
parser.add_argument('columns', nargs='+',type=str, help="columns to drop")
args = parser.parse_args()


reader = csv.DictReader(open(args.inputFile),quotechar='"',quoting=csv.QUOTE_ALL,delimiter=',',skipinitialspace=True)
columns = [c for c in reader.fieldnames if c not in args.columns]
print(columns)
writer = csv.DictWriter(open(args.outputFile,'w+'),fieldnames=columns)
writer.writeheader()
for row in reader:
    for column in args.columns:
        del row[column]
    writer.writerow(row)
print(f"Finished writing to {args.outputFile}")
