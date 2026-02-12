from sqlalchemy import Column, Integer, String
from db import Base  # Importamos la Clase Base que definimos en el archivo anterior

# Definimos la clase que representará a nuestra tabla de usuarios
class User(Base):
    # Nombre de la tabla dentro de la base de datos SQL
    __tablename__ = "users"

    # Definición de las columnas:
    
    # Identificador único (ID). Es la Llave Primaria y está indexado para búsquedas rápidas.
    id = Column(Integer, primary_key=True, index=True)
    
    # Correo del usuario. Debe ser único (no repetido) e indexado.
    email = Column(String, unique=True, index=True)
    
    # Contraseña (usualmente guardamos el hash, no el texto plano por seguridad)
    password_hash = Column(String)