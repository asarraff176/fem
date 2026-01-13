from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
def get_truss_local_stiffness_matrix_endpoint(data: dict[str, float]) -> dict[str, list[float]]: 
    
    area: float = data["area"]
    elastic_modulus: float = data["elastic_modulus"]
    length: float = data["length"]

    k_matrix = get_truss_local_stiffness_matrix(area, elastic_modulus, length)
    k = k_matrix[0].to_list()

    return {
        "stiffness": k
    }