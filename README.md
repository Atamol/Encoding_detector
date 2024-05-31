## 概要
[Chardet](https://pypi.org/project/chardet/)というパッケージを使用し，CSVファイルのエンコーディングを検出することができます．

エンコーディングのエラーが出てしまった場合や，UTF-8やShift JISのファイルが混合されてしまった場合の整理に使えます．

ファイルのサイズが大きい場合は，判定ができた時点で結果を返してくれる`Chardet`の`UniversalDetector`というクラスを使用すると良いかも知れません（`detect_encoding_l.py`に該当）．

## Chardetのインストール
コンソールにて以下を実行してください．
```
pip install chardet
```
インストールが完了したら，ファイルを実行することができます．

## 実行方法
それぞれパスを指定し，コンソールから実行してください．

ファイルのサイズが大きくない場合（個人の判断基準による）は`detect_encodhing_S.py`を，大きい場合は`detect_encoding_l.py`を使うと良いでしょう．
