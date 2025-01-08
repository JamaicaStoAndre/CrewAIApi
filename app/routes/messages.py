from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from app.config.database import get_engine

router = APIRouter()

@router.get("/messages_yesterday/")
def get_messages_yesterday(telefone: str = Query(..., description="Número de telefone")):
    """
    Busca mensagens enviadas no dia anterior para um telefone específico.
    """
    try:
        query = text("""
            SELECT *
            FROM public."msg_gp_WA"
            WHERE to_timestamp("messageTimestamp")::date = (CURRENT_DATE - INTERVAL '1 day')
              AND "telefone" = :telefone
        """)

        # Conectar ao banco 'memoria_inovabot'
        engine = get_engine("memoria_inovabot")
        with engine.connect() as conn:
            result = conn.execute(query, {"telefone": telefone}).fetchall()
        
        # Converter resultados para JSON
        messages = [dict(row._mapping) for row in result]
        return {"messages": messages}

    except Exception as e:
        return {"detail": f"Erro ao executar consulta: {e}"}
