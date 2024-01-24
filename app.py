from flask import Flask, jsonify
import requests

# Crear una instancia de la aplicación Flask.
# Flask usa esta instancia para manejar las solicitudes y respuestas.
app = Flask(__name__)


# Definir una ruta para el endpoint '/top5-dense-countries'.
# El decorador app.route asocia la URL con la función definida debajo.
@app.route("/top5-dense-countries")
def top_five_dense_countries():
    # Realizar una solicitud HTTP GET a la API externa de países.
    # Esta API proporciona datos sobre todos los países.
    response = requests.get("https://restcountries.com/v3.1/all")
    # Convertir la respuesta JSON de la API en una lista de diccionarios de Python.
    countries = response.json()

    # Calcular la densidad demográfica de cada país.
    # La densidad se calcula como la población dividida por el área.
    # Se incluye una comprobación para evitar la división por cero.
    for country in countries:
        country["density"] = (
            country["population"] / country["area"] if country["area"] > 0 else 0
        )

    # Ordenar los países por densidad demográfica en orden descendente y seleccionar los 5 primeros.
    top_countries = sorted(countries, key=lambda x: x["density"], reverse=True)[:5]

    # Crear una lista de diccionarios con la información formateada de los 5 países principales.
    # Cada diccionario contiene el nombre y la densidad demográfica del país.
    result = [
        {"name": country["name"]["common"], "density": country["density"]}
        for country in top_countries
    ]

    # Devolver la respuesta en formato JSON utilizando jsonify,
    # que convierte la lista de diccionarios en una respuesta JSON adecuada.
    return jsonify(result)


# Comprobar si el script es el punto de entrada principal y, en ese caso, ejecutar la aplicación.
# Esto inicia el servidor web de Flask en modo de depuración, que es útil durante el desarrollo.
if __name__ == "__main__":
    app.run(debug=True)
