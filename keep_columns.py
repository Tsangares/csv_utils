#!/usr/bin/env python3
import argparse,csv

parser = argparse.ArgumentParser(description=" specified columns of csv")
parser.add_argument('inputFile', type=str, help="Input CSV File")
parser.add_argument('outputFile', type=str, help="Output CSV File")
parser.add_argument('columns', nargs='+',type=str, help="columns to keep")
args = parser.parse_args()


reader = csv.DictReader(open(args.inputFile,encoding='cp1252'),quotechar='"',quoting=csv.QUOTE_ALL,delimiter=',',skipinitialspace=True)
dropColumns = [c for c in reader.fieldnames if c not in args.columns]
print("Dropping",dropColumns)
print("Keeping",args.columns)
writer = csv.DictWriter(open(args.outputFile,'w+'),fieldnames=args.columns)
writer.writeheader()
for row in reader:
    line = {key:value for key,value in row.items() if key in args.columns}
    writer.writerow(line)
print(f"Finished writing to {args.outputFile}")
