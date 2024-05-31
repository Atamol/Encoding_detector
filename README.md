## 概要
[Chardet](https://pypi.org/project/chardet/)というパッケージを使用し，CSVファイルのエンコーディングを検出することができます．

エンコーディングのエラーが出てしまった場合や，UTF-8やShift JISのファイルが混合されてしまった場合の整理に使えます．

ファイルのサイズが大きい場合は，判定ができた時点で結果を返してくれる`Chardet`の`UniversalDetector`というクラスを使用すると良いでしょう（`detect_encoding_l.py`に該当）．

## Chardetのインストール
コンソールにて以下を実行してください．
```
pip install chardet
```
インストールが完了したら，ファイルを実行することができます．

## 実行方法
ファイルのパスを指定し，コンソールから実行してください．

それぞれ，
- ファイルのサイズが大きくない場合は`detect_encodhing_S.py`
- ファイルのサイズが大きい場合は`detect_encoding_l.py`

というように使い分けてください．
