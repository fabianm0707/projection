import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="2-Year Athletic Performance Projection", layout="wide")

st.title("🏋️‍♂️ 2-Year Athletic Performance Projection")
st.markdown("### Current Baseline (July 2025)")

# Baseline metrics
baseline = {
    "Body Weight (lbs)": 210,
    "Body Fat (%)": "<10%",
    "100m Sprint (s)": 10.7,
    "40-yard Time (s)": 4.49,
    "Vertical Jump (in)": "37-38",
    "225 Bench Reps": 14,
    "Strength Indicator": "70lb Dumbbells"
}

# Convert all values to string to avoid Arrow serialization error
baseline_df = pd.DataFrame(
    [(k, str(v)) for k, v in baseline.items()],
    columns=["Metric", "Value"]
)
st.table(baseline_df)

st.markdown("---")
st.header("📈 Performance Projections Over Time")

# Projection data
data = {
    "Time": ["Baseline", "6 Months", "12 Months", "18 Months", "24 Months"],
    "Body Weight": [210, 216.5, 222.5, 227.5, 232.5],
    "Body Fat %": [9.5, 9, 8.5, 8, 7.5],
    "100m Sprint": [10.7, 10.55, 10.4, 10.2, 10.0],
    "40-yard Time": [4.49, 4.43, 4.375, 4.325, 4.275],
    "Vertical Jump": [37.5, 40, 42, 43.5, 45.5],
    "225 Bench Reps": [14, 18, 21, 24, 27],
    "Strength Gain %": [0, 17.5, 27.5, 37.5, 45]
}
df = pd.DataFrame(data)

# Line charts
metrics = ["Body Weight", "Body Fat %", "100m Sprint", "40-yard Time", "Vertical Jump", "225 Bench Reps", "Strength Gain %"]

for metric in metrics:
    fig, ax = plt.subplots()
    ax.plot(df["Time"], df[metric], marker='o')
    ax.set_title(f"{metric} Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel(metric)
    st.pyplot(fig)

st.markdown("---")
st.header("Training Phases")

phases = {
    "Fall Camp (July-Aug)": "High-volume strength (4x4, 3x3 @ 65-75%)",
    "In-Season (Sep-Dec)": "Maintenance phase with competition focus",
    "Post-Season (Jan)": "Transition toward off-season development"
}
st.subheader("Periodization Plan")
st.json(phases)

st.markdown("---")
st.header("Key Phase Benefits")

st.markdown("#### Fall Camp Benefits")
st.markdown("""
- Strength foundation building  
- Movement refinement  
- Work capacity development  
""")

st.markdown("#### In-Season Maintenance")
st.markdown("""
- Preserve strength/power  
- Prevent injuries  
- Game-specific conditioning  
""")

st.markdown("#### Off-Season Development")
st.markdown("""
- Maximize strength  
- Develop power  
- Refine speed technique  
""")

st.markdown("---")
st.header("Influencing Factors")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Positive Factors")
    st.markdown("""
    - Young athlete with high baseline  
    - Structured, periodized plan  
    - Low body fat  
    - Strong power metrics (vertical)  
    """)

with col2:
    st.markdown("#### Limiting Factors")
    st.markdown("""
    - Nearing genetic ceiling by 18 months  
    - Injury risks in contact sport  
    - Nutrition and sleep consistency  
    """)

st.markdown("---")
st.header("Training Recommendations")

st.markdown("#### Months 1-6: Foundation Phase")
st.markdown("- Posterior chain focus\n- Strength base building\n- Speed 2x/week")

st.markdown("#### Months 7-12: Development Phase")
st.markdown("- More power work\n- Plyometrics\n- Sport-specific skills")

st.markdown("#### Months 13-18: Specialization Phase")
st.markdown("- Peak strength\n- Advanced speed\n- Comp prep")

st.markdown("#### Months 19-24: Peak Performance")
st.markdown("- Maintain gains\n- Injury prevention\n- Tactical readiness")

st.markdown("---")
st.header("Summary of Expected Outcomes")

st.success("""
- Speed: 0.6–0.8s 100m improvement  
- Power: +7–9” vertical  
- Strength: +11–14 reps on 225 test  
- Lean Mass: +20–25 lbs  
- Status: From college level to pro-level athleticism  
""")
