from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import json
from pathlib import Path


app = FastAPI(title="Items API", version="1.0.0")
DB_PATH = Path("./db/shopping_list.json")

class Item(BaseModel):
    name: str
    quantity: int 

def check_database_exists() -> None:
    if not DB_PATH.exists():
        print(f"ERROR: Database file not found at {DB_PATH}")
        print("In development: Create the data/db.json file manually")
        print("In Docker: Mount a volume to /app/data with the db.json file")
        raise FileNotFoundError(f"Database file not found: {DB_PATH}")


def load_database():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def save_database(data: Dict) -> None:
    """Save dictionary data to JSON file"""
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)


@app.on_event("startup")
async def startup_event():
    check_database_exists()




@app.get("/items")
async def list_items():
    data = load_database()
    return data

@app.post("/items")
async def create_item(item: Item):
    data = load_database()
    item = item.dict()
    item["id"] = str(len(data) +1)
    data.append(item)
    save_database(data)
    return f"updated the new item: \n{item}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)