
import redis.asyncio as redis
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Pokemon
from schemas import PokemonCreate
from config import REDIS_URL

redis_client = redis.from_url(REDIS_URL)

async def get_pokemon_by_name(session: AsyncSession, name: str) -> Pokemon:
    cache_key = f"pokemon:{name}"
    cached_pokemon = await redis_client.get(cache_key)
    if cached_pokemon:
        return Pokemon.parse_raw(cached_pokemon)
    
    result = await session.execute(select(Pokemon).filter(Pokemon.name == name))
    pokemon = result.scalars().first()
    if pokemon:
        await redis_client.set(cache_key, pokemon.json(), ex=3600)
    return pokemon

async def get_all_pokemons(session: AsyncSession, name: str = None) -> list[Pokemon]:
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    result = await session.execute(query)
    return result.scalars().all()

async def create_pokemon(session: AsyncSession, pokemon: PokemonCreate) -> Pokemon:
    db_pokemon = Pokemon(**pokemon.dict())
    session.add(db_pokemon)
    await session.commit()
    await session.refresh(db_pokemon)
    await redis_client.delete(f"pokemon:{db_pokemon.name}")
    return db_pokemon
