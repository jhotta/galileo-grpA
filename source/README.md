# Pythonコードの概要

## galileo-grpA/sourceディレクトリ以下のファイル構成

- client_secrets.json (PyDriveが認証関連を保存する先)
- gdrive.py (Google DriveのターゲットファイルをDLするスクリプト)
- quickstart.py (localhost:8080を認証用に設定するためのスクリプト)
- settings.yaml (PyDriveの設定を記述するファイル)
- README.md (#このファイル)

`gdrive.py`, `lient_secrets.json`, `settings.yaml`は、同じディレクとに設置されている必要があります。


## 実行に必要な環境

- tadokoro SD full imageでgalileoを起動
- libyamlのコンパイル
	- `# wegt http://pyyaml.org/download/libyaml/yaml-0.1.5.tar.gz`
	- `# tar -zxvf yaml-0.1.5.tar.gz`
	- `# cd cd yaml-0.1.5` 
	- `# ./cofigure`
	- `# make ; make install`
- ez_setup.pyの取得
	- `# wget http://peak.telecommunity.com/dist/ez_setup.py`
- easy_installのインストール
	- `# python ./ez_setup.py`
- pipのインストール
	- `# easy_install pip`
- PyDriveのインストール
	- `# pip install PyDrive` 	
- python-dateutilのインストール（timestampのsortで推奨）
	- `pip install python-dateutil`
- sourceの取得
	- `# git clone https://github.com/jhotta/galileo-grpA.git` 


## 単体実行方法

- ディレクトリ移動
	- `# cd galileo-grpA/source/`
- 実行権限付与
	- `# chmod 755 gdrive.py`
- スクリプト実行
	- `./gdrive.py`


## Cronによる定期実行の設定

現在、検証中！（今後の課題です）
スケッチで作ったフログラムがtadokoro SD fullで使用できない場合は、対応策を検討中。


## スクリプトで取得したfileの保存先の変更

gdrive.pyの12行目のパスの指定部分に、`/root`などとすることで変更する。

`save_path = "."` 

## todo

- error処理
- script test