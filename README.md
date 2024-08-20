# 概要
[Chardet](https://pypi.org/project/chardet/)というパッケージを使用し，TXTファイルやCSVファイルなどのエンコーディングを検出することができます．<br>
UTF-8やShift JISのファイルが混合されてしまった場合の整理や，エンコーディングのエラーが出てしまった場合に便利です．

## Chardetの概要，およびインストール
Chardetはバイト列を読み込み，そのパターンからエンコーディングを推測するというものです．
コンソールにて以下を実行してください．
```
pip install chardet
```
インストールが完了したら，ファイルを実行することができるようになります．

## 実装・実行のおおまかな手順
1. `encoding_detector`をダウンロードします．
2. Chardetをインストールします（前述）．
3. コンソールからファイルを実行します．

## 出力例
例として，結果は以下のように出力されます．どちらのメソッドを使ったのかについても記述されます．
- 1MB未満の容量のファイル（Shift-JIS）:
```
Using chardet.detect() for file size: 410000 bytes
{'encoding': 'SHIFT_JIS', 'confidence': 0.99, 'language': 'Japanese'}
```
- 1MB以上の容量のファイル（UTF-8）:
```
Using UniversalDetector for file size: 2100000 bytes
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
```

## * 大きいファイルを効率的に処理する工夫について
`encoding_detector_larger.py`では`UniversalDetector`というクラスを使用しています．<br>
通常の`detect() `関数は大きなファイルに対して使うと検出に長い時間が掛かってしまうのですが，こちらのクラスには`feed()`というメソッドがあります．<br>
これは複数回に分けてバイト列を渡すことができるもので，十分に推定が完了していると見込めればインスタンスのメンバ変数`done`が真となり，その時点で計算を打ち切って結果を返してくれます．<br>
これにより大きなファイルの解析でも余計な時間をかけずに済むのです．
