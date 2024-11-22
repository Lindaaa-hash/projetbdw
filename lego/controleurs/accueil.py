from model.model_pg import count_instances
from jinja2 import Template
import psycopg
from psycopg import sql
import toml

def get_connexion(host, username, password, db, schema):
    try:
        print("Attempting to connect to the database...")
        connexion = psycopg.connect(
            host=host,
            user=username,
            password=password,
            dbname=db,
            autocommit=True
        )
        
        cursor = connexion.cursor()
        cursor.execute("SET search_path TO %s", [schema])
        print("Connection established successfully!")
        
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
    return connexion


def accueil(request):
    print("accueil function called")
    config = toml.load('./config-bd.toml')
    connexion = get_connexion(config['SERVER'], config['USER'], config['PASSWORD'], config['DATABASE'], config['SCHEMA'])
    if connexion:
        print("Database connection established")
        res = count_instances(connexion, 'piece')
        print(f"Count instances result: {res}")
        piece = res[0][0]
        if piece > 0:
            message = f"Actuellement {piece} pieces dans la base."
        else:
            message = "Aucun lego dans la base."
        print(f"Message: {message}")
    print(message)