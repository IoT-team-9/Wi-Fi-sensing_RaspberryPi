import sqlite3

# create db 
# connect to db file(csi-db.db)
connection = sqlite3.connect('csi-data.db')
cursor = connection.cursor()

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS csi-data (
    timestamp TEXT,
    label varchar(255)
)'''
)

# save to db
connection.commit()