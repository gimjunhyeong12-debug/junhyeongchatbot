import streamlit as st

st.set_page_config(
    page_title="Streamlit 요소 체험하기",
    page_icon="🧩",
    layout="wide",
)

st.title("🧩 Streamlit 요소를 직접 체험해 보세요")
st.caption("처음 배우는 사람도 쉽게 이해할 수 있는 Streamlit 위젯과 데이터 화면 예시입니다.")

st.markdown(
    """
    이 페이지에서는 Streamlit에서 자주 사용하는 요소를 직접 조작해 볼 수 있습니다.
    각 요소는 특정 역할을 하며, 입력한 값이 화면에 즉시 반영됩니다.
    """
)

with st.expander("📘 Streamlit이란 무엇인가요?", expanded=True):
    st.markdown(
        """
        **Streamlit**은 Python 코드를 이용해 웹 애플리케이션을 빠르게 만드는 도구입니다.
        작은 프로젝트부터 데이터 분석 결과를 보여주는 앱까지 만들 수 있습니다.

        - **입력 요소**: 사용자가 값을 입력하거나 선택할 수 있게 합니다.
        - **출력 요소**: 텍스트, 이미지, 표, 차트, 지도 등을 화면에 보여줍니다.
        - **버튼과 콜백**: 사용자가 버튼을 누를 때 특정 동작을 실행합니다.
        """
    )

st.subheader("1. 텍스트와 기본 출력")
st.write("`st.write()`는 값을 화면에 출력하는 가장 기본적인 요소입니다.")
st.write("아래의 값은 사용자가 입력한 내용에 따라 달라집니다.")

text_input = st.text_input(
    "이름을 입력해 주세요",
    placeholder="예: 홍길동",
    help="이름을 입력하면 결과에 반영됩니다.",
)
st.write(f"입력한 이름: **{text_input or '아직 입력하지 않았습니다.'}**")

st.text_area(
    "메모를 작성해 주세요",
    value="Streamlit을 배우는 중입니다.",
    height=120,
    help="여러 줄의 문장을 입력할 수 있습니다.",
)

st.markdown("---")

st.subheader("2. 버튼과 선택 요소")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 버튼")
    st.write("버튼을 누르면 아래 영역에 사용자가 누른 결과가 표시됩니다.")
    if st.button("🎯 버튼을 눌러 보세요", use_container_width=True):
        st.success("버튼을 눌렀습니다! 버튼은 사용자의 행동을 실행하는 데 사용됩니다.")

with col2:
    st.markdown("### 선택 메뉴")
    st.write("`st.selectbox()`는 여러 항목 중 하나를 선택할 때 사용합니다.")
    favorite = st.selectbox(
        "좋아하는 프로그래밍 언어를 선택하세요",
        ["Python", "JavaScript", "Java", "C++"],
        index=0,
    )
    st.info(f"선택한 언어: **{favorite}**")

st.markdown("### 라디오 버튼")
radio_value = st.radio(
    "진행 정도를 선택하세요",
    options=["처음 시작", "기초 학습", "응용 학습"],
    horizontal=True,
)
st.caption(f"현재 선택: {radio_value}")

st.markdown("### 체크박스")
show_detail = st.checkbox("추가 설명을 표시할까요?", value=True)
if show_detail:
    st.markdown(
        "체크박스는 켜거나 끄는 상태를 나타내는 간단한 선택 요소입니다. "
        "이 값에 따라 다른 내용을 보여줄 수 있습니다."
    )

st.markdown("---")

st.subheader("3. 숫자와 범위 입력")

number_col, slider_col = st.columns(2)

with number_col:
    st.markdown("### 숫자 입력")
    st.write("`st.number_input()`은 숫자를 직접 입력하거나 키보드로 조절할 수 있습니다.")
    count = st.number_input(
        "반복할 횟수를 입력하세요",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
    )
    st.code(f"반복 횟수: {count}")

with slider_col:
    st.markdown("### 슬라이더")
    st.write("슬라이더는 범위 안에서 값을 선택할 때 사용합니다.")
    level = st.slider(
        "완성도를 선택하세요",
        min_value=0,
        max_value=100,
        value=60,
        step=5,
        help="0부터 100까지의 값을 조절할 수 있습니다.",
    )
    st.progress(level / 100)
    st.caption(f"현재 선택한 값: {level}%")

st.markdown("---")

st.subheader("4. 여러 항목 선택과 날짜·시간")

multi_col, date_col = st.columns(2)

with multi_col:
    st.markdown("### 여러 항목 선택")
    topics = st.multiselect(
        "관심 있는 Streamlit 기능을 모두 선택하세요",
        ["텍스트", "버튼", "입력창", "슬라이더", "차트", "데이터 표"],
        default=["텍스트", "버튼"],
    )
    st.write(f"선택한 기능: {', '.join(topics) if topics else '없음'}")

