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
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. 모바일 가독성 최적화 커스텀 CSS (상단 가림 현상 수정)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    /* 최상단 헤더 가림 방지 여백 설정 */
    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* 히어로 배너 모바일 반응형 */
    .hero-banner {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        padding: 1.5rem 1.2rem;
        border-radius: 12px;
        margin-top: 0.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: #ffffff;
        word-break: keep-all;
    }
    
    .hero-subtitle {
        font-size: 0.95rem;
        color: #b0bec5;
        font-weight: 400;
        line-height: 1.4;
        word-break: keep-all;
    }

    /* 카드 스타일 최적화 */
    .custom-card {
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.2rem;
        background-color: #ffffff;
        margin-bottom: 1rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }

    .custom-card h3, .custom-card h4 {
        font-size: 1.15rem;
        word-break: keep-all;
    }

    .custom-card p, .custom-card li {
        font-size: 0.95rem;
        line-height: 1.5;
        word-break: keep-all;
    }

    /* 버튼 모바일 가독성 향상 */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }

    /* 모바일 전용 반응형 미디어 쿼리 (상단 공간 확보) */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 4.5rem !important;
        }
        .hero-banner {
            margin-top: 0.8rem;
        }
        .hero-title {
            font-size: 1.4rem;
        }
        .hero-subtitle {
            font-size: 0.88rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 안전한 이미지 출력 함수 (구버전 & 신버전 호환)
# -----------------------------------------------------------------------------
def render_image(image_url, caption=""):
    try:
        # 최신 Streamlit 버전용 (use_container_width)
        st.image(image_url, caption=caption, use_container_width=True)
    except TypeError:
        # 구버전 Streamlit 용 (use_column_width)
        st.image(image_url, caption=caption, use_column_width=True)

# -----------------------------------------------------------------------------
# 4. 사이드바 (메뉴)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚓ **광명기전**")
    st.caption("선박 전기 공사 · 수리 · 전장 전문")
    st.divider()
    
    menu = st.radio(
        "메뉴 선택", 
        ["회사 소개", "주요 서비스", "오시는 길 & 문의"],
        index=0
    )
    
    st.divider()
    st.markdown("### 📞 긴급 수리 문의")
    st.markdown("**대표 이곤희:**  \n[010-3872-0031](tel:010-1234-5678)")
    st.caption("전국 주요 항구 및 조선소 즉시 출장")

# -----------------------------------------------------------------------------
# 5. 메인 화면 - 회사 소개
# -----------------------------------------------------------------------------
if menu == "회사 소개":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">⚓ (주)광명기전</div>
        <div class="hero-subtitle">해양 환경에 최적화된 선박 전기 설비 & 신속 출장 수리 전문</div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- 달력 배치 ---
    with st.expander("📅 **출장 수리 및 점검 희망일 달력 확인하기**", expanded=True):
        selected_date = st.date_input(
            "희망하시는 방문/점검 날짜를 선택해 주세요:",
            value=datetime.date.today(),
            min_value=datetime.date.today()
        )
        st.caption(f"💡 선택하신 날짜: **{selected_date.strftime('%Y년 %m월 %d일')}** (전화 문의 시 선택하신 날짜를 말씀해 주시면 신속히 일정 접수가 가능합니다.)")

    st.divider()

    render_image(
        "https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=800&q=80", 
        caption="광명기전 선박 전장 시공 및 수리 현장"
    )
    
    st.markdown("### 🌊 **신뢰와 기술력의 파트너**")
    st.write("""
    저희 **광명기전**은 어선·화물선·여객선·관공선 등 각종 선박의 **전기 설비 신설, 전장 배선, 제어반 제작 및 긴급 수리**를 전문으로 합니다.
    
    극심한 염해와 진동 속에서도 안전하게 작동하도록 **엄격한 기준의 정밀 시공**을 약속드립니다.
    """)
    
    st.markdown("""
    <div class="custom-card">
        <h4 style="margin-top:0;">💡 광명기전 핵심 경쟁력</h4>
        <p>✔️ <b>24시간 긴급 출장:</b> 주요 항구/조선소 즉시 대응</p>
        <p>✔️ <b>맞춤형 전장 설계:</b> 케이블 포설 & 배전반 시공</p>
        <p style="margin-bottom:0;">✔️ <b>정기 검사 대비:</b> 절연 저항 측정 & 정밀 점검</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 메인 화면 - 주요 서비스
# -----------------------------------------------------------------------------
elif menu == "주요 서비스":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">⚙️ 주요 서비스 분야</div>
        <div class="hero-subtitle">광명기전의 전문 선박 전기 · 전장 종합 솔루션입니다.</div>
    </div>
    """, unsafe_allow_html=True)
    
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

# -----------------------------------------------------------------------------
# 7. 메인 화면 - 오시는 길 & 문의
# -----------------------------------------------------------------------------
elif menu == "오시는 길 & 문의":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📞 오시는 길 & 상담 문의</div>
        <div class="hero-subtitle">신속하고 친절하게 안내해 드리겠습니다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-card">
        <h3 style="margin-top:0;">📌 업체 정보</h3>
        <p><b>상호명:</b> 광명기전</p>
        <p><b>주요 사업:</b> 선박 전기 공사 / 전장 수리 / 제어반 제작</p>
        <p><b>주소:</b> 울산 남구 장생포고래로213번길 6-33 (예시 주소)</p>
        <p><b>대표 전화:</b> 051-123-4567</p>
        <p><b>긴급 출장:</b> <a href="tel:010-1234-5678">010-3872-0031</a> (클릭 시 전화 연결)</p>
        <p style="margin-bottom:0;"><b>이메일:</b> contact@gwangmyeong.com</p>
    </div>
    """, unsafe_allow_html=True)
        
    st.info("💡 **출장 안내:** 전화 문의 시 선박이 계류 중인 항구 위치를 말씀해 주시면 즉시 현장 출장이 가능합니다.")
    
    st.markdown("### 🗺️ **위치 안내**")
    df = pd.DataFrame({
        'lat': [35.0912],
        'lon': [129.0436]
    })
    st.map(df, zoom=13)
