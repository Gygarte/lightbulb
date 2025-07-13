import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Home", layout="wide")


@st.fragment(run_every=2 * 60)
def summary_section() -> None:
    col1, col2, col3, col4 = st.columns(4, border=True, gap="small")

    with col1:
        st.metric(label="TOTAL COST (RON)", value="$100,000", delta="$5,000")
    with col2:
        st.metric(label="TOTAL COST (EUR)", value="$50,000", delta="$2,000")
    with col3:
        st.metric(label="DIRECT EMPLOYEES", value="200", delta="10")
    with col4:
        st.metric(label="INDIRECT EMPLOYEES", value="100", delta="5")


@st.fragment
def model_adjustments_section() -> None:
    # Main laylout
    col1, col2 = st.columns(2, border=True, gap="small")

    with col1:
        line_fig = px.line(
            x=[1, 2, 3, 4, 5],
            y=[10, 15, 13, 17, 20],
            title="Sample Line Chart",
        )
        st.plotly_chart(line_fig, use_container_width=True, key="fig_1")

    with col2:
        # Adjustment panel layout
        with st.expander(label="Adjustment Panel", expanded=False):
            _v1 = st.slider(
                label="Adjustment Panel",
                label_visibility="hidden",
                width=250,
                min_value=0,
                max_value=100,
                step=10,
                key="s_1",
            )
        with st.expander(label="Adjustment Panel", expanded=False):
            _v2 = st.slider(
                label="Adjustment Panel",
                label_visibility="hidden",
                width=250,
                min_value=0,
                max_value=100,
                step=10,
                key="s_2",
            )
        with st.expander(label="Adjustment Panel", expanded=False):
            _v3 = st.slider(
                label="Adjustment Panel",
                label_visibility="hidden",
                width=250,
                min_value=0,
                max_value=100,
                step=10,
                key="s_3",
            )
        with st.expander(label="Adjustment Panel", expanded=False):
            _v4 = st.slider(
                label="Adjustment Panel",
                label_visibility="hidden",
                width=250,
                min_value=0,
                max_value=100,
                step=10,
                key="s_4",
            )
        with st.expander(label="Adjustment Panel", expanded=False):
            _v5 = st.slider(
                label="Adjustment Panel",
                label_visibility="hidden",
                width=250,
                min_value=0,
                max_value=100,
                step=10,
                key="s_5",
            )
        with st.expander(label="Forecasts", expanded=False):
            st.multiselect(
                label="Select Forecast",
                label_visibility="hidden",
                options=["Forecast 1", "Forecast 2", "Forecast 3"],
                key="forecast_select",
            )


@st.fragment
def chart_section() -> None:
    col1, col2 = st.columns(2, border=True, gap="small")

    with col1:
        line_fig = px.line(
            x=[1, 2, 3, 4, 5],
            y=[10, 15, 13, 17, 20],
            title="Sample Line Chart",
        )
        st.plotly_chart(line_fig, use_container_width=False)

    with col2:
        # Insert a pie chart
        pie_fig = px.pie(
            values=[10, 20, 30],
            names=["Category A", "Category B", "Category C"],
            title="Sample Pie Chart",
        )
        st.plotly_chart(pie_fig, use_container_width=False)


def home_page() -> None:
    # Add custom CSS to scale the entire app
    row1 = st.container(border=True)
    row2 = st.container(border=True)
    row3 = st.container(border=True)

    # Wage cost summary section
    with row1:
        summary_section()

    # Model section
    tab1, tab2 = st.tabs(tabs=["Overview", "Model"])
    with tab1:
        chart_section()
    # Other section
    with tab2:
        model_adjustments_section()
