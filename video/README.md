# Media Stream File Folder
ストリーミングに必要な，
* m3u8 ファイル
* ts ファイル
を各動画ごとに，配置

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
```

## ※ mp4 → ts / m3u8 file

```bash
# FILENAME : 任意のファイル名に置き換え
$ ffmpeg -i FILENAME.mp4 -codec copy -map 0 -f segment -vbsf h264_mp4toannexb -segment_format mpegts -segment_time 10 -segment_list FILENAME/video.m3u8 FILENAME/video-%03d.ts
```