from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Funcion para establecer conexion con la base de datos
def coneccion_db():
    try:
        conn = mysql.connector.connect(
            host="mysqlserver",
            user="root",
            password="12345",
            database="practica_docker"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: No se pudo establecer conexion con la base de datos. {err}")
        return None

# Funcion para obtener todos los usuarios de la base de datos
def obtener_usuarios():
    conn = coneccion_db()
    if conn is None:
        print("Error: No se pudo conectar a la DB.")
        return None
    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print(f"Error: No se pudo obtener los usuarios. {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/")
def index():
    usuarios = obtener_usuarios()
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)