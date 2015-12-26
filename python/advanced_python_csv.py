import csv

rFilename = 'faculty.csv'
wFilename = 'emails.csv'

csv.register_dialect('whitespace', delimiter=',', skipinitialspace=True)
with open(rFilename) as fr:
    rdr = csv.DictReader(fr, dialect='whitespace')
    with open(wFilename, 'w') as fw:
        for row in rdr:
            fw.write(row['email'] + '\n')
