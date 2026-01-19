from typing import Callable

def solve(function: Callable[[float] ,float], initial_guess:float, tolerance: float) -> float:
    
    MAX_ITER: int = 1000
    iteration: int = 0
    y1 = function(initial_guess)
    y2 = function(initial_guess + initial_guess * 0.1)
    x1 = initial_guess

    while (abs(y1) > tolerance) and (iteration < MAX_ITER): 
        iteration += 1
        x2 = x1 + x1 * 0.1

        y1 = function(x1)
        y2 = function(x2)

        dx = x2 - x1
        dy = y2 - y1

        # NEXT GUESS 
        
        x1: float = x1 -y1*(dx/dy)

    return x1
