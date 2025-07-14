import pandas as pd
import streamlit as st
from lightbulb.pages.page_models.model_form import model_info_form
from lightbulb.pages.page_models.data_preview import preview_data


@st.dialog(title="Upload Model", width="large")
def upload_model() -> None:
    """Renders the upload model form in the Wage Monitor application."""

    file = st.file_uploader(label="Upload Model Data", type=["xlsx"])
    if (file is not None) and (
        file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        try:
            # By default, the first column is set as the index column
            data = pd.read_excel(file, index_col=0)
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error reading the file: {str(e)}", icon="🚨")

    if ("data" in locals()) and (data.empty is False):
        # Show a preview of the data
        preview_data(data=data)

        # This section allows compleating the model information
        if model_info_form(data=data):
            st.rerun(scope="app")
