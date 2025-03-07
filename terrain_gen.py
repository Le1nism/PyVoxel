from noise import noise2, noise3
from random import random
from settings import *

@njit
def get_height(x, z):
    # Amplitude
    a1 = CENTER_Y

    # Frequency
    f1 = 0.005

    height = 0
    height += noise2(x * f1, z * f1) * a1 + a1

    return int(height)