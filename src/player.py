from direct.actor.Actor import Actor
from src.config import CHARACTER_BAM


class Player:

    def __init__(self, render):
        self._pressed: set[str] = set()
        self._current_anim: str = ""

        self.actor = Actor(str(CHARACTER_BAM))
        self.actor.reparentTo(render)
        self._update_anim()

    def update(self, dt):
        # フェーズ3で移動処理を追加
        pass

    def cleanup(self):
        self.actor.cleanup()

    def key_down(self, key: str) -> None:
        self._pressed.add(key)
        self._update_anim()

    def key_up(self, key: str) -> None:
        self._pressed.discard(key)
        self._update_anim()

    def _update_anim(self) -> None:
        anim = "Walking_A" if self._pressed else "Idle_A"
        if anim != self._current_anim:
            self._current_anim = anim
            self.actor.loop(anim)
