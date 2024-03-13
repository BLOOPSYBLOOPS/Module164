from flask import Flask
import pymysql

app = Flask(__name__)

#Configuration de la base de données
app.config['MYSQLHOST'] = 'localhost'  # Adresse IP ou nom d'hôte du serveur MySQL
app.config['MYSQLUSER'] = 'root'  # Nom d'utilisateur MySQL
app.config['MYSQLPASSWORD'] = ''  # Mot de passe MySQL
app.config['MYSQLDB'] = 'morattel_bryan_expi1a_mpd'  # Nom de la base de données

#Établir une connexion à la base de données
conn = pymysql.connect(host=app.config['MYSQL_HOST'],
                       user=app.config['MYSQL_USER'],
                       password=app.config['MYSQL_PASSWORD'],
                       database=app.config['MYSQL_DB'])

#Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

#Exemple : exécution d'une requête pour récupérer toutes les lignes d'une table nommée 'ma_table'
cursor.execute("SELECT * FROM t_compte")
rows = cursor.fetchall()

#Parcourir les résultats
for row in rows:
    print("chier ce module 164",row)

#Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()

if __name__ == '__main':
    app.run()