import csv

csv.register_dialect('albums', escapechar='\\', quoting=csv.QUOTE_NONE)

with open('rock.csv', 'rb') as f:
    reader = csv.reader(f, dialect='albums')
    for row in reader:
        print row

print "-----"

with open('rock.csv', 'rb') as f:
    reader = csv.DictReader(f, dialect='albums')
    for row in reader:
        print row

rows = [("Rainbow", "Long Live Rock 'n' Roll", 1978),("Black Sabbath","Dehumanizer", 1992), ("Helloween", "Keeper of the Seven Keys, Pt. 2", 1988)]
with open('rock_py.csv', 'wb') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(rows)
