Dlibで物体検出するやつ
====

## Script
 - main.py : 指定したディレクトリのファイル全部を顔検出に流す
 - face_detector_dlib.py : dlib標準の顔検出 frontal_face_detector に画像を投げる

## Usage
 - 画像1枚送りたい時はface_detector_dlib.pyで画像へのpathを指定して

    ```python face_detector_dlib.py```

 - まとめてなげる時はmain.pyで入出力ディレクトリを指定して

    ```python main.py```

 - 後はブログ記事を参考に
