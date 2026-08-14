import streamlit as st
import pandas as pd
import datetime

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="광명기전 - 선박 전기 공사 & 수리 전문",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. 최초 접속 팝업 모달
# -----------------------------------------------------------------------------
if hasattr(st, "dialog"):
    @st.dialog("⚓ (주)광명기전")
    def notice_dialog():
        st.markdown("### **선박 전기 공사 & 긴급 출장 수리 전문**")
        st.write("해양 환경에 최적화된 **선박 전기 설비 및 전장 시공** 서비스를 제공합니다.")
        st.info("💡 탭이나 하단 버튼을 이용해 오시는 길 및 출장 예약 일정을 확인해 보세요.")
        if st.button("시작하기", type="primary", use_container_width=True):
            st.rerun()

    if "welcomed" not in st.session_state:
        st.session_state["welcomed"] = True
        notice_dialog()

# -----------------------------------------------------------------------------
# 3. 세션 상태 (페이지 이동) - [오시는 길]을 [출장 예약] 앞으로 순서 변경
# -----------------------------------------------------------------------------
if "page_idx" not in st.session_state:
    st.session_state["page_idx"] = 0

pages = ["🏢 회사 소개", "⚙️ 주요 서비스", "📞 오시는 길 & 문의", "📅 출장 일정 예약"]

def next_page():
    if st.session_state["page_idx"] < len(pages) - 1:
        st.session_state["page_idx"] += 1

def prev_page():
    if st.session_state["page_idx"] > 0:
        st.session_state["page_idx"] -= 1

