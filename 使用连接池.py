from sqlhelper2 import db

# db.fetchone('...')
#
# db.fetchall('...')

'''
conn, cursor = db.open()
cursor.excute('...')
result = cursor.fetchmany(4)
db.close(conn, cursor)
'''

with db as cur:
    cur.execute('select * from student')
    result = cur.fetchmany(4)
