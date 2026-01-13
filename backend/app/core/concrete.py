def get_elastic_modulus(compression_strength: float) -> float:
    Ec: float = 4700.0 * (compression_strength)**0.5
    return Ec

def get_modulus_of_rupture(compression_strength: float) -> float: 
    fr: float = 0.62 * (compression_strength)**0.5
    return fr

def get_maximum_deformation(): 
    return 0.003