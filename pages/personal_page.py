import streamlit as st


def show_personal_page():
    st.title("箫张跋扈的个人主页")

    # 添加说明信息
    st.info(
        """这是我的个人空间，未来我会逐步推出一些新的功能和内容。你可以通过点击链接访问我的网页，我致力于分享深度学习写论文的相关模块和教程。所有的视频内容都旨在为你提供新的学习机会，让你在观看的过程中收获实用的知识。无论是专业技能、兴趣爱好，还是个人成长方面的知识，我希望能够为大家带来启发和帮助。即便是没有购买课程也必能有所收获""")

    # 添加B站链接
    st.markdown("[🎬 访问我的B站空间](https://space.bilibili.com/478113245)", unsafe_allow_html=True) 