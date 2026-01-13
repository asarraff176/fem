def get_elastic_modulus(compression_strength: float) -> float:
    return 200_000

def get_maximum_deformation(elastic_modulus: float, tensile_strength: float): 
    maximum_deformation: float = tensile_strength / elastic_modulus 
    return maximum_deformation