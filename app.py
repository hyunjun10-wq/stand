
import streamlit as st
import random

st.title("⚡ 죠죠 스탠드 뽑기 ⚡")
st.write("당신의 스탠드는 무엇일까요?")

stands = [
    "스타 플래티나 ⭐",
    "더 월드 ⏰",
    "킬러 퀸 💣",
    "골드 익스피리언스 🌟",
    "실버 채리엇 ⚔️",
    "크레이지 다이아몬드 💎",
    "킹 크림슨 👑",
    "스틱키 핑거즈 ✨",
    "메이드 인 헤븐 🌌",
    "더 핸드 ✋"
]

if st.button("스탠드 뽑기!!"):
    result = random.choice(stands)
    st.success("당신의 스탠드는...")
    st.header(result)
    st.balloons()
