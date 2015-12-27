from collections import defaultdict
import csv

def printAnswer(qi, countElements, colName, col, iterator):
    """
    Prints a markdown friendly answer
    :param qi: question number
    :param countElements: count of items to print
    :param colName: variable name of col
    :param col: collection that contains results
    :param iterator: used for traversing col
    :return: pass
    """
    celem = min(len(col), countElements)
    print "A%d. the first %d items in %s are:<br/>" % (qi, celem, colName)
    try:
        i = 0
        while i < celem:
            key, value  = iterator.next()
            print key, ':', value, '<br/>'
            i += 1
    except StopIteration:
        pass


rFilename = 'faculty.csv'
faculty_dict = defaultdict(list)
professor_dict = defaultdict(list)
sorted_pairs = []

csv.register_dialect('whitespace', delimiter=',', skipinitialspace=True)
with open(rFilename) as fin:
    rdr = csv.DictReader(fin, dialect='whitespace')
    for row in rdr:
        # keys
        names = row['name'].split(' ')
        lastname = names[-1]
        firstname = names[0]
        if(firstname[-1] == '.' and len(names) > 2): # professor uses middle name as first
            firstname = names[1]

        # values
        deg = row['degree'].translate(None, '.')
        values = [deg, row['title'], row['email']]

        faculty_dict[lastname] = values
        professor_dict[(firstname, lastname)] = values

sorted_keys = sorted(professor_dict, key=lambda item: item[1])
for key in sorted_keys :
     value = professor_dict[key]
     pair = (key, value)
     sorted_pairs.append( pair )

printAnswer(6, 3, "faculty_dict", faculty_dict, faculty_dict.iteritems())
printAnswer(7, 3, "professor_dict", professor_dict, professor_dict.iteritems())
printAnswer(8, 3, "sorted_pairs", sorted_pairs, iter(sorted_pairs))

