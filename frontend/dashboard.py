import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(
    page_title="Enterprise Meeting Intelligence",
    layout="wide"
)

st.title("Enterprise Meeting Intelligence Dashboard")

st.subheader("AI Meeting Summarizer")

transcript = st.text_area(
    "Paste Meeting Transcript",
    height=250
)

if st.button("Generate Summary"):

    with st.spinner("Generating AI summary..."):

        response = requests.post(
            "http://127.0.0.1:8000/ai/summarize",
            json={
                "transcript": transcript
            }
        )

        result = response.json()

        st.success("Summary Generated")

        st.write(result["summary"])

st.divider()

st.subheader("Meeting Analytics")

analytics_df = pd.DataFrame({
    "Department": [
        "Engineering",
        "Analytics",
        "Product",
        "Management"
    ],
    "Meetings": [25, 18, 12, 8],
    "Productivity": [85, 78, 92, 70]
})

fig = px.bar(
    analytics_df,
    x="Department",
    y="Productivity",
    title="Department Productivity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.pie(
    analytics_df,
    names="Department",
    values="Meetings",
    title="Meeting Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)