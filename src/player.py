from direct.actor.Actor import Actor
from src.config import CHARACTER_BAM


class Player:

    def __init__(self, render):
        self.actor = Actor(str(CHARACTER_BAM))
        self.actor.reparentTo(render)
        self.actor.loop("Walking_A")

    def update(self, dt):
        # フェーズ3で移動処理を追加
        pass

    def cleanup(self):
        self.actor.cleanup()
