# Panda3D Animation Viewer

Python + Panda3D を使った 3D キャラクターアニメーションのインタラクティブビューア。

ゲームエンジンの原理（ゲームループ・SceneGraph・Actor・コリジョン）を説明するための教育用プロトタイプ。

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## アセットの準備（初回のみ）

Panda3D 標準ローダーは GLB の骨格アニメーションを正しく読めないため、
`panda3d-gltf` 付属の `gltf2bam` で BAM 形式に変換してから使用する。

```bash
.venv/bin/gltf2bam assets/kaykit-mannequin-medium-append.glb assets/kaykit-mannequin-medium.bam
.venv/bin/gltf2bam assets/panda3d-level.glb assets/level.bam
```

生成された `.bam` ファイルは `.gitignore` 対象のため、クローン後に一度だけ実行が必要。

## 実行

```bash
python main.py
```

ESC キーで終了。

## 動作環境

- Python 3.10 以上
- Panda3D 1.10.14 以上

## ライセンス

MIT License — 詳細は [LICENSE.txt](LICENSE.txt) を参照。

### アセット

`assets/` 内のキャラクターアセットは [Kay Lousberg](https://www.kaylousberg.com) 氏による
[KayKit : Character Animations](https://kaylousberg.itch.io/) を使用しています。
ライセンス: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)（パブリックドメイン）
