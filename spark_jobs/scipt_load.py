import psycopg2
from datetime import datetime

# Datos de conexión
conexion = psycopg2.connect(
    host="192.168.1.135",
    database="usuari_db",
    user="airflow",
    password="airflow",  # Reemplaza con tu contraseña real
    port=5432
)

# Crear cursor
cursor = conexion.cursor()

# Lista de usuarios a insertar
usuarios = [
    ("Ana Torres", "ana.torres@example.com"),
    ("Luis Mejía", "luis.mejia@example.com"),
    ("Carmen Ruiz", "carmen.ruiz@example.com"),
    ("Pedro Gómez", "pedro.gomez@example.com"),
    ("Valeria León", "valeria.leon@example.com"),
]

# Ejecutar inserciones
for nombre, correo in usuarios:
    cursor.execute("""
        INSERT INTO usuario_tabla (nombre, correo)
        VALUES (%s, %s)
    """, (nombre, correo))

# Guardar cambios
conexion.commit()
print("✅ Usuarios insertados exitosamente.")

# Cerrar conexión
cursor.close()
conexion.close()
