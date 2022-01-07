from genericpath import exists
import os
import sys
import argparse
import subprocess

"""mp4からストリーミングデータ + サムネイル画像作成
Args:
    input : mp4 file path

Returns:
    ./video/*/.ts : ストリーミングデータ
    ./video/*/.m3u8 : ストリーミングリストデータ
    ./thumbnail/*/.png : サムネイルデータ
"""

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='動画コンバートプログラム')

    parser.add_argument('input', help="Input file (mp4)")

    args = parser.parse_args()

    filename = os.path.splitext(os.path.basename(args.input))[0]

    # 重複確認
    video_path = "./video/" + str(filename)
    thumbnail_path = "./thumbnail/" + str(filename)

    if os.path.exists(video_path) or os.path.exists(thumbnail_path):
        yesno = input("video / thumbnail_path already exists. Are you execute?? [y|n]")

        if yesno != "y":
            sys.exit(0)

    # ディレクトリ Setup
    os.makedirs(video_path, exist_ok=True)
    os.makedirs(thumbnail_path, exist_ok=True)

    # ファイル名定義
    m3u8_filename = "./video/" + str(filename) + '/' + 'video.m3u8'
    ts_filename = "./video/" + str(filename) + '/' + '%04d.ts'

    exec_args = [
        'ffmpeg', '-i', args.input,
        '-codec', 'copy',
        '-map', '0',
        '-f', 'segment',
        '-vbsf', 'h264_mp4toannexb',
        '-segment_format', 'mpegts',
        '-segment_time', '10',
        '-segment_list', m3u8_filename, ts_filename
    ]

    res = subprocess.check_call(exec_args)


    png_filename = "./thumbnail/" + str(filename) + '/' '%04d.png'

    exec_args = [
        'ffmpeg', '-i', args.input,
        '-r', '0.01',
        png_filename
    ]

    res = subprocess.check_call(exec_args)
