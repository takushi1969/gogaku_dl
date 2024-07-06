#!/usr/bin/env python
#-*- coding: utf-8 -*-

from gogaku_dl import english
from ffmpeg import (
    FFmpeg,
    Progress)
from tqdm import tqdm
import re


def main(title: str) -> None:
    program = english.get_hls(title)
    for episode in program['episodes']:
        for title, info in episode.items():

            subtitle = re.sub(r'.*「', '', title)
            subtitle = re.sub(r'」.*', '', subtitle)
            progress_bar = tqdm(
                desc=subtitle,
                total=int(info['len_in_sec']),
                bar_format='{l_bar}{bar}{n_fmt}/{total_fmt} sec'
            )
            cur_sec = 0

            ffmpeg = (
                FFmpeg()
                .option('y')
                .option('f', 'hls')
                .input(info['hls'],
                       {"seg_max_retry": "100",
                        "http_seekable": "0"})
                .output(
                    f'{title}.mp3',
                    {'codec:a': 'libmp3lame',
                     'b:a': '128k'}))

            @ffmpeg.on("progress")
            def on_progress(progress: Progress):
                nonlocal progress_bar
                nonlocal cur_sec

                old_sec = cur_sec
                cur_sec = int(progress.time.total_seconds())
                progress_bar.update(cur_sec - old_sec)

            @ffmpeg.on("completed")
            def on_completed():
                nonlocal progress_bar
                nonlocal cur_sec

                cur_sec = int(info['len_in_sec']) - cur_sec
                progress_bar.update(cur_sec)
                progress_bar.close()

            ffmpeg.execute()


if __name__ == '__main__':
    main('エンジョイ・シンプル・イングリッシュ')
