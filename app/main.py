from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from database import engine, Base, get_session
from models import Pokemon
from schemas import PokemonCreate, Pokemon as PokemonSchema
from crud import get_all_pokemons, create_pokemon

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/api/v1/pokemons/", response_model=PokemonSchema)
async def create_pokemon_endpoint(pokemon: PokemonCreate, session: AsyncSession = Depends(get_session)):
    return await create_pokemon(session, pokemon)

@app.get("/api/v1/pokemons/", response_model=list[PokemonSchema])
async def read_pokemons(name: str = None, type: str = None, session: AsyncSession = Depends(get_session)):
    return await get_all_pokemons(session, name, type)
