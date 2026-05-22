from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from src.config import (
    WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT,
    BACKGROUND_COLOR, SHOW_FPS,
)
from src.player import Player
from src.level import Level

class App(ShowBase):

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_camera()
        self._setup_input()
        self._setup_debug()
        self.level = Level(self.render, self.loader)
        self.player = Player(self.render)
        self.taskMgr.add(self._update, "main_update")
        self._setup_input_system()

    def _setup_input_system(self) -> None:
        for key in ("w", "a", "s", "d"):
            self.accept(key,         self.player.key_down, [key])
            self.accept(f"{key}-up", self.player.key_up, [key])

    def _setup_window(self):
        props = WindowProperties()
        props.setTitle(WINDOW_TITLE)
        props.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.win.requestProperties(props)
        self.setBackgroundColor(*BACKGROUND_COLOR)

    def _setup_camera(self):
        self.camera.setPos(5.0, -10.0, 1.2)
        self.camera.lookAt(0, 0, 0.8)

    def _setup_input(self):
        self.disableMouse()
        self.accept("escape", self.userExit)

    def _setup_debug(self):
        if SHOW_FPS:
            self.setFrameRateMeter(True)

    def _update(self, task):
        dt = self.clock.getDt()
        self.player.update(dt)
        return task.cont
