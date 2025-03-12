# import functionality for sqlite
import sqlite3

#  connects to db if it exists otherwise it creates it locally
connection = sqlite3.connect('pokemon.db')

# tool to execute sql commands on db
cursor = connection.cursor()

# create tabe in db
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    territory TEXT NOT NULL
    )
    ''')
    connection.commit()

create_table()

def add_pokemon(name, poketype, territory):
    cursor.execute('''
    INSERT INTO pokemon (name, type, territory)
    VALUES (?, ?, ?)
    ''', (name, poketype, territory))
    connection.commit()

# add_pokemon("Bulbasaur", "Grass", "Kanto Pokemon Lab")

def read_all_pokemon():
    cursor.execute("SELECT * FROM pokemon")
    pokemon = cursor.fetchall()
    for mon in pokemon:
        print(mon)

def update_pokemon(dex_id, name):
    cursor.execute('''
    UPDATE pokemon
    SET name = ?
    WHERE id = ?
    ''', (name, dex_id))
    connection.commit()


add_pokemon("Venusaur", "Grass, Poison", "Kanto")
# read_all_pokemon()

def delete_pokemon(dex_id):
    cursor.execute('''
    DELETE FROM pokemon
    WHERE id = ?
    ''', (dex_id,))
    connection.commit()

# delete_pokemon(3)
read_all_pokemon()