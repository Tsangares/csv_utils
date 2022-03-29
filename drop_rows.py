#!/usr/bin/env python3
import argparse,csv

parser = argparse.ArgumentParser(description="Drop specified columns of csv")
parser.add_argument('inputFile', type=str, help="Input CSV File")
parser.add_argument('outputFile', type=str, help="Output CSV File")
parser.add_argument('column',type=str, help="columns to filter on.")
parser.add_argument('values',nargs='+',type=str, help="Value to keep on.")
args = parser.parse_args()


reader = csv.DictReader(open(args.inputFile),quotechar='"',quoting=csv.QUOTE_ALL,delimiter=',',skipinitialspace=True)
writer = csv.DictWriter(open(args.outputFile,'w+'),fieldnames=reader.fieldnames)
writer.writeheader()
values = [v.lower().strip() for v in args.values]
for row in reader:
    if row[args.column].lower() in values:
        writer.writerow(row)
print(f"Finished writing to {args.outputFile}")
