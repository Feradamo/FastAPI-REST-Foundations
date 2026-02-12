from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Dirección de la base de datos (SQLite en este caso)
# "sqlite:///./app.db" crea un archivo local llamado app.db en la misma carpeta
DATABASE_URL = "sqlite:///./app.db"

# 2. El Motor (Engine): Es el corazón de la conexión
# 'check_same_thread': False es necesario SOLO para SQLite en apps web (como FastAPI)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Fábrica de Sesiones: Genera los objetos que usaremos para hacer consultas
# autoflush=False: No envía cambios a la DB hasta que tú lo indiques
# autocommit=False: No confirma los cambios permanentemente hasta que uses session.commit()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 4. Clase Base: De aquí heredarán todos tus modelos (tablas)
# Es la que se encarga de "mapear" tus clases de Python a tablas de SQL
Base = declarative_base()