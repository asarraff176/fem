from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    # allow_origins=["*"], # JUST FOR LOCAL DEV
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add")
def add(a: int, b: int) -> dict[str, int]: 
    return {
        "result": a + b
    }

