import mysql.connector

# MySQL 서버와 연결 -> !! 깃헙 push 전 암호화 필수 !!
mydb = mysql.connector.connect(
  host="****",
  user="****",
  password="****",
  database="****"
)