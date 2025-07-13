import streamlit as st
import pandas as pd


@st.fragment()
def preview_data(data: pd.DataFrame) -> None:
    """Renders a preview of the loaded data in the Streamlit application.


    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to be previewed.

    """
    # This section allows a preview of the loaded data
    with st.expander("Preview Data", expanded=False):
        # Create a slider to select a number of rows to be displayed
        n_rows: int = st.slider(
            label="Display number of rows",
            min_value=1,
            max_value=(50 if 50 <= len(data) else len(data)),
            value=5,
        )
        # Show a preview of the data
        st.dataframe(data.iloc[:n_rows])
