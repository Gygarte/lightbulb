import streamlit as st
from moonlight.pages.page_models.upload_win import upload_model
from moonlight.pages.page_models.description_card import model_description
from moonlight.utils import split_list_equal

st.set_page_config(
    page_title="Models Inventory", page_icon=":material/robot:", layout="wide"
)


def models_page() -> None:
    """
    Main function for rendering the Models Inventory page.
    """

    st.title("Models inventory")
    st.write("""
             This page allows you to manage your wage models .""")
    st.button(
        label="Upload Model",
        on_click=upload_model,
        use_container_width=True,
    )
    current_models = st.session_state.get("model", None)

    with st.container(border=True):
        st.subheader("Available Models")
        # For each model in the session state, a model description is displayed
        # formatted on 3 colomns inside the container
        if current_models is not None and len(current_models) > 0:
            col1, col2, col3 = st.columns(3, gap="small")
            l1, l2, l3 = split_list_equal(current_models)
            with col1:
                for model in l1:
                    model_description(model=model)
            with col2:
                for model in l2:
                    model_description(model=model)
            with col3:
                for model in l3:
                    model_description(model=model)

        else:
            st.write("No models available. Please upload a model.")

    if current_models is not None and len(current_models) > 0:
        pass
