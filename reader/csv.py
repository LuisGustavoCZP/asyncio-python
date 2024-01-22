import csv

def read_csv(path):
    result = ""
    with open(path, newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            result += (', ').join(row)
    return result
    