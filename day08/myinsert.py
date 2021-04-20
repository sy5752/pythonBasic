import pymysql


conn = pymysql.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'java', 
    db = 'python', 
    charset = 'utf8'
)
curs = conn.cursor()
sql = "insert into sample (col01, col02, col03) values ('5', '5', '5')"
cnt = curs.execute(sql)
print("cnt:", cnt)


conn.commit()   

conn.close()
