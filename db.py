from sqlmodel import create_engine, SQLModel, Session

DATABSE_URL = "postgresql://postgres.bveaeajkjyrnfjvhctcx:Sumerian5588!*@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABSE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session