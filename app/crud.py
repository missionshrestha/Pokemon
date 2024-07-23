from sqlalchemy.future import select
from app.models import Pokemon
from app.schemas import PokemonCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def get_pokemon_by_name(session: AsyncSession, name: str):
    result = await session.execute(select(Pokemon).filter(Pokemon.name == name))
    return result.scalars().first()

async def get_all_pokemons(session: AsyncSession, name: str = None):
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    result = await session.execute(query)
    return result.scalars().all()

async def create_pokemon(session: AsyncSession, pokemon: PokemonCreate):
    db_pokemon = Pokemon(**pokemon.dict())
    session.add(db_pokemon)
    await session.commit()
    await session.refresh(db_pokemon)
    return db_pokemon
