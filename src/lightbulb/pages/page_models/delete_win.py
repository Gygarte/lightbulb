import streamlit as st
from lightbulb.database.struct_base import BaseModel


@st.dialog(title="Are you sure?")
def delete_model(model: BaseModel) -> None:
    """
    Deletes the specified model from the session state.

    Parameters:
    - model: WageModel instance to be deleted.
    """

    st.write(f"Are you sure you want to delete the model {model.id}?")
    if st.button(
        label="Yes, delete",
        use_container_width=True,
        type="primary",
    ):
        try:
            models: list[BaseModel] = st.session_state.get("model")
            models.remove(model)
            st.session_state["model"] = models
            st.session_state.db.delete(model)
            st.success(f"Model {model.id} deleted successfully!")
            st.rerun()
        except Exception as e:
            st.error("No models available to delete. Error: " + str(e), icon="🚨")

    if st.button(
        label="No, cancel",
        use_container_width=True,
        type="secondary",
    ):
        st.rerun()
