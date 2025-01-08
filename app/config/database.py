from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Conexões para múltiplos bancos
DATABASES = {
    "memoria_inovabot": os.getenv("MEMORIA_DB_URL", "postgresql://postgres:cf715447d23c8e8187b4668ca96c2524@postgres:5432/memoria_Inovabot"),
    "crewai_db": os.getenv("CREWAI_DB_URL", "postgresql://postgres:cf715447d23c8e8187b4668ca96c2524@postgres:5432/crewai_db")
}

# Criar motores de conexão
engines = {name: create_engine(url) for name, url in DATABASES.items()}

# Função para obter a conexão correta
def get_engine(db_name: str):
    return engines.get(db_name)

# Função para gerenciar sessões do banco
def get_db_session(db_name: str):
    engine = get_engine(db_name)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
