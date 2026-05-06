from pathlib import Path

WINDOW_TITLE = "Panda3D Animation Viewer"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
BACKGROUND_COLOR = (0.15, 0.15, 0.20, 1.0)
SHOW_FPS = True
ASSET_DIR = Path(__file__).parent.parent / "assets"
CHARACTER_BAM = ASSET_DIR / "kaykit-mannequin-medium.bam"
