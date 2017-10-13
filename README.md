# templa
## 概要
[jinja2](http://jinja.pocoo.org/)を使った粗挽きファイル生成ツール

設定値をフック関数で加工、追加してファイルに埋め込むこともできます。

コマンドは下記の様な感じで実行します。

```
templa.py テンプレートファイル名 --ini テンプレートに埋め込む設定ファイル(.ini) -f フック関数のpythonパッケージ -c フック関数設定ファイル(.ini) > 出力先ファイル名
```

## インストール
gitからcloneした後、pipより依存パッケージをインストールします。

```
git clone git@github.com:balaenoptera-musculus/templa.git
pip install -r templa/packages.txt
```

シバンのパスは適時変えてください。

## 設定ファイルについて
### テンプレートファイル
* テンプレートエンジンはjinja2を使用しています。
* テンプレートに--iniで設定した設定値を埋め込むには

```
{{セクション.パラメータ}}
```

とすればできます。

### テンプレートに埋め込む設定ファイル(--ini)
* テンプレートに渡す設定値を定義します。

```パラメータ=値```とすればOKです。

### フック関数のpythonパッケージ(-f 省略可)

* フック関数をまとめたパッケージファイルを指定します(WordPressのfunctions.php的なイメージです)

* カレントディレクトリが起点です。

* フック関数の定義は

```
def 関数名(引数):
   ~~中略~~
   return 引数
```

としてください。

引数にテンプレートに渡す設定値が入ってます。(形式:変数名\[セクション\]\[パラメータ\]で取れます)

戻り値に引数で受け取った変数を指定しないとテンプレートに値を埋め込めません。

### フック関数設定ファイル(-c)
* 実行するフック関数名、実行順を指定します。

* hookに実行する関数の関数名、priorityで実行順を指定します。

* priorityの値がが低い関数から実行します。同一の値であれば、先に指定した関数から実行します。

### 注意
ちょっとこんなん欲しいなと思ってPythonの勉強がてら片手間で作ったものです。品質はお察しです。

使用は自己責任でお願いします。

こうした方が良いとかは是非受け付けます！

Issuesに挙げてもらえると喜びます！
