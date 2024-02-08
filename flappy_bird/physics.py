from typing import TypeAlias, Sequence
from pygame.math import Vector2

Scalar: TypeAlias = float
Vector: TypeAlias = Vector2 | Sequence[float]

REAL_SCALAR: Scalar = 0.01
NULL_SCALAR: Scalar = 0
NULL_VECTOR: Vector = (0, 0)

class PhysicsBody2D(object):

    def __init__(self,
        mass        : Scalar = REAL_SCALAR,
        position    : Vector = NULL_VECTOR,
        velocity    : Vector = NULL_VECTOR,
        acceleration: Vector = NULL_VECTOR,

        angle                : Scalar = NULL_SCALAR,
        angular_velocity     : Scalar = NULL_SCALAR,
        angular_acceleration : Scalar = NULL_SCALAR
    ):
        self._mass         = mass
        self._position     = Vector2(position)
        self._velocity     = Vector2(velocity)
        self._acceleration = Vector2(acceleration)

        self.angle                = angle
        self.angle_velocity       = angular_velocity
        self.angular_acceleration = angular_acceleration

    def update(self, deltatime: Scalar = REAL_SCALAR):

        self.velocity += deltatime*self.acceleration
        self.position += deltatime*self.velocity
        self.acceleration = NULL_VECTOR

        self.angle_velocity += deltatime*self.angular_acceleration
        self.angle          += deltatime*self.angle_velocity
        self.angular_acceleration = NULL_SCALAR

    def apply_forces(self, *forces: Vector):
        for force_x, force_y in forces:
            self.acceleration.x += force_x
            self.acceleration.y += force_y

    def apply_angular_forces(self, *forces: Scalar):
        self.angular_acceleration += sum(forces) / self.mass

    @property
    def mass(self) -> Scalar:
        """The mass property."""
        return self._mass

    @mass.setter
    def mass(self, scalar: Scalar):
        if scalar > 0:
            self._mass = scalar

    @property
    def position(self) -> Vector2:
        """The position property."""
        return self._position

    @position.setter
    def position(self, vector: Vector):
        self._position.update(vector)

    @property
    def velocity(self) -> Vector2:
        """The velocity property."""
        return self._velocity

    @velocity.setter
    def velocity(self, vector: Vector):
        self._velocity.update(vector)

    @property
    def acceleration(self) -> Vector2:
        """The acceleration property."""
        return self._acceleration

    @acceleration.setter
    def acceleration(self, vector: Vector):
        self._acceleration.update(vector)

# Forces:
def gravity(m1: Scalar, m2: Scalar, r1: Vector, r2: Vector, g: Scalar = 1) -> Vector2:
    return Vector2(
        g*m1*m2*(r2[0] - r1[0]) / ( (r2[0] - r1[0])**2 + (r2[1] - r1[1])**2 )**(3/2),
        g*m1*m2*(r2[1] - r1[1]) / ( (r2[0] - r1[0])**2 + (r2[1] - r1[1])**2 )**(3/2)
    )

def air_resistence(v: Vector, k: Scalar = 1) -> Vector2:
    return Vector2(
        - v[0] * (v[0]**2 + v[1]**2) * k,
        - v[1] * (v[0]**2 + v[1]**2) * k
    )
