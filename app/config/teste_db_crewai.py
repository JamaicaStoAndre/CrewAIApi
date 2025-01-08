DATABASE_URL = "postgresql://postgres:cf715447d23c8e8187b4668ca96c2524@localhost:5432/crewai_db"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Conexão com crewai_db bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao crewai_db:", e)
