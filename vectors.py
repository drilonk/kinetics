"""Vectors."""

import numpy as np
from attrs import field, validate, define, validators
from attrs.validators import instance_of

@define
class vector2d:
    x: float = field(validators=instance_of(float))
    y: float = field(validators=instance_of(float))

    
