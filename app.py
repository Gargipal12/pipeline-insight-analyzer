import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

st.title("🚀 Pipeline Insight Analyzer")

st.subheader("Pipeline Data")
st.write(df)

# Metrics
st.subheader("Key Metrics")

avg_duration = df["duration"].mean()
success_rate = (df["status"] == "success").mean() * 100

st.write(f"Average Duration: {avg_duration:.2f} sec")
st.write(f"Success Rate: {success_rate:.2f}%")

# Health Score
health_score = success_rate - (avg_duration / 10)

st.subheader("Pipeline Health Score ⭐")
st.write(f"{health_score:.2f}")

# Chart
st.subheader("Project Comparison")
grouped = df.groupby("project")["duration"].mean()
st.bar_chart(grouped)