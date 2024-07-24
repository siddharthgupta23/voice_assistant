import sqlite3
conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()
query= "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'one note 2016','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote 2016')"
# cursor.execute(query)
# conn.commit()

# query="CREATE TABLE IF NOT EXISTS web_content(id integer primary key, name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO web_content  VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

app_name="android studio"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
results=cursor.fetchall()
print(results[0][0])