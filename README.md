# Cosmetic-AI-Program (화장시켜 주는 인공지능)<br/>
## Intro.<br/>
유명한 AI Program입니다, 모 회사에서는 이 모듈을 응용하여 자체적으로 서비스하는 곳이 있을 정도입니다.<br/>
예시(본인의 사진, 혹은 노메이크업 상태의 얼굴이미지)를 가지고 화장된 모습의 입력된 데이터를 따라 얼굴의 범위를 인식하고<br/>
화장을 했을때 모습을 예측하여 보여주는 형태입니다.<br/>
<br/>

## Explanation<br/>
|Title|Contents|Explain|
|:----:|:----:|:----:|
|beautyGAN.py|화장시켜주는 AI 메인 프로그램|준비된 데이터를 토대로 얼굴을 인식하고<br/>화장된 모습을 예측하여 결과물을 도출해내는 시스템|
|model.meta|학습이 미리 완료된 프로그램|서버를 따로 운용하거나, 고성능의 GPU를 가진 컴퓨터가 아니라면<br/>학습을 하는데 많은 시간이 걸리게 되므로<br/>미리 준비한, 학습된 데이터|<br/>
<br/>

## Data From<br/>
**Pre-Trained-Model :** https://drive.google.com/drive/folders/1pgVqnF2-rnOxcUQ3SO4JwHUFTdiSe5t9<br/>
**Paper :** http://liusi-group.com/projects/BeautyGAN<br/>
**본 프로그램에 대한 출처이며, 이미 학습된 data를 읽어오는 것이 전부입니다.**<br/>
**단, 본문은 tensorflow 1.x 이므로, 제가 tensorflow 2.x에서 호환될 수 있도록 수정하였습니다.**<br/>
<br/>

## Requirements<br/>
- Tensorflow 2.4.1<br/>
- Numpy<br/>
- OS<br/>
- Glob<br/>
- imageio<br/>
&nbsp;- 이 모듈을 활용하기 위해서는 'pip install imageio'를 해주시면 됩니다.<br/>
- cv2<br/>
&nbsp;- OpenCV는 일반적으로 객체, 얼굴 및 모션 추적, 행동 인식 등의 프로그램에서 사용되는 모듈입니다.<br/>
&nbsp;- 인스타그램, 그리고 Gmail로부터 'No module named cv2'라는 메세지가 기록되며 안된다는 말씀을 하셔서 방법을 알려드리겠습니다.<br/>
&nbsp;- cv2같은 경우는, 'pip install opencv-python'을 해주셔야 설치가 되고 사용이 가능해집니다.<br/>
&nbsp;- 이렇게 하시면, 오류를 해결하실 수 있으실 겁니다.<br/>
- argparse<br/>
&nbsp;- argparse 같은 경우는, 도움말과 사용 방법에 대하여 자동으로 문구를 생성하고, 이용자가 프로그램에 잘못된 인자를 입력했을 경우 에러를 발생시킵니다.<br/>
<br/>

## How to apply
- 본 모델은, 당연 전이학습 방법을 통해 얼마든지 각 개인이 원하는대로 응용할 수 있습니다.<br/>
- 전이학습에 대하여 잘 설명해주신 분의 url을 참고해주시면 더욱 이해가 쉬우실 거라 사료됩니다.<br/>
**URL : https://www.youtube.com/watch?v=0u5bNeJngDk**<br/>
- 이와 비슷한 방식의 예제를 추가로 올려드리오니, 참조하시면 되겠습니다.<br/>
**URL : https://www.tensorflow.org/tutorials/images/transfer_learning?hl=ko**<br/>
<br/>

## Incidental Explanation<br/>
- 상위에 게시한 'Tensorflow 예제 사이트'에서는 Cats vs Dogs 라는 데이터셋을 사용합니다.<br/>
- 이름처럼 개와 고양이를 분류하는 용도의 데이터 셋이니 참고하시면 되겠습니다.<br/>
- 'Pre-Trained-Model'은 'MobileNetV2'의 구조로 'imagenet Dataset'에 학습한 모델입니다,<br/>이미지의 엄청난 양을 모아놓은 데이터 셋으로, 모바일넷은 말 그대로 모바일 환경에서 잘 작동되도록 만든 모델입니다.<br/>
- 잠시 설명을 드리자면, 데이터셋을 왕창 모아서 거대한 모델에 훈련을 시키면 성능은 좋아집니다.<br/> 그러나 요즘에는 스마트폰, 외부 카메라 등 작은 디바이스에서도 작동하는 모델에 대해 큰 관심을 보이고 있습니다.<br/> 아시다시피 성능에 제한이 있는 환경들 입니다, 해서 성능은 다소 떨어지더라도 모델의 사이즈를 줄이고, 빠르게 작동하는 모델에 관심이 많이 있습니다.<br/> 이런 분야에 관심있는 사람들이 만들어낸 모델이라고 설명할 수 있겠습니다.
