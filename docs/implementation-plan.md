# 実装計画

## フェーズ 1：基本アプリケーションウィンドウ

### 実装内容

- Panda3D の `ShowBase` を継承したアプリクラスの骨格
- ウィンドウタイトル・解像度・背景色の設定
- FPS 表示（デバッグ用）
- `ESC` キーでの終了
- ゲームループの確認用タスク（毎フレーム `dt` を取得）

### 受け入れ条件

- [ ] ウィンドウが `1280×720` で開く
- [ ] タイトルバーに `"Panda3D Animation Viewer"` が表示される
- [ ] 背景色が暗いグレーになっている
- [ ] 右上に FPS カウンターが表示される
- [ ] `ESC` キーでウィンドウが閉じる
- [ ] コンソールにエラーが出ない

### ファイル仕様

#### `requirements.txt`

```
panda3d>=1.10.14
```

#### `src/config.py`

アプリ全体で使う定数をここに集約する。

```python
from pathlib import Path

# ウィンドウ設定
WINDOW_TITLE = "Panda3D Animation Viewer"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# 背景色 (R, G, B, A)  0.0〜1.0
BACKGROUND_COLOR = (0.15, 0.15, 0.20, 1.0)

# デバッグ
SHOW_FPS = True

# パス
ASSET_DIR = Path(__file__).parent.parent / "assets"
```

#### `src/app.py`

```python
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
```

> **注意：** `globalClock` はグローバルスコープに自動注入されるが、`self.clock` を使う方が明示的で静的解析ツールにも優しい。

#### `main.py`

```python
from src.app import App

if __name__ == "__main__":
    app = App()
    app.run()
```

### `.gitignore`

```
.venv/
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
assets/*.glb
assets/*.fbx
```

---

## フェーズ 2：GLB キャラクターの読み込みとアニメーション再生

### アセット情報

`assets/kaykit-mannequin-medium.glb`（KayKit 製、Blender でテクスチャを埋め込み済み）

| 項目 | 内容 |
|---|---|
| スケルトン | `Rig_Medium`（23 joints） |
| メッシュ | Body / Head / ArmLeft / ArmRight / LegLeft / LegRight（6パーツ） |
| テクスチャ | `mannequin_texture`（512×512 px PNG、GLB 内に埋め込み） |
| アニメーション | 11 本（下表） |

| アニメーション名 | フレーム数 |
|---|---|
| `Walking_A` / `Walking_B` / `Walking_C` | 33 / 33 / 49 |
| `Running_A` / `Running_B` | 25 / 25 |
| `Jump_Start` / `Jump_Idle` / `Jump_Land` | 19 / 33 / 21 |
| `Jump_Full_Short` / `Jump_Full_Long` | 35 / 70 |
| `T-Pose` | 1 |

すべて 30 fps。

### ローダーについて

Panda3D 標準の Assimp ローダーは GLB の骨格アニメーションを正しく読めない。
`panda3d-gltf` を使う必要がある。

`Actor` クラスは内部ローダーとして Assimp を使うため、GLB を直接渡すと壊れる。
**GLB → BAM に変換してから Actor に渡す**のが正しいワークフロー。

### BAM 変換手順（セットアップ時に一度だけ実行）

```bash
.venv/bin/gltf2bam assets/kaykit-mannequin-medium.glb assets/kaykit-mannequin-medium.bam
```

BAM はビルド生成物として `.gitignore` に追加済み（`assets/*.bam`）。

### 実装内容

- `src/player.py` を追加
- `Actor` で `assets/kaykit-mannequin-medium.bam` を読み込む
- `Walking_A` をデフォルトアニメーションとしてループ再生

---

## フェーズ 3：キー入力によるアニメーション切り替えと X 方向移動

（フェーズ2完了後に詳細を記述する）

---

## フェーズ 4：レベルメッシュの読み込みと Box コリジョン

（フェーズ3完了後に詳細を記述する）

---

## フェーズ 5：WASD によるゲームフィールド歩き回り

（フェーズ4完了後に詳細を記述する）
