#! /usr/bin/python
# -*- coding: utf-8 -*-
u"""dlibによる顔画像検出."""
import cv2
import dlib

# このスクリプトを単体で実行する場合はここにファイルパスを指定
sample_img_path = 'sample.jpg'
# svmファイルの指定, 自作svmを使う時はここ修正と15行目, 23行目くらいのコメントを使ってよしなに
svm = 'detector.svm'

def facedetector_dlib(img, image_path):
    try:
        # dlib標準の顔検出 frontal_face_detector クラス
        # detector = dlib.simple_object_detector(svm)
        detector = dlib.get_frontal_face_detector()

        # RGB変換 (opencv形式からskimage形式に変換)
        # 公式のデモだとskimage使ってるのでそちらが良いかも
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # frontal_face_detectorクラスは矩形, スコア, サブ検出器の結果を返す
        # 引数のupsample_numを設定すると画像の見る枚数が増えるため精度が向上するがその分探索時間とメモリを要する
        # dets = detector(img_rgb, 0)
        dets, scores, idx = detector.run(img_rgb, 0)

        # 矩形の色
        color = (0, 0, 255)
        s = ''
        if len(dets) > 0:
            # 顔画像ありと判断された場合
            for i, rect in enumerate(dets):
                # detsが矩形, scoreはスコア、idxはサブ検出器の結果(0.0がメインで数が大きい程弱い)
                # print rect, scores[i], idx[i]

                # 矩形を作って書く
                cv2.rectangle(img, (rect.left(), rect.top()), (rect.right(), rect.bottom()), color, thickness=10)
                # 矩形情報を保存
                s += (str(rect.left()) + ' ' + str(rect.top()) + ' ' + str(rect.right()) + ' ' + str(rect.bottom()) + ' ')
            # 画像情報
            s += image_path
        # 矩形が書き込まれた画像とs = 'x1 y1 x2 y2 x1 y1 x2 y2 file_name'
        # 顔が無ければ s='' が返る
        return img, s

    except:
        # メモリエラーの時など
        return img, ""

if __name__ == '__main__':
    # 画像読み込み
    img = cv2.imread(sample_img_path)

    # dlib
    img, s = facedetector_dlib(img, sample_img_path)

    # 画像出力
    cv2.imwrite('output_' + sample_img_path, img)

    # 矩形情報出力
    f = open('./rect.txt', 'w')
    f.write(s)
    f.close()
