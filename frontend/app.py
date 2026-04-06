import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# 🔥 ADVANCED CSS (STARTUP LEVEL)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-title {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 40px;
}

.glass {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(10px);
    margin-top: 15px;
}

.metric {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

.tag {
    display: inline-block;
    background: #1e293b;
    padding: 6px 12px;
    margin: 5px;
    border-radius: 999px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 HEADER
st.markdown('<div class="main-title">🚀 AI Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Crack ATS. Optimize Resume. Get Hired.</div>', unsafe_allow_html=True)

# 📂 INPUT SECTION
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📄 Upload Resume")
    file = st.file_uploader("", type=["pdf"])

with col2:
    st.markdown("### 💼 Job Description")
    job = st.text_area("", height=400)

# 🚀 BUTTON
if st.button("Analyze Resume"):
    if file and job:

        with st.spinner("Analyzing like a recruiter... 🔍"):
            res = requests.post(
                "http://127.0.0.1:8000/analyze",
                files={"file": file},
                data={"job_desc": job}
            )

            data = res.json()

        # 📊 METRICS
        st.markdown("## 📊 Overview")
        c1, c2, c3 = st.columns(3)

        c1.markdown(f'<div class="glass"><div class="metric">{data["ats_score"]}%</div>ATS Score</div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="glass"><div class="metric">{data["experience_years"]}</div>Experience</div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="glass"><div class="metric">{data["final_score"]}</div>Final Score</div>', unsafe_allow_html=True)

        # 📈 PROGRESS BARS
        st.progress(int(data["ats_score"]))
        st.progress(int(data["final_score"]))

        # 🧠 CONTENT
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## 🧠 Skills")
            st.markdown('<div class="glass">', unsafe_allow_html=True)

            for skill in data["skills"]:
                st.markdown(f'<span class="tag">{skill}</span>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("## 🎯 Skill Gap")
            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.write("✅ Matched Skills")
            for s in data["skill_gap"]["matched"]:
                st.markdown(f"- {s}")

            st.write("❌ Missing Skills")
            for s in data["skill_gap"]["missing"]:
                st.markdown(f"- {s}")

            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("## 🤖 Suggestions")
            st.markdown('<div class="glass">', unsafe_allow_html=True)

            suggestions = data["suggestions"]

            if isinstance(suggestions, list):
                for s in suggestions:
                    st.markdown(f"👉 {s}")
            else:
                st.write(suggestions)

            st.markdown('</div>', unsafe_allow_html=True)

        # 📂 SECTIONS
        st.markdown("## 📂 Resume Breakdown")
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.json(data["sections"])
        st.markdown('</div>', unsafe_allow_html=True)

        # 📥 DOWNLOAD REPORT
        st.download_button(
            label="📥 Download Report",
            data=str(data),
            file_name="resume_analysis.txt"
        )

    else:
        st.warning("Upload resume and job description first!")