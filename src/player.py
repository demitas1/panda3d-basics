from direct.actor.Actor import Actor
from src.config import CHARACTER_BAM


class Player:

    def __init__(self, render):
        self._pressed: set[str] = set()
        self._current_anim: str = ""
        self._velocity_x = 0.0
        self._velocity_y = 0.0
        self._direction = 0.0

        self.actor = Actor(str(CHARACTER_BAM))
        self.actor.reparentTo(render)
        self._update_anim()

    MOVE_SPEED = 1.0

    def update(self, dt):
        self.actor.setX(self.actor.getX() + self._velocity_x * dt)
        self.actor.setY(self.actor.getY() + self._velocity_y * dt)
        self.actor.setH(self._direction)

    def cleanup(self):
        self.actor.cleanup()

    def key_down(self, key: str) -> None:
        self._pressed.add(key)
        self._update_anim()

    def key_up(self, key: str) -> None:
        self._pressed.discard(key)
        self._update_anim()

    def _update_anim(self) -> None:
        # set velocity
        if "s" in self._pressed:
            self._velocity_x = 0.0
            self._velocity_y = -self.MOVE_SPEED
            self._direction = 0.0
        elif "w" in self._pressed:
            self._velocity_x = 0.0
            self._velocity_y = self.MOVE_SPEED
            self._direction = 180.0
        elif "a" in self._pressed:
            self._velocity_x = -self.MOVE_SPEED
            self._velocity_y = 0.0
            self._direction = 270.0
        elif "d" in self._pressed:
            self._velocity_x = self.MOVE_SPEED
            self._velocity_y = 0.0
            self._direction = 90.0
        else:
            self._velocity_x = 0.0
            self._velocity_y = 0.0

        # set animation
        anim = "Walking_A" if self._pressed else "Idle_A"
        if anim != self._current_anim:
            self._current_anim = anim
            self.actor.loop(anim)
