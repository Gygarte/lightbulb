import uuid
import streamlit as st
from lightbulb.database.struct_base import BaseData
from lightbulb.utils import split_list_equal

st.set_page_config(
    page_title="Models Inventory", page_icon=":material/robot:", layout="wide"
)
COLOR: dict[str, str] = {"Active": "green", "Draft": "orange", "Archived": "red"}


def data_description(data: BaseData) -> None:
    with st.container(border=True, height=220):
        st.subheader(f"{data.name} (v:{data.version})")
        st.write(f"**Owner:** {data.owner}")
        st.badge(f"{data.status}", color=COLOR.get(data.status, "gray"))
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                label="Details",
                use_container_width=True,
                type="secondary",
                key=f"{uuid.uuid4()}",
            )
        with col2:
            st.button(
                label="Delete",
                use_container_width=True,
                type="primary",
                key=f"{uuid.uuid4()}",
            )


# TODO: refactor this mess
def data_page() -> None:
    """Render the Data page."""
    st.title("Data Page")
    st.write(
        "This page will display various datasets related to wage monitoring. "
        "You can explore different datasets, visualize data trends, and analyze wage statistics."
    )
    _tabs = ["Train Data", "Test Data", "Forecast Data", "Prediction"]
    _data = ["train_data", "test_data", "forecast_data", "prediction_data"]
    for tab, data in zip(st.tabs(tabs=_tabs), _data):
        with tab:
            for col, d in zip(
                st.columns(3, gap="small"),
                split_list_equal(st.session_state.get(data, [])),
            ):
                with col:
                    for d_item in d:
                        data_description(data=d_item)
