import streamlit as st

# Set up the webpage layout
st.set_page_config(page_title="OESC Career Matcher Tool", layout="centered")

# App Header
st.title("🎯 OESC Smart Career Matcher")
st.write("Match your skills against Oklahoma's highest-growth industries.")
st.markdown("---")

# 1. User Input Section
st.subheader("📋 Step 1: Enter Your Professional Profile")
user_name = st.text_input("Full Name")
user_skills_input = st.text_area("Paste your resume summary or list your skills here (comma-separated):", 
                                 placeholder="Example: Customer service, Excel, data entry, communication")

# 2. Industry Selection
st.subheader("📈 Step 2: Choose Your Target Oklahoma Industry")
target_industry = st.selectbox(
    "Which high-growth sector from our BLS reports are you targeting?",
    ["Healthcare Support", "Logistics & Supply Chain", "Data Analytics & IT", "Advanced Manufacturing"]
)

# 3. Matching Logic Data
industry_requirements = {
    "Healthcare Support": {
        "required": ["communication", "patient care", "cpr", "emr", "scheduling"],
        "cert": "Certified Nursing Assistant (CNA) or BLS Certification",
        "growth": "+14% (High Demand)"
    },
    "Logistics & Supply Chain": {
        "required": ["inventory", "excel", "shipping", "forklift", "safety"],
        "cert": "Certified Logistics Associate (CLA)",
        "growth": "+11% (Steady Growth)"
    },
    "Data Analytics & IT": {
        "required": ["excel", "sql", "tableau", "python", "data entry"],
        "cert": "Google Data Analytics Certificate or Tableau Desktop Certified",
        "growth": "+22% (Critical Demand)"
    },
    "Advanced Manufacturing": {
        "required": ["safety", "blueprints", "quality control", "machining", "math"],
        "cert": "OSHA 10-Hour General Industry Certification",
        "growth": "+8% (Regional Growth)"
    }
}

# 4. Action Button & Results Generator
st.markdown("---")
if st.button("🚀 Analyze My Career Match"):
    if not user_skills_input:
        st.error("Please enter some skills first to run the analysis.")
    else:
        # Process user skills (lowercase for accurate matching)
        user_skills = [s.strip().lower() for s in user_skills_input.split(",")]
        
        # Get target industry data
        industry_data = industry_requirements[target_industry]
        req_skills = industry_data["required"]
        
        # Calculate overlapping skills
        matched_skills = [skill for skill in user_skills if skill in req_skills]
        missing_skills = [skill for skill in req_skills if skill not in user_skills]
        
        # Calculate a mock matching percentage score
        score = int((len(matched_skills) / len(req_skills)) * 100) if req_skills else 0
        
        # Display Results Dashboard
        st.subheader(f"📊 Results for {user_name if user_name else 'Applicant'}")
        
        # Score visual metric
        st.metric(label=f"Match Score for {target_industry}", value=f"{score}%", delta=industry_data["growth"])
        
        # Progress Bar visual
        st.progress(score / 100)
        
        # Breakdown columns
        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.write(f"- {skill.title()}")
            else:
                st.write("*None detected yet.*")
                
        with col2:
            st.warning("🔍 Recommended to Add")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"- {skill.title()}")
            else:
                st.write("*You match all core skills!*")
        
        # Tailored Action Plan Step
        st.markdown("---")
        st.subheader("💡 Your Next Step Plan")
        st.info(f"**Recommended Certification:** To bridge your skill gaps and stand out to local Oklahoma employers, look into getting your **{industry_data['cert']}**.")
        st.markdown("🔗 *Report compiled automatically using your BLS Agent data profile.*")