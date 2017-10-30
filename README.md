# quick-search

コマンドラインからGoogle検索ができるツールです。マウスを使わず検索し、タイトルやリンク、内容を表示します。対話形式で実行することができ、気になったリンクには番号を入力することで辿ることができます。quick-searchはGoogle Custom Search APIを使用しているため、検索回数に比例して課金されます。


# コンセプト

quick-searchは学習コストを少なくするため、可能な限りオプションやコマンド特有の使い方を省いています。「シンプル」に「見やすく」を基本設計として、直感的に操作できるようになっています。

# 実行環境

現行は、以下の環境でのみ実行検証を行なっています。

|ツール/OS/サービス|バージョン|
|:-----------|:------------|
|python|python3.5 or later|
|OS|CentOS6 or later|
|Google Custom Search API|https://cloud.google.com/?hl=ja|

# インストール

```
# Gitからダウンロード
$ git clone git@github.com:eitake0002/quick-search.git

# 必要ライブラリのインストール
$ pip install -r requirements.txt

# Google API Keyのセットアップ
$ export GOOGLE_API_KEY=[GCPのアクセスキー]

# 実行
$ python quick-search [検索ワード]

# エイリアスを設定しより簡単に実行
$ alias q='~/quick-search/quick-search.py'
$ q [検索ワード]
```

# 使い方

```
# 構文
$ ./quick-search [検索クエリ]

# 例
$ ./quick-search テスト クエリ
```

# 実行後オプション

実行後は対話形式でオプションを指定することができます。デフォルトでは5つずつリンク数が表示されます。

|オプション|説明|
|:-----------|:------------|
|Enter| 次へ進む|
|リンク番号|指定したリンク番号を表示する|
|q|Quit|

# 高度な設定

params.yamlを設定することで、検索条件や動作環境をカスタマイズすることができます。

|パラメータ|説明|デフォルト|
|:-----------|:------------|:------------|
|query_num|1回の実行で表示する検索結果数を指定します。|20|
|stop_num|5|
