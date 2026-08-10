Tablas:
- clientes(id PK, nombre, cuit)
- productos(id PK, nombre, precio_unitario)
- ventas(id PK, cliente_id FK -> clientes.id, producto_id FK -> productos.id, fecha, cantidad)

"""

SCHEMA_EXAMPLE = """
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2)
);

CREATE TABLE ventas (
    id INT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    fecha DATE,
    cantidad INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);
"""
