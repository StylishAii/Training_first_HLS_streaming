# サムネイル用画像置き場

**ディレクトリ構成**

```
/thumbnail
  ┝ video001/
    ┝ 0001.png
    ┝ 0002.png
    ┝ ・・・
    ┗ 0100.png
  ┝ ・・・
  ┗ video100/
```

# mp4 → 100秒ごとの画像抽出

```bash
$ ffmpeg -i FILENAME.mp4 -r 0.01 ./thumbnail/FILENAME/%04d.png
```