from fastapi import APIRouter
from sqlalchemy import text
from app.config.database import get_engine

router = APIRouter()

@router.get("/test_crewai_db")
def test_crewai_db():
    """
    Testa a conexão com o banco crewai_db e retorna as tabelas existentes.
    """
    engine = get_engine("crewai_db")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"))
            # Corrigir o formato para garantir acesso como dicionário
            tables = [row[0] for row in result]  # Acessa o primeiro elemento da tupla
            return {"status": "success", "tables": tables}
    except Exception as e:
        return {"status": "error", "message": str(e)}
