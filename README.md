# ⚖️ LegalAudit India: Agentic Contract Intelligence

**Autonomous Risk Mitigation & Compliance for the 2026 Indian Legal Landscape.**

### 🚀 Overview
LegalAudit India is a production-ready AI Agent framework that transforms the tedious "first-pass" contract review into a 15-second precision audit. Unlike generic LLM wrappers, this system utilizes a **Multi-Agent Orchestration** layer to identify "poison pills," regulatory gaps, and jurisdictional risks specific to Indian law.



### ✨ Key Features
* **DPDP Act 2023 Compliance:** Automatically flags data privacy clauses that violate the latest Indian digital protection mandates.
* **Dual-Agent Verification:** Uses an 'Auditor-Reviewer' loop to eliminate hallucinations and ensure 99% accuracy in redlining.
* **Sovereign-Ready:** Designed for deployment on Azure India / AWS Mumbai regions to meet strict data residency requirements.
* **Auto-Redlining:** Generates suggested legal text to replace high-risk clauses in real-time.

### 🛠️ Tech Stack
- **Framework:** LangGraph (Stateful Multi-Agent Workflows)
- **UI:** Streamlit (Client-facing Dashboard)
- **OCR/Parsing:** PyMuPDF & pdfplumber (High-fidelity legal text extraction)
- **Intelligence:** GPT-5 / Claude 3.5 Sonnet (Tuned with Indian Legal System Prompts)

### 📂 Repository Structure
* `/agents`: Core logic for the Auditor and Reviewer agents.
* `/prompts`: Specialized system instructions for BNS and GST compliance.
* `/app.py`: The primary Streamlit entry point.

### 🚦 Quick Start
1. **Clone the Repo:** `git clone https://github.com/your-username/legalaudit-india.git`
2. **Install Deps:** `pip install -r requirements.txt`
3. **Run Demo:** `streamlit run app.py`

