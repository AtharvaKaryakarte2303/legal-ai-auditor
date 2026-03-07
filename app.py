import streamlit as st
import pdfplumber
from google import genai
from google.genai import types
import time

# --- CONFIG ---
st.set_page_config(page_title="LegalAudit AI | Gemini India", layout="wide")

# --- SESSION STATE ---
if "audit_results" not in st.session_state:
    st.session_state.audit_results = None

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    gemini_key = st.text_input("Google AI API Key", type="password", help="Get it free at aistudio.google.com")
    india_mode = st.toggle("DPDP Act 2023 Compliance", value=True)
    st.info("Using Gemini 2.5 Flash (Free Tier)")

if not gemini_key:
    st.warning("⚠️ Enter your Gemini API Key in the sidebar.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=gemini_key)

# --- UI ---
st.title("⚖️ LegalAudit India (Powered by Gemini)")
uploaded_file = st.file_uploader("Upload Indian Legal Contract (PDF)", type="pdf")

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.write("### 📄 Document Preview")
        st.text_area("Source Text", value=text, height=600)

    with col2:
        st.write("### 🔍 Gemini Multi-Agent Audit")
        
        if st.button("🚀 Run Analysis"):
            with st.status("Gemini Agents Collaborating...", expanded=True) as status:
                
                # TASK: Audit & Redline
                prompt = f"""You are a Senior Indian Legal Expert. 
                Audit this contract for risks related to the DPDP Act 2023 and Indian Contract law.
                Format the output as a Markdown Table with: [Clause, Risk Level, Issue, Suggested Redline].
                
                CONTRACT TEXT:
                {text}"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                st.session_state.audit_results = response.text
                status.update(label="Audit Complete!", state="complete", expanded=False)

        if st.session_state.audit_results:
            st.markdown(st.session_state.audit_results)
            st.download_button("📩 Download Report", st.session_state.audit_results, "Legal_Audit_India.md")
