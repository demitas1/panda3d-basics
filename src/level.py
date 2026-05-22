from panda3d.core import NodePath, Loader


class Level:

    def __init__(self, render: NodePath, loader: Loader) -> None:
        self.ground = loader.loadModel("assets/level.bam")
        self.ground.reparentTo(render)

    def cleanup(self) -> None:
        self.ground.removeNode()
