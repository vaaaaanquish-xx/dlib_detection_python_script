Dlibで物体検出するやつ
====

## Script
 - main.py : 指定したディレクトリのファイル全部を顔検出に流す
 - detector_dlib.py
   - dlib標準の顔検出 frontal_face_detector に画像を投げる
   - 学習したsvmを使いたい時はコメントアウトでよしなに
 - dlib_train_detector.py : 学習用のスクリプト(パラメータなんかは中に書いてある)
 - japanese_comment_train_object_detector.txt
   - http://dlib.net/train_object_detector.py.html
   - これ適当に日本語に訳したやつ

## Usage
 - 画像1枚送りたい時はface_detector_dlib.pyで画像へのpathを指定して

    ```python detector_dlib.py```

 - まとめてなげる時はmain.pyで入出力ディレクトリを指定して

    ```python main.py```

 - 学習する時はdlib_train_detector.pyで入出力ディレクトリを指定して

    ```python dlib_train_detector.py```

 - 後はブログ記事を参考に
  http://vaaaaaanquish.hatenablog.com/entry/2016/09/04/143408
