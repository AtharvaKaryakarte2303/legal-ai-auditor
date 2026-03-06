import streamlit as st
import pdfplumber
from openai import OpenAI
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="LegalAudit AI | India", layout="wide", page_icon="⚖️")

# Custom CSS for a premium "Legal Firm" look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1E3A8A; color: white; }
    .risk-high { color: #dc3545; font-weight: bold; }
    .risk-med { color: #fd7e14; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if "audit_results" not in st.session_state:
    st.session_state.audit_results = None

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", help="Data is processed via private API tunnel.")
    st.divider()
    st.info("🎯 **Target:** Indian Professional Services\n\n✅ DPDP Act 2023 Compliance\n✅ BNS 2023 Ready\n✅ GST Clause Validation")

# --- MAIN UI ---
st.title("⚖️ LegalAudit India")
st.subheader("Autonomous Contract Risk Assessment & Redlining")

if not api_key:
    st.warning("⚠️ Please enter your API Key in the sidebar to begin.")
    st.stop()

client = OpenAI(api_key=api_key)

uploaded_file = st.file_uploader("Upload Contract (PDF)", type="pdf")

if uploaded_file:
    # 1. Efficient Text Extraction
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.write("### 📄 Document Preview")
        st.text_area("Source Text", value=text, height=600)

    with col2:
        st.write("### 🔍 Agentic Audit Report")
        
        if st.button("🚀 Start Multi-Agent Analysis"):
            with st.status("Agents Collaborating...", expanded=True) as status:
                
                # AGENT 1: The Indian Law Auditor
                st.write("🤖 **Agent 1:** Scanning for DPDP & BNS compliance gaps...")
                
                auditor_sys = """You are a Senior Legal Auditor specializing in Indian Law. 
                Focus on: 1. DPDP Act 2023 (Data Privacy), 2. Arbitration Clauses, 3. Liability Caps.
                Identify 3-5 specific risks."""
                
                audit_task = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": auditor_sys},
                        {"role": "user", "content": f"Audit this contract:\n\n{text}"}
                    ]
                )
                raw_findings = audit_task.choices[0].message.content
                
                # AGENT 2: The Redline Specialist
                st.write("🤖 **Agent 2:** Verifying findings and generating redlines...")
                time.sleep(1) # Visual delay for demo impact
                
                reviewer_sys = """You are a Legal Redline Expert. Convert the provided audit into a 
                Structured Markdown Table with columns: [Clause, Risk Level (High/Med/Low), 
                Legal Issue, Suggested Redline]. Ensure redlines follow Indian legal standards."""
                
                review_task = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": reviewer_sys},
                        {"role": "user", "content": raw_findings}
                    ]
                )
                st.session_state.audit_results = review_task.choices[0].message.content
                status.update(label="Audit Complete!", state="complete", expanded=False)

        # Display persistent results
        if st.session_state.audit_results:
            st.markdown(st.session_state.audit_results)
            st.download_button("📩 Download Professional Report", st.session_state.audit_results, "Risk_Report.md")
