import pytest
from app import app

# Constantes de configuración de pruebas
C_TESTING = True
C_HTTP_OK = 200
C_RUTA_HOME = "/"
C_RUTA_HEALTH = "/health"
C_CLAVE_STATUS = "status"
C_STATUS_OK = "ok"
C_STATUS_HEALTHY = "healthy"

# PROCEDIMIENTO: P_CLIENT
# Crea un cliente de prueba para simular peticiones HTTP a la app
@pytest.fixture
def P_CLIENT():
  app.config["TESTING"] = C_TESTING
  with app.test_client() as V_CLIENT:
    yield V_CLIENT

# PRUEBA: T_HOME
# Prueba que la ruta principal responde correctamente
def T_HOME(P_CLIENT):
  V_RESPUESTA = P_CLIENT.get(C_RUTA_HOME)
  assert V_RESPUESTA.status_code == C_HTTP_OK
  V_DATA = V_RESPUESTA.get_json()
  assert V_DATA[C_CLAVE_STATUS] == C_STATUS_OK

# PRUEBA: T_HEALTH
# Prueba que la ruta de salud responde correctamente
def T_HEALTH(P_CLIENT):
  V_RESPUESTA = P_CLIENT.get(C_RUTA_HEALTH)
  assert V_RESPUESTA.status_code == C_HTTP_OK
  V_DATA = V_RESPUESTA.get_json()
  assert V_DATA[C_CLAVE_STATUS] == C_STATUS_HEALTHY
