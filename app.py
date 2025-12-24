import streamlit as st
from pathlib import Path

# URL public tới thư mục asset trên GitHub (raw). Đổi <user>/<branch> cho đúng.
base_url = "https://raw.githubusercontent.com/nguyenhuyduchieu/christmas/main/Me%20Ry%20Chit%20Mot/"

html_path = Path("Me Ry Chit Mot/index ver1.2.html")
html = html_path.read_text(encoding="utf-8")

# Chuyển đường dẫn tương đối thành URL tuyệt đối để iframe tải được
for i in range(1, 6):
    html = html.replace(f"./image{i}.jpeg", f"{base_url}image{i}.jpeg")
html = html.replace("./audio.mp3", f"{base_url}audio.mp3")

# Ẩn tất cả UI của Streamlit
st.set_page_config(
    page_title="Magic Christmas",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# CSS để ẩn header, footer, menu và các phần tử Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    div[data-testid="stToolbar"] {visibility: hidden;}
    div[data-testid="stDecoration"] {visibility: hidden;}
    div[data-testid="stHeader"] {visibility: hidden;}
    #stDecoration {display: none;}
    footer {display: none;}
    header {display: none;}
    .stApp > header {display: none;}
    .stApp > footer {display: none;}
    .stApp > div[data-testid="stToolbar"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.components.v1.html(html, height=900, scrolling=False)