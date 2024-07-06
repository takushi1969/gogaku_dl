#!/usr/bin/env python
#-*- coding: utf-8 -*-

from gogaku_dl import english
from ffmpeg import (
    FFmpeg,
    Progress)


def main(title: str) -> None:
    program = english.get_hls(title)

    for episode in program['episodes']:
        for title, info in episode.items():
            ffmpeg = (
                FFmpeg()
                .option('y')
                .option('f', 'hls')
                .input(info['hls'],
                       {"seg_max_retry": "100",
                        "http_seekable": "1"})
                .output(
                    f'{title}.mp3',
                    {'codec:a': 'libmp3lame',
                     'b:a': '128k'}))

            @ffmpeg.on("progress")
            def on_progress(progress: Progress):
                print(progress)

            ffmpeg.execute()


if __name__ == '__main__':
    main('エンジョイ・シンプル・イングリッシュ')
