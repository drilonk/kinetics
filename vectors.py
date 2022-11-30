"""Vectors."""


import numpy as np
from attrs import field, define, validators
from attrs.validators import instance_of


@define
class Vector2D:
    x: float = field(validators=instance_of(float))
    y: float = field(validators=instance_of(float))

    def __str__(self):
        """Human-readable string representation of the vector."""
        return f'{self.x:g}i + {self.y:g}j'


vec = Vector2D(x=4.3, y=8.8)
print(vec)
