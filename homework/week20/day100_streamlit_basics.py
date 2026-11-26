# Day 100 · Streamlit 输入界面：不调用 API
import streamlit as st

st.set_page_config(page_title="Super PPT")
st.title("Super PPT")
st.write("输入主题，生成一份带质量检查的PPT")

topic = st.text_input(
    "PPT 主题",
    placeholder="例如：给大一学生将牛顿第二定律",
)

use_doc = st.checkbox("使用 Markdown/TXT 文档")

uploaded_file = None
if use_doc:
    uploaded_file = st.file_uploader(
        "上传资料",
        type=["md", "txt"],
    )

if st.button("预览输入"):
    if not topic.strip():
        st.warning("请先输入 PPT 主题")

    elif use_doc and uploaded_file is None:
        st.warning("已选择文档模式，请上传 .md 或 .txt 文件")

    else:
        mode = "RAG 文档模式" if use_doc else "主题模式"
        st.success("输入检查通过")
        st.write(f"模式：{mode}")
        st.write(f"主题：{topic}")

        if uploaded_file is not None:
            st.write(f"文件：{uploaded_file.name}")
            st.write(f"大小：{uploaded_file.size} 字节")
