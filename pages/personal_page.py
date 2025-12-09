import streamlit as st


def show_personal_page():
    st.title("箫张跋扈的个人主页")

    # 添加说明信息
    st.info(
        """这是我的个人空间，未来我会逐步推出一些新的功能和内容。你可以通过点击链接访问我的网页，我致力于分享深度学习写论文的相关模块和教程。所有的视频内容都旨在为你提供新的学习机会，让你在观看的过程中收获实用的知识。无论是专业技能、兴趣爱好，还是个人成长方面的知识，我希望能够为大家带来启发和帮助。即便是没有购买课程也必能有所收获""")

    # 添加B站链接
    st.markdown("[🎬 访问我的B站空间](https://space.bilibili.com/478113245)", unsafe_allow_html=True)
    
    # 添加模块缝合视频链接
    st.markdown("这是我的其中两个有关模块缝合的视频链接：")
    st.markdown("- [模块缝合视频 1](https://www.bilibili.com/video/BV1zg4y1C7oP/)")
    st.markdown("- [模块缝合视频 2](https://www.bilibili.com/video/BV1Kw411G7Rw)")


     # 引用图片并放大1.5倍
    # 你可以指定图片宽度，例如将宽度设置为原来1.5倍
    st.image("tupian.jpg", caption="**也可以扫码了解课程哦**", use_column_width=False, width=900)  # 这里的 900 是自定义宽度，可以根据需要调整

    # 说明文字加粗、放大
    # 通过 Markdown 语法可以加粗和增加文字大小
    st.markdown("<h3 style='font-size:20px; font-weight: bold;'>也可以扫码了解课程哦，性价比嘎嘎高！</h3>", unsafe_allow_html=True)
