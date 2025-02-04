DATABASE_URL = "postgresql://postgres:XXXXX@localhost:5432/crewai_db"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Conexão com crewai_db bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao crewai_db:", e)
