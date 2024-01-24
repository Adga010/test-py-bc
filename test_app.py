import unittest
from app import app

class TestWebServices(unittest.TestCase):
    # setUp es un método especial que se ejecuta antes de cada prueba unitaria.
    # Se usa para configurar cualquier estado o configuración inicial necesaria para las pruebas.
    def setUp(self):
        # Aquí, se crea un cliente de prueba para la aplicación Flask.
        # Este cliente se usará para simular solicitudes HTTP a tu aplicación Flask.
        self.app = app.test_client()

    # Esta es una prueba unitaria que verifica el funcionamiento del endpoint '/top5-dense-countries'.
    def test_top_five_dense_countries(self):
        # Realiza una solicitud GET al endpoint y guarda la respuesta.
        response = self.app.get("/top5-dense-countries")
        # Verifica que el código de estado HTTP de la respuesta sea 200, lo cual indica éxito.
        self.assertEqual(response.status_code, 200)
        # Comprueba que la longitud de la respuesta JSON sea exactamente 5, esperando 5 países.
        self.assertTrue(len(response.json) == 5)

    # Esta prueba verifica que el formato de los datos de la respuesta sea correcto.
    def test_response_data_format(self):
        # Realiza una solicitud GET al mismo endpoint.
        response = self.app.get("/top5-dense-countries")
        # Itera sobre cada país en la respuesta JSON.
        for country in response.json:
            # Comprueba que cada país tenga un campo 'name'.
            self.assertIn("name", country)
            # Comprueba que cada país tenga un campo 'density'.
            self.assertIn("density", country)

    # Esta prueba se asegura de que los valores de densidad sean razonables (no negativos).
    def test_density_values(self):
        # Nuevamente, realiza una solicitud GET al endpoint.
        response = self.app.get("/top5-dense-countries")
        # Revisa cada país en la respuesta.
        for country in response.json:
            # Verifica que la densidad sea mayor o igual a 0.
            # Esto es importante para asegurarse de que la densidad demográfica se calcula correctamente.
            self.assertGreaterEqual(country["density"], 0)

# Estas líneas verifican si el script se está ejecutando como el script principal y, de ser así, ejecutan las pruebas.
if __name__ == "__main__":
    unittest.main()
