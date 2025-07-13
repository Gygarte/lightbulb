import streamlit as st
from moonlight.database.struct_base import BaseModel
from moonlight.pages.page_models.delete_win import delete_model
from moonlight.pages.page_models.description_win import model_description_popup
from moonlight.layout import STATUS_COLOR


def model_description(model: BaseModel) -> None:
    with st.container(border=True, height=220):
        # This section displays some basic information about the model
        st.subheader(
            f"{model.name}/{model.type}/v:{model.version}@{model.calibration_date}"
        )
        st.write(f"**Owner:** {model.owner}")
        st.badge(f"{model.status}", color=STATUS_COLOR.get(model.status, "gray"))

        # This section contains buttons for details and delete actions
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                label="Details",
                on_click=model_description_popup,
                kwargs={"model": model},
                use_container_width=True,
                type="secondary",
                key=f"details_{model.id}",
            )
        with col2:
            st.button(
                label="Delete",
                on_click=delete_model,
                kwargs={"model": model},
                use_container_width=True,
                type="primary",
                key=f"delete_{model.id}",
            )
