import base64
from openai import OpenAI
import os
import sys
import cv2

class ChatGPT:
    def __init__(self):
        self.model = "gpt-4o-mini"
        self.client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"]
        )
        self.timeout_sec = 15

        if self.check_api_connection():
            print("Hello ChatGPT!")
        else:
            print("Error ChatGPT")
            sys.exit(0)

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def cv_to_base64(self, cv_image):
        _, encoded = cv2.imencode(".jpg", cv_image)
        img_str = base64.b64encode(encoded).decode("utf-8")

        return img_str

    def ask_chatgpt(self, prompt_text):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt_text}],
                max_tokens=10,
                timeout=self.timeout_sec,
            )
        except Exception as e:
            print(f"An error occurred: {e}")
            return False, ""

        return True, response.choices[0].message.content

    def ask_chatgpt_with_image(self, prompt_cv_image, prompt_text):
        base64_image = self.cv_to_base64(prompt_cv_image)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt_text},
                            {"type": "image_url", "image_url":{"url": f"data:image/jpeg;base64,{base64_image}"}},
                        ],
                    }
                ],
                max_tokens=300,
                timeout=self.timeout_sec,
            )
        except Exception as e:
            print(f"An error occurred: {e}")
            return False, ""

        return True, response.choices[0].message.content

    def check_api_connection(self):
        is_connection, msg = self.ask_chatgpt(prompt_text="Hi")

        return is_connection

if __name__ == '__main__':
    print("hello")
