# streamlit_chat.py
import streamlit as st
from zhipuai import ZhipuAI

# 页面配置
st.set_page_config(
    page_title="智谱AI 智能助手",
    page_icon="🤖",
    layout="wide"
)

# 标题
st.title("🤖 智谱AI 智能助手")
st.markdown("基于 GLM-4 模型的多轮对话系统")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 设置")
    
    # API Key 输入
    api_key = st.text_input(
        "API Key",
        value="c810f141e5964fa5bca62e285801166d.lWRsg0Yv7hCl4vwO",
        type="password",
        help="请输入您的智谱AI API Key"
    )
    
    # 模型选择
    model = st.selectbox(
        "选择模型",
        ["glm-4-0520", "glm-4", "glm-3-turbo"],
        index=0
    )
    
    # 温度参数
    temperature = st.slider(
        "Temperature (创造性)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="值越高回答越随机，值越低回答越确定"
    )
    
    # 清空对话按钮
    if st.button("🗑️ 清空对话历史", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("**💡 提示**：输入 'quit' 或点击清空按钮重新开始对话")

# 初始化对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入框
if prompt := st.chat_input("请输入您的问题..."):
    if not api_key:
        st.error("请先在侧边栏输入 API Key！")
        st.stop()
    
    # 添加用户消息到历史记录
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 生成 AI 响应
    with st.chat_message("assistant"):
        try:
            client = ZhipuAI(api_key=api_key)
            
            # 流式调用
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                stream=True,
                temperature=temperature
            )
            
            # 流式显示响应
            message_placeholder = st.empty()
            full_response = ""
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
            
            # 显示完整响应
            message_placeholder.markdown(full_response)
            
            # 添加 AI 响应到历史记录
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response
            })
            
        except Exception as e:
            st.error(f"请求出错：{str(e)}")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"抱歉，发生错误：{str(e)}"
            })