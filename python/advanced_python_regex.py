from collections import defaultdict
import csv

csvFilename = 'faculty.csv'
ddeg = defaultdict(int)
dtitle = defaultdict(int)
emails = []
domains = set()

csv.register_dialect('whitespace', delimiter=',', skipinitialspace=True)
with open(csvFilename) as fin:
    rdr = csv.DictReader(fin, dialect='whitespace')
    for row in rdr:
        deg = row['degree'].translate(None, '.')
        ddeg[deg] += 1
        dtitle[row['title']] += 1
        email = row['email']
        emails.append(email)
        ed = email.split('@')
        domains.add(ed[1])

print "Q1. There are %d different degrees with frequenices:<br/>" % len(ddeg)
for key, value in ddeg.iteritems():
    print key, ':', value, '<br/>'

print "Q2. There are %d different titles with frequenices:<br/>" % len(dtitle)
for key, value in dtitle.iteritems():
    print key, ':', value, '<br/>'

print "Q3. Email addreses are:<br/>"
for email in emails:
    print email, '<br/>'

print "Q4. There are %d different email domains:<br/>" % len(domains)
for value in domains:
    print value, '<br/>'
