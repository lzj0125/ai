# zhipuAuth.py   用户鉴权
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO")  # 请填写您自己的API Key
response = client.chat.completions.create(
  model="glm-4-0520",  # 填写需要调用的模型编码
  messages=[
      {"role": "user", "content": "你好！你会干什么"},
  ],
  stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)
