import streamlit as st
import os
import sys

# 设置页面配置必须是第一个 Streamlit 命令
st.set_page_config(
    page_title="论文写作助手",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 添加项目根目录到 Python 路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from pages.gpt_prompts import show_gpt_prompts
from pages.module_chat import show_module_chat
from pages.personal_page import show_personal_page

# 侧边栏导航
with st.sidebar:
    st.title("功能导航")
    selected_page = st.radio(
        "选择功能:",
        ["学术论文写作GPT提示词", "模块缝合专项对话", "箫张跋扈的个人主页"]
    )

# 根据选择显示不同页面
if selected_page == "学术论文写作GPT提示词":
    show_gpt_prompts()
elif selected_page == "模块缝合专项对话":
    show_module_chat()
else:
    show_personal_page() 