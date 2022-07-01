# Windowsで環境構築時のメモ
condaとpip併用
python3.5
torch1.1.10

# 結論
1. リポジトリのクローン
```bat
git clone https://github.com/tohinz/ConSinGAN.git
cd ConSinGAN
```
2. conda環境の作成
```bat
conda create -n py35_pConSinGAN python=3.5
conda activate py35_pConSinGAN
```
3. ライブラリのインストール
```bat
conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
python -m pip install -r requirements.txt
```
4. ファイルの編集
main_train.py 107行目
~~~python
copyfile(py_file, osp.join(dir2save, py_file.split("/")[-1]))
~~~
を
~~~python
copyfile(py_file, osp.join(dir2save, py_file.split("\\")[-1]))
~~~
に編集


# 補足
## 環境
pip用のrequirementsが配られているので、colabではpipでやるのが望ましいが、\
１から構築する場合、他との兼ね合いやtorchのダウンロードの利便性でcondaの仮想環境でpipでインストールしている。
## ライブラリ
torchのみcondaでいれたほうが楽。[こちら](https://pytorch.org/get-started/previous-versions/)にあるように単純なpipで入らないらしい\
rewuirementsはcondaで入れたほうがいいのだろうが、conda-forgeにしかなかったりでめんどくさいので仮想環境上でpipした。
## ファイルの編集
もともとlinux用のコードらしく、windowsの場合はパスのシステムの関係で4の手順を踏まないとエラーになる。\
[言及されているところ](https://github.com/tohinz/ConSinGAN/issues/4)