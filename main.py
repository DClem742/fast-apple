import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from db import get_session 
from models.ceos import Ceo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "I like bacon"}

@app.get("/ceos")
def list_ceos(session: Session = Depends(get_session)):
    statement = select(Ceo)
    print(f"SQL STATEMENT: {statement}")
    results = session.exec(statement)
    return results.all()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)