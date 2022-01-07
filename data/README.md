# Media Stream File Folder
ストリーミングに必要な，ファイルを各動画ごとに，配置

**ディレクトリ構成**

```
/video
    ┝ video1/
        ┝ video1-001.ts
        ┝ video1-002.ts
        ┝ video1-003.ts
        ・・・
        ┗ video1.m3u8
    ┝ video2/
    ┝ video3/

/thumbnail
    ┝ video001/
        ┝ 0001.png
        ┝ 0002.png
        ┝ ・・・
        ┗ 0100.png
      ┝ ・・・
      ┗ video100/
```

# Quick Start
このディレクトリに，動画を配置して，以下のスクリプトを実行すると上記のディレクトリ構成でファイル作成されます．

```bash
$ python3 script/setup.py example.mp4
```

# Detail convert process
以下が "Quick Start" で処理されていることです．

## ※ mp4 → ts / m3u8 file

```bash
# FILENAME : 任意のファイル名に置き換え
$ ffmpeg -i FILENAME.mp4 -codec copy -map 0 -f segment -vbsf h264_mp4toannexb -segment_format mpegts -segment_time 10 -segment_list FILENAME/video.m3u8 FILENAME/video-%03d.ts
```

## mp4 → サムネイル png

```bash
$ ffmpeg -i FILENAME.mp4 -r 0.01 ./thumbnail/FILENAME/%04d.png
```

## 動画素材参考サイト

- [Free Stock Video Footage](https://www.videvo.net/)