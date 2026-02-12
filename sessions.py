import uuid

# 1. Almacenamiento en memoria (Diccionario)
# ¡Cuidado! Si reinicias el servidor, todas las sesiones desaparecen.
# Formato: {"codigo-uuid-largo": id_del_usuario}
SESSIONS = {}

def create_session(user_id: int):
    """
    Crea un identificador único para el usuario y lo guarda en el diccionario.
    """
    # Genera un ID aleatorio e irrepetible (ej: '550e8400-e29b...')
    session_id = str(uuid.uuid4())
    
    # Guarda la relación: ID de sesión -> ID de usuario
    SESSIONS[session_id] = user_id
    
    # Retorna el token que se enviará al navegador/cliente
    return session_id

def get_user_from_session(session_id: str):
    """
    Busca si existe un usuario vinculado a un ID de sesión específico.
    """
    # .get() devuelve el user_id si existe, o None si la sesión no es válida
    return SESSIONS.get(session_id)