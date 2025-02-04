from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_engine

router = APIRouter()

@router.post("/")
def create_automation(name: str, description: str, db: Session = Depends(lambda: get_db_session("crewai_db"))):
    """
    Cria uma nova automação.
    """
    query = f"INSERT INTO automations (name, description) VALUES (:name, :description) RETURNING automation_id;"
    try:
        with db.connection() as conn:
            result = conn.execute(query, {"name": name, "description": description})
            return {"automation_id": result.fetchone()[0]}
    except Exception as e:
        return {"detail": f"Erro ao criar automação: {e}"}
