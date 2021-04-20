import pymysql

conn = pymysql.connect(host="localhost", user="root", password="java", db="python", charset="utf8")
# try:
#     curs = conn.cursor()
#     sql = "delete from sample where col01='5'"
#     curs.execute(sql, '')
#     conn.commit()
# finally:
#     conn.close()

conn = pymysql.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'java', 
    db = 'python', 
    charset = 'utf8'
)
curs = conn.cursor()
sql = "delete from sample where col01='5'"
cnt = curs.execute(sql)
print("cnt:", cnt)


conn.commit()   

conn.close()
    
