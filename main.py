import streamlit as st
import random

# 과학 꿀팁 리스트
science_tips = [
    "🌡️ 뜨거운 물보다 미지근한 물이 손 씻기에 더 효과적일 수 있어요.",
    "🌞 아침 햇살은 생체 리듬을 조절하고 기분을 좋게 해줘요.",
    "🪴 밤에 식물이 산소를 소비하므로 침실에 너무 많으면 안 좋아요.",
    "🚀 우주에서는 눈물이 둥글게 떠다녀요. 중력이 없으니까요!",
    "☕ 커피는 일시적으로 집중력을 높여주는 뇌 자극제예요.",
    "🧊 절대 영도(-273.15℃)에서는 분자의 움직임이 완전히 멈춰요.",
    "🧬 DNA는 자외선에 의해 쉽게 손상될 수 있어요.",
    "🫧 비누는 바이러스의 지질막을 파괴해서 손 씻기에 효과적이에요.",
    "🍌 바나나는 자연적으로 방사능을 띠는 과일이에요 (칼륨-40 때문).",
    "🌫️ 높은 산에서는 기압이 낮아져 물이 100℃보다 낮은 온도에서 끓어요."
]

# 페이지 제목
st.title("🔬 오늘의 과학 꿀팁")
st.markdown("궁금할 땐 눌러보세요! 꿀팁이 매번 달라져요 🤓")

# 버튼을 누르면 새로운 꿀팁 생성
if st.button("다른 꿀팁 보기 🔄"):
    st.session_state.current_tip = random.choice(science_tips)

# 초기값이 없으면 하나 생성
if 'current_tip' not in st.session_state:
    st.session_state.current_tip = random.choice(science_tips)

# 꿀팁 출력
st.success(st.session_state.current_tip)

# 하단 문구
st.markdown("---")
st.caption("생활 속 과학을 쉽고 재미있게! 🧠✨")