with date_col:
    st.markdown("### 날짜와 시간")
    selected_date = st.date_input("날짜를 선택하세요", help="달력에서 날짜를 선택할 수 있습니다.")
    selected_time = st.time_input("시간을 선택하세요", help="시간을 직접 선택할 수 있습니다.")
    st.write(f"선택한 일정: {selected_date} {selected_time}")

st.markdown("---")

st.subheader("5. 데이터 표와 차트")

st.markdown("### 데이터 표")
st.write("`st.dataframe()`은 데이터와 같은 표 형태의 정보를 보여주는 요소입니다.")

data = [
    {"이름": "가나", "점수": 85, "완료": True},
    {"이름": "다라", "점수": 72, "완료": False},
    {"이름": "마바", "점수": 92, "완료": True},
    {"이름": "사아", "점수": 78, "완료": True},
]

st.dataframe(data, use_container_width=True, hide_index=True)

st.markdown("### 차트")
chart_col, stat_col = st.columns([2, 1])

with chart_col:
    st.write("`st.line_chart()`와 `st.bar_chart()`는 숫자 데이터를 시각적으로 보여줍니다.")
    chart_data = {
        "월": ["1월", "2월", "3월", "4월", "5월"],
        "조회수": [120, 180, 150, 220, 260],
        "방문자": [80, 110, 130, 170, 210],
    }
    st.line_chart(chart_data, x="월", y=["조회수", "방문자"])

with stat_col:
    st.bar_chart({"평가": [85, 72, 92, 78]})
    st.caption("막대 그래프는 각 항목의 크기를 비교하기에 적합합니다.")

st.markdown("---")

st.subheader("6. 파일 업로드와 사용자에게 보여줄 메시지")
file_col, message_col = st.columns(2)

with file_col:
    st.markdown("### 파일 업로드")
    uploaded_file = st.file_uploader(
        "파일을 업로드해 보세요",
        type=["csv", "txt", "png", "jpg"],
    )
    if uploaded_file is not None:
        st.success(f"업로드된 파일: **{uploaded_file.name}**")
        st.caption(f"파일 크기: {uploaded_file.size} bytes")
    else:
        st.info("파일을 선택하면 파일 이름과 크기를 확인할 수 있습니다.")

with message_col:
    st.markdown("### 상태 메시지")
    st.success("성공 메시지입니다.")
    st.warning("주의 메시지입니다.")
    st.error("오류 메시지입니다.")
    st.info("정보 메시지입니다.")

st.markdown("---")

st.subheader("7. 실행 상태와 스피너")

st.write("아래 버튼을 누르면 긴 작업을 실행하는 것처럼 보이는 상태를 표시할 수 있습니다.")
if st.button("⏳ 처리하기", use_container_width=True):
    with st.spinner("처리 중입니다. 잠시만 기다려 주세요..."):
        import time

        time.sleep(1)
    st.balloons()
    st.success("처리가 완료되었습니다!")

st.markdown("---")

st.subheader("8. 사이드바 활용")
st.write("사이드바는 일반 화면과 별도로 중요한 설정을 배치할 때 사용합니다.")

with st.sidebar:
    st.header("🛠️ 사이드바 설정")
    st.markdown("사이드바에서 값을 선택할 수 있습니다.")
    sidebar_theme = st.selectbox("테마를 선택하세요", ["기본", "어두운 테마", "밝은 테마"])
    sidebar_switch = st.toggle("사이드바 기능을 활성화할까요?", value=True)
    st.write(f"선택된 테마: **{sidebar_theme}**")
    st.write(f"기능 활성화: **{sidebar_switch}**")

st.markdown("---")

st.subheader("9. 결과 요약")
summary = [
    "텍스트와 버튼은 사용자의 행동을 보여줍니다.",
    "입력창과 슬라이더는 값을 받아서 다른 화면에 반영합니다.",
    "체크박스와 선택 메뉴로 기능을 켜거나 옵션을 고를 수 있습니다.",
    "표와 차트는 데이터를 쉽게 비교하고 이해할 수 있도록 합니다.",
    "사이드바는 설명이나 설정을 별도로 구성하는 데 사용합니다.",
]

st.markdown("\n".join(f"- {item}" for item in summary))

st.download_button(
    "📥 예시 설명서를 다운로드하세요",
    data="Streamlit은 Python으로 웹 애플리케이션을 만들 수 있는 도구입니다.\n\n이 페이지에서는 텍스트, 버튼, 입력창, 슬라이더, 체크박스, 데이터 표, 차트, 파일 업로드, 상태 메시지, 스피너, 사이드바 등을 체험할 수 있습니다.",
    file_name="streamlit_element_guide.txt",
    mime="text/plain",
)

st.caption("이 예제는 Streamlit의 여러 요소를 간단하게 설명하고 직접 확인할 수 있게 구성한 페이지입니다.")
