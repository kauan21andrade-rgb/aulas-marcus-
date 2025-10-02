from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./erp.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    estoque = Column(Integer)

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
    class Config:
        orm_mode = True
        from sqlalchemy.orm import Session
import models, schemas

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    db_prod = models.Produto(**produto.dict())
    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)
    return db_prod

def listar_produtos(db: Session):
    return db.query(models.Produto).all()
    from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtos/", response_model=schemas.Produto)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@app.get("/produtos/", response_model=list[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)
    import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("ERP - Comércio Pequeno")

menu = ["Produtos", "Clientes", "Pedidos"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Produtos":
    st.header("Cadastro de Produtos")
    nome = st.text_input("Nome")
    preco = st.number_input("Preço", min_value=0.0)
    estoque = st.number_input("Estoque", min_value=0)

    if st.button("Cadastrar"):
        res = requests.post(f"{API_URL}/produtos/", json={
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        })
        if res.status_code == 200:
            st.success("Produto cadastrado!")

    st.subheader("Lista de Produtos")
    produtos = requests.get(f"{API_URL}/produtos/").json()
    for p in produtos:
        st.write(f"{p['id']} - {p['nome']} | R$ {p['preco']} | Estoque: {p['estoque']}")
        python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app:app --reload
streamlit run frontend/main.py