# -----------------------------------------------------------------------------
# 4. 커스텀 CSS (어두운 배너 & 지마켓 산스 타이틀 & 폰트 스타일)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* 웹폰트 불러오기: 에스코어 드림 & 지마켓 산스 */
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-5Medium.woff');
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-7Bold.woff');
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansBold.woff');
    
    .stApp {
        background-color: #f4f7fb;
    }

    html, body, [class*="css"], .stMarkdown, button, input, select {
        font-family: 'S-CoreDream-5Medium', -apple-system, BlinkMacSystemFont, sans-serif !important;
        letter-spacing: -0.3px;
    }

    h1, h2, h3, h4 {
        font-family: 'S-CoreDream-7Bold', sans-serif !important;
    }

    .block-container {
        padding-top: 3.2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* 어두운 계열의 메인 배너 스타일 */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        padding: 2rem 1.2rem;
        border-radius: 20px;
        margin-bottom: 1.2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.3);
        border: 1px solid #334155;
    }
    
    /* (주)광명기전 전용 굵고 인상적인 Gmarket Sans 폰트 및 크기 확대 */
    .hero-title {
        font-family: 'GmarketSansBold', sans-serif !important;
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
        color: #f8fafc;
        letter-spacing: -0.5px;
    }
    
    .hero-subtitle {
        font-size: 0.95rem;
        color: #94a3b8;
        line-height: 1.4;
    }

    /* 긴급 전화 박스 */
    .call-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 16px;
        padding: 0.9rem;
        text-align: center;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.06);
    }

    .call-box a {
        font-size: 1.15rem;
        font-family: 'S-CoreDream-7Bold', sans-serif;
        color: #0284c7;
        text-decoration: none;
    }

    /* 카드 스타일 */
    .custom-card {
        background: #ffffff;
        border: 1px solid rgba(226, 232, 240, 0.8);
        border-radius: 18px;
        padding: 1.4rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 6px 18px rgba(148, 163, 184, 0.08);
    }

    .custom-card h3, .custom-card h4 {
        font-size: 1.2rem;
        color: #0284c7;
        margin-bottom: 0.6rem;
        word-break: keep-all;
    }

    .custom-card p, .custom-card li {
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.6;
        word-break: keep-all;
    }

    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #e2e8f0;
        padding: 5px;
        border-radius: 14px;
        margin-bottom: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 44px;
        border-radius: 10px;
        color: #64748b;
        font-size: 0.9rem;
        background-color: transparent;
        border: none !important;
        padding: 0 12px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #0284c7 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    /* 버튼 스타일 */
    .stButton > button {
        border-radius: 12px !important;
        padding: 0.6rem 1rem !important;
        font-family: 'S-CoreDream-7Bold', sans-serif !important;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 3.5rem !important;
        }
        .hero-title {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. 안전한 이미지 출력 함수
# -----------------------------------------------------------------------------
def render_image(image_url, caption=""):
    try:
        st.image(image_url, caption=caption, use_container_width=True)
    except TypeError:
        st.image(image_url, caption=caption, use_column_width=True)

# -----------------------------------------------------------------------------
# 6. 어두운 배경의 헤더 배너 & 대형 상호명 타이틀
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">⚓ (주)광명기전</div>
    <div class="hero-subtitle">해양 환경에 최적화된 선박 전기 설비 & 24시간 출장 수리</div>
</div>

<div class="call-box">
    <a href="tel:010-3872-0031">🚨 대표 이곤희 : 010-1234-5678</a>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. 상단 탭
# -----------------------------------------------------------------------------
tabs = st.tabs(pages)

# -----------------------------------------------------------------------------
# 8. 페이지 콘텐츠
# -----------------------------------------------------------------------------

# --- PAGE 1: 회사 소개 ---
with tabs[0]:
    st.subheader("🏢 회사 소개")
    render_image(
        "https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=800&q=80", 
        caption="광명기전 선박 전장 시공 및 수리 현장"
    )
    st.write("""
    저희 **(주)광명기전**은 어선·화물선·여객선·관공선 등 각종 선박의 **전기 설비 신설, 전장 배선, 제어반 제작 및 긴급 수리**를 전문으로 합니다.
    
    극심한 염해와 진동 속에서도 안전하게 작동하도록 **엄격한 기준의 정밀 시공**을 약속드립니다.
    """)
    st.markdown("""
    <div class="custom-card">
        <h4 style="margin-top:0;">💡 광명기전 핵심 경쟁력</h4>
        <p>✔️ <b>24시간 긴급 출장:</b> 주요 항구 및 조선소 즉시 대응</p>
        <p>✔️ <b>맞춤형 전장 설계:</b> 케이블 포설 & 배전반 제작 시공</p>
        <p style="margin-bottom:0;">✔️ <b>정기 검사 대비:</b> 절연 저항 측정 & 정밀 점검</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: 주요 서비스 ---
with tabs[1]:
    st.subheader("⚙️ 주요 서비스 분야")
    st.markdown("""
    <div class="custom-card">
        <h3 style="margin-top:0;">🚢 선박 전기 공사 & 전장 배선</h3>
        <p>• <b>신조선/개보수 전장:</b> 해양 전용 케이블 포설 및 배선</p>
        <p>• <b>배전반/제어반:</b> 메인 배전반(MSBD) 및 자동 제어반</p>
        <p style="margin-bottom:0;">• <b>조명 설비:</b> 고효율 LED 항해등, 작업등, 비상 등화</p>
    </div>

    <div class="custom-card">
        <h3 style="margin-top:0;">🛠️ 긴급 수리 & 누전 복구</h3>
        <p>• <b>발전기/모터:</b> 출력 이상, 과부하, 절연 저하 복구</p>
        <p>• <b>알람 시스템:</b> 엔진 경보, 누전/화재 감지 시스템 정비</p>
        <p style="margin-bottom:0;">• <b>누전 탐지:</b> 염해 부식부 누전/단선 정밀 진단</p>
    </div>

    <div class="custom-card">
        <h3 style="margin-top:0;">🔌 항해·통신 장비 & 정기 검사</h3>
        <p>• 레이다, GPS, 어군탐지기 전원 안정화</p>
        <p style="margin-bottom:0;">• 선박 정기 안전 검사 대비 사전 점검 및 절연 데이터 제공</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 3: 오시는 길 & 문의 (순서 변경 적용) ---
with tabs[2]:
    st.subheader("📞 오시는 길 & 업체 정보")
    st.markdown("""
    <div class="custom-card">
        <p><b>상호명:</b> (주)광명기전</p>
        <p><b>주요 사업:</b> 선박 전기 공사 / 전장 수리 / 제어반 제작</p>
        <p><b>주소:</b> 울산 남구 장생포고래로213번길 (예시 주소)</p>
        <p><b>대표 전화:</b> 051-123-4567</p>
        <p><b>긴급 출장:</b> <a href="tel:010-1234-5678" style="color:#0284c7;">010-1234-5678</a></p>
        <p style="margin-bottom:0;"><b>이메일:</b> contact@gwangmyeong.com</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🗺️ **위치 안내**")
    
    # OpenStreetMap 지도 (높이 250px 지정)
    lat, lon = 35.0912, 129.0436
    map_html = f"""
    <div style="width: 100%; height: 250px; border-radius: 14px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <iframe 
            width="100%" 
            height="250" 
            frameborder="0" 
            scrolling="no" 
            marginheight="0" 
            marginwidth="0" 
            src="https://www.openstreetmap.org/export/embed.html?bbox={lon-0.01}%2C{lat-0.005}%2C{lon+0.01}%2C{lat+0.005}&amp;layer=mapnik&amp;marker={lat}%2C{lon}">
        </iframe>
    </div>
    """
    st.components.v1.html(map_html, height=260)

# --- PAGE 4: 출장 및 점검 달력 예약 ---
with tabs[3]:
    st.subheader("📅 출장 수리 & 점검 일정 확인")
    selected_date = st.date_input(
        "방문/점검 희망 날짜를 선택해 주세요:",
        value=datetime.date.today(),
        min_value=datetime.date.today()
    )
    st.info(f"💡 선택하신 날짜: **{selected_date.strftime('%Y년 %m월 %d일')}**\n\n전화 문의 시 해당 날짜를 말씀해 주시면 신속히 출장 일정을 조정해 드립니다.")

st.divider()

# -----------------------------------------------------------------------------
# 9. 화면 하단 [이전 / 다음] 버튼
# -----------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.button("◀ 이전 내용", on_click=prev_page, use_container_width=True)

with col2:
    st.button("다음 내용 ▶", on_click=next_page, type="primary", use_container_width=True)
