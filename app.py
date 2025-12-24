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

st.set_page_config(page_title="Magic Christmas", layout="wide")
st.components.v1.html(html, height=900, scrolling=False)