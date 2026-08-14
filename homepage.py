import streamlit as st
import pandas as pd

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
# 2. 커스텀 CSS 스타일링
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        padding: 2.2rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #b0bec5;
        font-weight: 400;
    }

    .custom-card {
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.5rem;
        background-color: #ffffff;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    
    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 사이드바 (메뉴)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚓ **광명기전**")
    st.caption("선박 전기 공사 · 수리 · 전장 전문")
    st.divider()
    
    menu = st.radio(
        "메뉴 바로가기", 
        ["회사 소개", "주요 서비스", "오시는 길 & 문의"],
        index=0
    )
    
    st.divider()
    st.markdown("### 📞 긴급 수리 문의")
    st.markdown("**이곤희:** `010-3872-0031`")
    st.caption("항구 및 조선소 출장 가능")

# -----------------------------------------------------------------------------
# 4. 메인 화면 - 회사 소개
# -----------------------------------------------------------------------------
if menu == "회사 소개":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">⚓ (주)광명기전</div>
        <div class="hero-subtitle">해양 환경에 최적화된 최상의 선박 전기 설비 및 신속 출장 수리 솔루션</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.1, 1], gap="large")
    
    with col1:
        # 최신 버전에 맞춰 use_container_width=True 로 지정
        st.image(
            "https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=800&q=80", 
            caption="광명기전 선박 전장 시공 및 수리 현장", 
            use_container_width=True
        )
        
    with col2:
        st.markdown("### 🌊 **신뢰와 기술력으로 보답하는 파트너**")
        st.write("""
        안녕하십니까, **광명기전** 웹사이트를 방문해 주셔서 감사합니다.
        
        저희 광명기전은 각종 선박(어선, 화물선, 여객선, 관공선 등)의 **전기 설비 신설, 전장 배선, 알람/제어반 제작 및 긴급 수리**를 전문으로 하는 기술 기업입니다.
        
        염해와 진동이 극심한 해양 환경 속에서도 완벽하게 작동할 수 있도록 **엄격한 안전 기준과 정밀한 시공**을 약속드립니다.
        """)
        
        st.markdown("""
        <div class="custom-card">
            <h4 style="margin-top:0;">💡 광명기전의 핵심 경쟁력</h4>
            <p>✔️ <b>24시간 긴급 출장:</b> 주요 항구 및 조선소 즉시 대응</p>
            <p>✔️ <b>맞춤형 전장 설계:</b> 선박 구조에 최적화된 케이블 & 배전반 시공</p>
            <p style="margin-bottom:0;">✔️ <b>정기 검사 완벽 대비:</b> 절연 저항 측정 및 정밀 안전 점검</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. 메인 화면 - 주요 서비스
# -----------------------------------------------------------------------------
elif menu == "주요 서비스":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">⚙️ 주요 서비스 분야</div>
        <div class="hero-subtitle">광명기전이 제공하는 전문 선박 전기 · 전장 종합 솔루션입니다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top:0;">🚢 선박 전기 공사 & 전장 배선</h3>
            <ul>
                <li><b>신조선 & 개보수 전장 공사</b>
                    <ul><li>해양 전용 케이블 포설 및 정밀 배선</li></ul>
                </li>
                <li><b>배전반 & 제어반 제작/설치</b>
                    <ul><li>메인 배전반(MSBD) 및 자동 제어 시스템</li></ul>
                </li>
                <li><b>조명 & 비상 전원 설비</b>
                    <ul><li>고효율 LED 항해등, 작업등, 비상 등화 설치</li></ul>
                </li>
            </ul>
        </div>
        
        <div class="custom-card">
            <h3 style="margin-top:0;">🔌 항해 · 통신 장비 전원 정비</h3>
            <ul>
                <li>레이다, GPS, 어군탐지기 전원 안정화</li>
                <li>노후 통신 케이블 교체 및 신호 간섭/잡음 해결</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top:0;">🛠️ 선박 전기 긴급 수리 & 복구</h3>
            <ul>
                <li><b>발전기 & 모터 정밀 진단</b>
                    <ul><li>출력 이상, 과부하, 절연 저하 긴급 복구</li></ul>
                </li>
                <li><b>알람 & 경보 시스템 정비</b>
                    <ul><li>엔진 경보, 누전 감지기, 화재 감지 시스템</li></ul>
                </li>
                <li><b>누전 & 단선 탐지</b>
                    <ul><li>염해 및 부식에 의한 누전부 정밀 진단</li></ul>
                </li>
            </ul>
        </div>
        
        <div class="custom-card">
            <h3 style="margin-top:0;">📋 선박 정기 검사 대비 점검</h3>
            <ul>
                <li>선박 안전 검사 기준에 맞춘 사전 총괄 점검</li>
                <li>절연 저항 측정 데이터 제공 및 보수 작업</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 메인 화면 - 오시는 길 & 문의
# -----------------------------------------------------------------------------
elif menu == "오시는 길 & 문의":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📞 오시는 길 & 상담 문의</div>
        <div class="hero-subtitle">언제든 문의해 주시면 친절하고 신속하게 안내해 드리겠습니다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top:0;">📌 업체 정보</h3>
            <p><b>상호명:</b> 광명기전</p>
            <p><b>주요 사업:</b> 선박 전기 공사 / 전장 수리 / 제어반 제작</p>
            <p><b>주소:</b> 울산 남구 장생포고래로213번길 6-33 /p>
            <p><b>대표 전화:</b> 052-123-4567</p>
            <p><b>긴급 출장 직통:</b> 010-3872-0031</p>
            <p style="margin-bottom:0;"><b>이메일:</b> contact@gwangmyeong.com</p>
        </div>
        """, unsafe_allow_html=True)
            
        st.info("💡 **항구 / 조선소 출장 안내:** 전화 문의 후 선박이 계류 중인 항구 위치를 말씀해 주시면 현장 출장 점검이 가능합니다.")
        
    with col2:
        st.markdown("### 🗺️ **오시는 길 (위치)**")
        df = pd.DataFrame({
            'lat': [35.0912],
            'lon': [129.0436]
        })
        st.map(df, zoom=13)
