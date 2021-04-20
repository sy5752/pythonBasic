import pymysql
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "select s_price,in_time from stock WHERE s_name = '삼성전자' order by in_time desc  "
curs.execute(sql)
rows = curs.fetchall()

print(rows) 
 
prices = []    
for row in rows :
    prices.append(row[0])
    
print(prices)    

conn.close()
