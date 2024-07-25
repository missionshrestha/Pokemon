import os

# Correctly URL-encoded password
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:%40123@localhost/pokemon_db")

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")