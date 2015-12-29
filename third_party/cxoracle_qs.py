import cx_Oracle
import pprint

def column_names_from_cursor(cur):
    """returns column names as a list when provided cx_Oracle Cursor"""

    column_names = []
    for column_info in cur.description:
        column_names.append(column_info[0])
    return column_names

def rows_as_dicts(cur):
    """returns rows as dictionaries in a generator when
    provided cx_Oracle Cursor"""

    columns = column_names_from_cursor(cur)
    for row in cur:
        yield dict(zip(columns, row))


host = 'localhost'
port = 1521
sid = 'TEST'
username = 'test'
password = 'testpwd'
dsn_tns = cx_Oracle.makedsn(host, port, sid)

conn = cx_Oracle.connect(username, password, dsn_tns)
cursor = conn.cursor()
cursor.execute('SELECT * from SOME_TABLE')

for row in rows_as_dicts(cursor):
    pprint.pprint(row)

cursor.close()
conn.close()
