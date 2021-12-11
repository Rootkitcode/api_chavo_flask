from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)
# configuracion db

app.config['MYSQL_HOST'] = 'bn7l1v1nprncqduslm2j-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'urgancqyaq1ep6pv'
app.config['MYSQL_PASSWORD'] = 'urgancqyaq1ep6pv'
app.config['MYSQL_DB'] = 'bn7l1v1nprncqduslm2j'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
cors = CORS(app, resource={r"/*": {"origin": "*"}})


@app.route('/')
def getCharacters():
    lista = requests.get('https://chavo.s3.us-east-2.amazonaws.com/characters.json')

    return jsonify(lista.json())


@app.route('/character/<int:id>')
def getCharacterId(id):
    lista = requests.get('https://chavo.s3.us-east-2.amazonaws.com/characters.json')

    for element in lista.json():
        if (id == element["id"]):
            insertCharacter(element)
            return jsonify({"message":"Dato guardado exitosamente"})
        else:
            jsonify({"message": "usuario no encontrado"})

def insertCharacter(character):
    nombrePersonaje=character['name']
    categoriaPersonaje=character['category']
    frase=character['quote']
    url=character['url']
    cur=mysql.connection.cursor()
    cur.execute(f"INSERT INTO personajes(name, category, quote, url) VALUES('{nombrePersonaje}','{categoriaPersonaje}','{frase}','{url}')")

    mysql.connection.commit()
    cur.close()
    return jsonify({"message":"Personaje creado correctamente"})


if __name__ == '__main__':
    app.run(debug=True)