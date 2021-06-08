import pymysql
from opensql import exec_sql_file

# password = input("Mot de passe de de la base de données (\"root\" par défaut) :")
password = input('Entrez le mot de passe de votre base de données :')  # Use your password.
login = pymysql.connect(user='root',
                        password=password,
                        host='localhost',
                        charset='utf8mb4')
cur = login.cursor()
exec_sql_file(cur, 'db.sql')
