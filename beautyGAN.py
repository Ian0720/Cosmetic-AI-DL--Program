# 원본 Source Code가 tensorflow 1.x 버전이므로, 저같은 경우는 2.x버전을 사용하고 있다보니
# 원문에서 수정하여, 2.x버전에 맞추었음을 이해 바랍니다.

import tensorflow.compat.v1 as tf 
# 이렇게 작성을 해주어야지, 2.x버전에서도 호환이 이루어집니다.
import numpy as np 
import os 
import glob 
from imageio import imread, imsave
# 'imageio'는 pip install imageio를 해주시면 설치가 됩니다.

import cv2
# OpenCV는 일반적으로, 객체, 얼굴 및 행동 인식, 독순, 모션 추적 등의 응용프로그램에서 사용이 됩니다.
# OpenCV는 'Open Source Computer Vision'의 줄인말이며, 이미지 인식 및 분류를 위해 필수적으로 공부하시게 될 것입니다.

# 받는 질문 중, 'No module named cv2'라는 에러를 많이들 접하시는 것 같기에 답변을 링크해봅니다.

# cv2 같은 경우는 'pip install opencv-python'을 해주셔야 설치가 됩니다
# 이는 OpenCV의 메인 모듈로, contrib 모듈(고급형)을 사용하고 싶으시면
# 부수적으로 'pip install opencv-contrib-python'을 해주셔서 설치하시면 됩니다.

import argparse
# 'argparse'모듈은 도움말과 사용방법에 대한 메세지를 자동 생성하고
# 사용자가 프로그램에 잘못된 인자를 주었을 때, 에러를 발생시킵니다.

parser = argparse.ArgumentParser()
parser.add_argument('--no_makeup', type=str, default =
os.path.join('C:/AI/BeautyGAN/imgs', 'no_makeup', 'xfsy_0068.png'), help = 'path to the no_makeup image')
args = parser.parse_args()

def preprocess(img):
    return (img / 255. - 0.5) * 2

def deprocess(img):
    return (img + 1) / 2

batch_size = 1
img_size = 256
no_makeup = cv2.resize(imread(args.no_makeup), (img_size, img_size))
X_img = np.expand_dims(preprocess(no_makeup), 0)
makeups = glob.glob(os.path.join('C:/AI/BeautyGAN/imgs', 'makeup', '*.*'))

result = np.ones((2 * img_size, (len(makeups) + 1) * img_size, 3))
result[img_size: 2 * img_size, :img_size] = no_makeup / 255.

with tf.compat.v1.Session() as ses:
    # ses = tf.compat.v1.Session()
    ses.run(tf.global_variables_initializer())
    # 이미 학습한 모델을 읽어서 복원해줍니다.
    saver = tf.train.import_meta_graph(os.path.join('C:/AI/BeautyGAN/models', 'model.meta'))
    saver.restore(ses, tf.train.latest_checkpoint('C:/AI/BeautyGAN/models'))

    graph = tf.get_default_graph()
    X = graph.get_tensor_by_name('X:0')
    Y = graph.get_tensor_by_name('Y:0')
    Xs = graph.get_tensor_by_name('generator/xs:0')
    for i in range(len(makeups)):
        makeup = cv2.resize(imread(makeups[i]), (img_size, img_size))
        Y_img = np.expand_dims(preprocess(makeup), 0)

        # 입력과 결과를 주고 예측합니다.
        Xs_ = ses.run(Xs, feed_dict={X: X_img, Y: Y_img})
        Xs_ = deprocess(Xs_)
        result[:img_size, (i + 1) * img_size: (i + 2)
               * img_size] = makeup / 255.
        result[img_size: 2 * img_size,
               (i + 1) * img_size: (i + 2) * img_size] = Xs_[0]
    imsave('C:/AI/BeautyGAN/result.jpg', result)
