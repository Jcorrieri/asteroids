import pygame

from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS

class Player(CircleShape):
    def __init__(self, x: int, y: int, cooldown_timer: float = 0) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0.0
        self.cooldown_timer = cooldown_timer

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown_timer -= dt
    
    def move(self, dt: float):
        move_vec = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += move_vec

    def shoot(self):
        if self.cooldown_timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

