from sqlalchemy import create_engine

DB_USER = "airflow"
DB_PASSWORD = "airflow"
DB_HOST = "postgres"  
DB_PORT = "5432"
DB_NAME = "airflow"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print(result.fetchone())