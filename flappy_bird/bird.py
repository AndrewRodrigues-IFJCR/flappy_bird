from typing import Any

from entity import*
from physics import*

JUMP = (0, -900)
K = 0.001

class Bird(Entity2D):

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.body = PhysicsBody2D(1e1, (300, 300))
        self.plan = PhysicsBody2D(9e5, (300, 600))
        self.time = 0
        self.surf.fill('green')

    def update(self, *args: Any, **kwargs: Any):
        self.time -= kwargs.get('deltatime', REAL_SCALAR)
        # self.body.apply_forces(
        #     JUMP if self.time > 0 else (0, 0),
        #     gravity(
        #         self.body.mass,
        #         self.plan.mass,
        #         self.body.position,
        #         self.plan.position
        #     ),
        #     air_resistence(self.body.velocity, K)
        # )
        self.body.apply_angular_forces(+10 if self.time > 0 else -10)
        print(self.body.angle)
        return super().update(*args, **kwargs)

    def jump(self):
        self.time = 50

