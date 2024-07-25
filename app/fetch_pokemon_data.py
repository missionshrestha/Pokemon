import asyncio
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from schemas import PokemonCreate
from crud import create_pokemon

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"

async def fetch_pokemon_data(session: AsyncSession):
    async with httpx.AsyncClient() as client:
        response = await client.get(POKEAPI_URL)
        data = response.json()
        pokemons = data['results']
        for pokemon in pokemons:
            pokemon_detail = await client.get(pokemon['url'])
            detail_data = pokemon_detail.json()
            pokemon_create = PokemonCreate(
                name=detail_data['name'],
                image=detail_data['sprites']['front_default'],
                type=detail_data['types'][0]['type']['name']
            )
            await create_pokemon(session, pokemon_create)

async def main():
    async for session in get_session():
        await fetch_pokemon_data(session)

if __name__ == "__main__":
    asyncio.run(main())
