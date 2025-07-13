import streamlit as st
from moonlight.pages import (
    page_main_about,
    page_main_data,
    page_main_home,
    page_main_map,
    page_main_models,
)


def pages_config() -> list[st.Page]:
    """This function returns a dictionary of Streamlit pages.

    Returns
    -------
    list[st.Page]
        A list of Streamlit Page objects, each representing a page in the application.
    """
    return [
        # st.Page(page=page_main_home.home_page, title="Home", icon=":material/home:"),
        st.Page(
            page=page_main_models.models_page, title="Models", icon=":material/robot:"
        ),
        st.Page(
            page=page_main_data.data_page, title="Data", icon=":material/database:"
        ),
        # st.Page(page=page_main_about.about_page, title="About", icon=":material/info:"),
    ]
