import pymysql

conn = pymysql.connect(host="localhost", user="root", password="java", db="python", charset="utf8")
try:
    curs = conn.cursor()
    sql = "update sample set col01='0', col02='0', col03='0' where col01='5'"
    curs.execute(sql)
    conn.commit()
finally:
    conn.close()