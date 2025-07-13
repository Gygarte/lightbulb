import streamlit as st
from moonlight.database.struct_base import BaseModel
from moonlight.layout import STATUS_COLOR


@st.dialog(title="Model Description", width="large")
def model_description_popup(model: BaseModel) -> None:
    """
    Renders a popup dialog with the model description in the Wage Monitor application.

    Parameters:
    - model: WageModel instance containing the model information.
    """
    st.badge(f"{model.status}", color=STATUS_COLOR.get(model.status, "gray"))
    with st.container(border=True):
        st.write(
            f"**Model name:** {model.name} | **Version:** {model.version} | "
            f"**Calibration Date:** {model.calibration_date}"
            f" | **Type:** {model.type}"
            f" | **Owner:** {model.owner}"
            f" | **Description:** {model.description}"
        )
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        tabs=[
            "Model Summary",
            "Model Validation",
            "Train Data",
            "Test Data",
            "Forecast Data",
            "Prediction",
        ]
    )
    with tab1:
        # Display the model summary
        if model.model is not None:
            st.write(model.model.summary())
        else:
            st.write(
                "Model is not fitted yet. Please fit the model before viewing the summary."
            )
    with tab2:
        # Display the model validation results
        st.write("Model validation is not implemented yet.")
    with tab3:
        # TODO: implement train data display
        pass
    with tab4:
        pass
    with tab5:
        st.write("Forecast data is not implemented yet.")
    with tab6:
        pass
