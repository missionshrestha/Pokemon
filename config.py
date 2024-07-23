import os

# Correctly URL-encoded password
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:M1s2n3sth%40123@localhost/pokemon_db")
