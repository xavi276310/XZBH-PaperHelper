import streamlit as st
from utils.helpers import save_chat_history, load_chat_history

def show_module_chat():
    st.title("模块缝合专项对话")
    
    # 添加提醒信息
    st.info("⚠️ ps：目前希望能够把2600+人群的聊天记录作为语料库与GPT结合做出一个模块缝合对话助手，会处理掉个人信息，希望顺利，敬请期待")
    
    # 创建两列布局
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("对话历史")
        # 加载聊天历史
        chats = load_chat_history()
        for chat in chats:
            if st.button(f"对话 {chat['date']}"):
                st.session_state.selected_chat = chat
                
        # 开始新对话的按钮
        if st.button("🆕 新对话"):
            st.session_state.new_chat = True
            
    with col2:
        st.subheader("当前对话")
        # 显示对话内容
        if 'selected_chat' in st.session_state:
            for message in st.session_state.selected_chat['messages']:
                with st.chat_message(message['role']):
                    st.write(message['content'])
        
        # 输入框
        user_input = st.chat_input("输入您的问题...")
        if user_input:
            # 处理用户输入
            pass 