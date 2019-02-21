# ImageAIを使った機械学習
### 動作環境
Python 3.5.1 (and later versions)  
Tensorflow 1.4.0 (and later versions)  
Keras 2.x  
ImageAI 2.0.2

詳細は[ImageAIのGitHub](https://github.com/OlafenwaMoses/ImageAI) 

## リアルタイム物体検知
### 概要
簡単に物体検知を体験するためのソースコード。  

IPカメラで取得した映像を、リアルタイムで推論する。  
ソース内のURLを変更することで、他のカメラ、
mp4等ファイルパスを指定すれば、手持ちの動画ファイルの推論が可能。  

今回使用したカメラ映像は、[Insecam](http://www.insecam.org/)に掲載されているものを使用しました。
### 使用方法
```bash
# object_detector_ImageAIディレクトリ内で
python camera_detector.py
```

## オリジナルモデルのトレーニング＆推論
### 概要
オリジナルのデータセットを使用して、モデル作成を行い、  
作成したモデルを使用して推論を行う。  

fine tuningを実行したかったがImageAIに機能が実装されていなかったため、  
オリジナルモデルの作成としている。
### ファイル
```
predict_dog_ breeds.ipynb
train_dog_breeds.ipynb
```
