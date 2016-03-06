import csv


# reading

with open('guitars.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

print "-----"

with open('guitars.csv', 'rb') as f:
    # values in first row used if fieldnames parameter omitted
    reader = csv.DictReader(f)
    for row in reader:
        print row

print "-----"


# reading with a dialect - https://docs.python.org/2/library/csv.html#csv-fmt-params
# reader, DictReader, writer, DictWriter default to csv.excel

csv.register_dialect('albums', escapechar='\\', quoting=csv.QUOTE_NONE)

with open('rock.csv', 'rb') as f:
    reader = csv.reader(f, dialect='albums')
    for row in reader:
        print row

print "-----"

with open('rock.csv', 'rb') as f:
    field_names = ["Artist", "Album", "Year"]
    reader = csv.DictReader(f, fieldnames=field_names, dialect='albums')
    for row in reader:
        print row


# writing

rows = [("Rainbow", "Long Live Rock 'n' Roll", 1978), ("Black Sabbath", "Dehumanizer", 1992), ("Helloween", "Keeper of the Seven Keys, Pt. 2", 1988), ("David Bowie", '"Heroes"', 1977)]
with open('rock_out.csv', 'wb') as f:
    print "wrote file rock_out.csv"
    writer = csv.writer(f)
    writer.writerows(rows)

with open('guitars_out.csv', 'wb') as f:
    print "wrote file guitars_out.csv"
    # fieldnames defines the order fields are written since dictionaries are not ordered
    # all dictionary keys must be present in fieldnames (ValueError) but not vice versa
    field_names = ["Make", "Model", "Finish"]
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'Make': "Gibson", 'Model': "Les Paul Custom", 'Finish': "Black"})
    writer.writerow({'Make': "Ibanez", 'Finish': "Desert Red", 'Model': "RT150"})
    writer.writerow({'Model': "CE", 'Finish': "Vintage Sunburst", 'Make': "PRS"})
