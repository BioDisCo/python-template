"""Main module of the multiplier package."""

import numpy as np


def multiply(x: float, y: float) -> float:
    """Calculates the product of two numbers.

    Args:
        x: first number
        y: second number

    Returns:
        Product of the two numbers.
    """
    return np.multiply(x, y)
