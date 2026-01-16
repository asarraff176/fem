from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from core.two_dimension_space import get_truss_local_stiffness_matrix
  
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


@app.post("/get_truss_local_stiffness_matrix")
def get_truss_local_stiffness_matrix_endpoint(data: dict[str, float]) -> dict[str, float]: 
    
    area: float = data["area"]
    elastic_modulus: float = data["elastic_modulus"]
    length: float = data["length"]

    k_matrix: np.ndarray[tuple[Any, ...], np.dtype[np.Any]] = get_truss_local_stiffness_matrix(area, elastic_modulus, length)
    k: list[float] = round(float(k_matrix[0][0]),3)  # Just return the first row for simplicity

    return {
        "stiffness": k
    }