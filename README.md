# quick-search

quick-searchはGoogle検索ができるコマンドラインツールです。ターミナルから検索し、タイトルやリンク、コンテンツを一覧表示します。対話形式で実行することができ、気になったリンクには番号を入力することで辿ることができます。quick-searchはGoogle Custom Search APIを使用しているため、検索回数に比例して課金されます。

<img src="https://i.gyazo.com/bfc1c55318f75366205913a674fd381a.png" width="600" style="display: block;margin-left: auto;margin-right: auto;">

# コンセプト

quick-searchは学習コストを少なくするため、可能な限りオプションやコマンド特有の使い方を省いています。「シンプル」に「見やすく」を基本設計とし、直感的に操作できるようになっています。

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
$ export SEARCH_ENGINE_ID=[サーチエンジンID]
$ export GOOGLE_API_KEY=[GCPのアクセスキー]

# 実行
$ python quick-search [検索ワード]

# エイリアスを設定しより簡単に実行
$ alias q='python ~/quick-search/quick-search.py'
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

実行後は対話形式でオプションを指定することができます。デフォルトでは5つずつ検索結果が表示されます。

|オプション|説明|補足|
|:-----------|:------------|:--------------|
|Enter| 次へ進む||
|検索結果番号|指定した検索結果番号を表示する||
|[検索結果番号]c|指定した検索結果をChromeブラウザで表示する。（例） 1c|MacOSのみ対応|
|[検索結果番号]b|指定した検索結果をFirefoxブラウザで表示する。 （例） 1b|MacOSのみ対応|
|q|Quit||

# 高度な設定

params.yamlを設定することで、検索条件や動作環境をカスタマイズすることができます。

|パラメータ|説明|デフォルト|
|:-----------|:------------|:------------|
|result_num|検索結果数を指定します。|20|
|stop_num|指定した回数で一旦止めます。|5|
|summary_num|検索結果時に表示する要約の文字数を指定します.|300|
|multi_process|検索結果をまとめて表示します。multi_processをTrueにすると初期実行は時間がかかりますが、対話形式の表示が早くなります。|False|
