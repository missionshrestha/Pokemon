# Pokemon
# Pokémon API

## Setup

1. Clone the repository
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure your database in `config.py`
5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

- **POST /api/v1/pokemons/**: Create a new Pokémon
- **GET /api/v1/pokemons/**: List all Pokémon or filter by name
