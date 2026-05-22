from panda3d.core import NodePath, Loader


class Level:

    def __init__(self, render: NodePath, loader: Loader) -> None:
        self.ground = loader.loadModel("models/box")
        self.ground.setScale(50, 50, 0.5)
        self.ground.setPos(-25, -25, -0.5)
        self.ground.setTextureOff(1)
        self.ground.setColor(0.5, 0.5, 0.5, 1)
        self.ground.reparentTo(render)

    def cleanup(self) -> None:
        self.ground.removeNode()
