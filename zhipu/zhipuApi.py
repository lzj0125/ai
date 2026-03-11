
#  zhipuApi.py    
#   同步调用  
#   调用后即可一次性获得最终结果，Python 代码示例如下：
"""
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
print(response.choices[0].message)
"""

# 异步调用
# 调用后会立即返回一个任务 ID，然后用任务ID查询调用结果（根据模型和参数的不同，通常需要等待10-30秒才能得到最终结果），Python代码示例如下：
"""
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO") # 填写您自己的APIKey
response = client.chat.asyncCompletions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[]
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO") # 填写您自己的APIKey
response = client.chat.asyncCompletions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {
            "role": "user",
            "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"
        }
    ],
)
print(response)
"""

#   流式调用
#   调用后可以流式的实时获取到结果直到结束，Python 代码示例如下：
"""

from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO") # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
        {"role": "user", "content": "我对太阳系的行星非常感兴趣，特别是土星。请提供关于土星的基本信息，包括其大小、组成、环系统和任何独特的天文现象。"},
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)
"""





# 流式输出 + 多轮对话实现
def stream_chat_with_history():
    from zhipuai import ZhipuAI
    
    client = ZhipuAI(api_key="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO")
    
    # 维护对话历史
    messages = []
    
    print("=== 智谱AI 流式多轮对话 ===")
    print("输入 'quit' 退出对话\n")
    
    while True:
        # 获取用户输入
        user_input = input("你：").strip()
        
        if user_input.lower() == 'quit':
            print("对话结束！")
            break
        
        # 添加用户消息到历史记录
        messages.append({"role": "user", "content": user_input})
        
        try:
            # 流式调用
            response = client.chat.completions.create(
                model="glm-4-0520",
                messages=messages,
                stream=True,  # 启用流式输出
            )
            
            print("AI：", end="", flush=True)
            
            # 收集完整响应
            full_response = ""
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
            
            print("\n")  # 换行
            
            # 将 AI 响应添加到历史记录
            messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            print(f"\n请求出错：{e}\n")

if __name__ == "__main__":
    stream_chat_with_history()
