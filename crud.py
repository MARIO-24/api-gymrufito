import pymysql
from database import get_connection
from models import ClienteCreate, ClienteUpdate
# -----------------
# CRUD CLIENTES
# -----------------

def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def obtener_cliente(id_cliente: int):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM clientes WHERE id_cliente=%s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente

def crear_cliente(cliente: ClienteCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO clientes (nombre, apellidos, fecha_nacimiento, plan_contratado, activo, telefono, correo, direccion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        cliente.nombre,
        cliente.apellidos,
        cliente.fecha_nacimiento,
        cliente.plan_contratado,
        True,
        cliente.telefono,
        cliente.correo,
        cliente.direccion
    ))
    conn.commit()
    nuevo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return nuevo_id

def actualizar_cliente(id_cliente: int, cliente: ClienteUpdate):
    """Actualiza un cliente existente"""
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE clientes
        SET nombre=%s,
            apellidos=%s,
            fecha_nacimiento=%s,
            plan_contratado=%s,
            activo=%s,
            telefono=%s,
            correo=%s,
            direccion=%s
        WHERE id_cliente=%s
    """
    cursor.execute(sql, (
        cliente.nombre,
        cliente.apellidos,
        cliente.fecha_nacimiento,
        cliente.plan_contratado,
        cliente.activo,
        cliente.telefono,
        cliente.correo,
        cliente.direccion,
        id_cliente
    ))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_cliente(id_cliente: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()