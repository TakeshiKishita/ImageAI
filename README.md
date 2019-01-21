# ImageAIを使った物体検知

## 概要
勉強会で紹介した、簡単に物体検知を体験するためのソースコードです。  

IPカメラで取得した映像を、リアルタイムで推論します。  
ソース内のURLを変更することで、他のカメラ、
mp4等ファイルパスを指定すれば、手持ちの動画ファイルの推論が可能です。  

今回使用したカメラ映像は、[Insecam](http://www.insecam.org/)に掲載されているものを使用しました。

## 動作環境
Python 3.5.1 (and later versions)  
Tensorflow 1.4.0 (and later versions)  
Keras 2.x  
ImageAI 2.0.2

詳細は[ImageAIのGitHub](https://github.com/OlafenwaMoses/ImageAI)を確認して下さい。  

## 使用方法
```bash
# object_detector_ImageAIディレクトリ内で
python camera_detector.py
```
