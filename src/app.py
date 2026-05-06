from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from src.config import (
    WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT,
    BACKGROUND_COLOR, SHOW_FPS,
)

# フェーズ2で追加予定
# from src.player import Player


class App(ShowBase):

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_input()
        self._setup_debug()
        self.taskMgr.add(self._update, "main_update")

    def _setup_window(self):
        props = WindowProperties()
        props.setTitle(WINDOW_TITLE)
        props.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.win.requestProperties(props)
        self.setBackgroundColor(*BACKGROUND_COLOR)

    def _setup_input(self):
        self.disableMouse()
        self.accept("escape", self.userExit)

    def _setup_debug(self):
        if SHOW_FPS:
            self.setFrameRateMeter(True)

    def _update(self, task):
        dt = self.clock.getDt()
        # フェーズ2以降でキャラクター移動などをここに追加する
        # if self.player:
        #     self.player.update(dt)
        return task.cont
