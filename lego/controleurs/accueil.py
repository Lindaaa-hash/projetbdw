from model.model_pg import count_instances
from jinja2 import Template
import psycopg
from psycopg import sql
import toml
import random

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
    
def get_random_pieces(conn, limit=4):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT * 
            FROM piece
            WHERE longueur <= 2 OR largeur <= 2
            ORDER BY RANDOM()
            LIMIT %s;
        """, (limit,))
        return cursor.fetchall()

def select_piece():
    conn = get_connection()
    if request.method == "POST":
        selected_id = request.form.get("selected_piece")

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM piece WHERE id = %s;", (selected_id,))
            selected_piece = cursor.fetchone()

        print("Piece choisie: ", selected_piece)

        # Replace with a new random
        new_piece = get_random_pieces(conn, limit=1)[0]
        print("Nouvelle piece:", new_piece)
        