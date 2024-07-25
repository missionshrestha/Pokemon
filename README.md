# Pokémon API Project

Welcome to the Pokémon API Project! This project serves a list of Pokémon with their details and allows filtering by name and type. The backend is built using FastAPI, and data is stored and served from a PostgreSQL database.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- Fetch and display Pokémon data.
- Filter Pokémon by name and type.
- Data stored in PostgreSQL and fetched from the database.

## Installation

### Prerequisites
- Python 3.11 or higher
- PostgreSQL
- Virtualenv (optional but recommended)

### Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/missionshrestha/Pokemon.git
    cd Pokemon
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**
    Create a `.env` file in the root directory and add your database URL:
    ```env
    DATABASE_URL=postgresql+asyncpg://your_username:your_password@localhost/pokemon_db
    ```

5. **Run Database Migrations**
    ```bash
    python -m app.fetch_pokemon_data  # This will populate your database
    ```

6. **Start the Server**
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

1. **Start the Server**
    Run the server using the command:
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Access the API**
    - Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
    - Use the `/api/v1/pokemons/` endpoint to fetch Pokémon data.

## API Endpoints

- **Get All Pokemons**
    - **Endpoint:** `/api/v1/pokemons/`
    - **Method:** `GET`
    - **Query Parameters:**
      - `name` (optional): Filter by Pokémon name.
      - `type` (optional): Filter by Pokémon type.
    - **Response:**
      ```json
      [
        {
          "id": 1,
          "name": "bulbasaur",
          "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
          "type": "grass"
        },
        ...
      ]
      ```

- **Create a New Pokemon**
    - **Endpoint:** `/api/v1/pokemons/`
    - **Method:** `POST`
    - **Request Body:**
      ```json
      {
        "name": "new_pokemon",
        "image": "http://image.url",
        "type": "fire"
      }
      ```
    - **Response:**
      ```json
      {
        "id": 101,
        "name": "new_pokemon",
        "image": "http://image.url",
        "type": "fire"
      }
      ```