# はじめに

このプログラムは、NHKラジオの「らじる★らじる」で公開されている番組の
HLSのアドレスを取得するためのパッケージを提供します。

HLSのアドレスが入手できれば、
[第48回『らじる★らじる』の聴き逃がしサービス（4）](https://gihyo.jp/article/2023/04/zoku-gansiki-0048?summary)を参照に
コンテンツのダウンロードが可能となります。

参考までに、「エンジョイ・シンプル・イングリシュ」のCLIでのダウンロード実装例を`examples`に格納しています。

# API 

## 使用方法

### 「らじる★らじる」の英語番組のタイトル一覧の習得例

```python
(nhk) taku@okisuke:~/study/nhk/gogaku_dl$ ipython
Python 3.12.4 | packaged by conda-forge | (main, Jun 17 2024, 10:23:07) [GCC 12.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from gogaku_dl import english

In [2]: english.get_program_titles()
Out[2]: 
['小学生の基礎英語',
 '中学生の基礎英語レベル1',
 '中学生の基礎英語レベル2',
 '中高生の基礎英語in English',
 'ラジオ英会話',
 'ボキャブライダー',
 'エンジョイ・シンプル・イングリッシュ',
 '英会話タイムトライアル',
 'ニュースで学ぶ「現代英語」',
 'ラジオビジネス英語']

In [3]: 

```
### 「らじる★らじる」の英語番組のHLSの取得例

`get_english_hls`関数でHLSを取得することができます。
`get_english_hls`の引数には、`get_program_titles`で取得したいずれかの値を指定します。

「エンジョイ・シンンプル・イングリシュ」のHLSの取得例を示します。

```python
(nhk) taku@okisuke:~$ ipython
Python 3.12.4 | packaged by conda-forge | (main, Jun 17 2024, 10:23:07) [GCC 12.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from gogaku_dl import english

In [2]: english.get_hls('エンジョイ・シンプル・イングリッシュ')
Out[2]: 
{'title': 'エンジョイ・シンプル・イングリッシュ',
 'detail_url': 'https://www.nhk.or.jp/radio-api/app/v1/web/ondemand/series?site_id=3064&corner_site_id=01',
 'episodes': [{'エンジョイ・シンプル・イングリッシュ「新紙幣」': {'onair': '7月1日(月)午前9:10放送',
    'len_in_sec': 300.0,
    'hls': 'https://vod-stream.nhk.jp/radioondemand/r/3064/s/stream_3064_b57b533405e7427dead106a78e09c354/index.m3u8'}},
  {'エンジョイ・シンプル・イングリッシュ「梅雨＆ヒール・レスラー」': {'onair': '7月2日(火)午前9:10放送',
    'len_in_sec': 300.0,
    'hls': 'https://vod-stream.nhk.jp/radioondemand/r/3064/s/stream_3064_43db53cbce8796bae3123c2de51e3d8b/index.m3u8'}},
  {'エンジョイ・シンプル・イングリッシュ「地雷除去機」': {'onair': '7月3日(水)午前9:10放送',
    'len_in_sec': 300.0,
    'hls': 'https://vod-stream.nhk.jp/radioondemand/r/3064/s/stream_3064_fc64d9225949641ef1fc938e6e47b1c2/index.m3u8'}},
  {'エンジョイ・シンプル・イングリッシュ「アキレスけん」': {'onair': '7月4日(木)午前9:10放送',
    'len_in_sec': 300.0,
    'hls': 'https://vod-stream.nhk.jp/radioondemand/r/3064/s/stream_3064_c1755ef446f15b6c7548e5586b974a6f/index.m3u8'}},
  {'エンジョイ・シンプル・イングリッシュ「女王の首飾り－第１話－」': {'onair': '7月5日(金)午前9:10放送',
    'len_in_sec': 300.0,
    'hls': 'https://vod-stream.nhk.jp/radioondemand/r/3064/s/stream_3064_840fbc6b0cb82e68b22c93ff5d60775b/index.m3u8'}}],
 'fiscal_year': 2024}

In [3]: 

```

# APIを使用した実装例

「エンジョイン・シンプル・イングリシュ」をmp3にダウンロードする実装例
を`examples/rec_enjoy_simple_english.py`として格納しました。

実行例を以下に示します。

https://github.com/takushi1969/gogaku_dl/assets/3589129/bf56750c-3b2b-47b7-a925-a9e1f15bce87






