import cv2
import sys
import time
sys.path.append('/workspace/ros_catkin_ws/src/ros_chatgpt/')
from scripts.chatgpt import ChatGPT

def test_chatgpt():
    gpt = ChatGPT()

    test_data1_path = '/workspace/ros_catkin_ws/src/ros_chatgpt/tests/datas/woman.jpg'
    cv_image = cv2.imread(test_data1_path)

    prompt_text = '画像中に写っているマネキンの洋服について端的に特徴を説明してください'
    st = time.time()
    _, text = gpt.ask_chatgpt_with_image(cv_image, prompt_text)
    print(text)

    print("api呼び出しにかかった時間: {}" .format(time.time()-st))

if __name__ == '__main__':
    test_chatgpt()