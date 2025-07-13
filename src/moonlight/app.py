import streamlit as st
from moonlight.pages import pages_config
from moonlight.database.db_manager import DBManager


def init_session_state() -> None:
    """
    Initialize the session state for the application.
    This function sets up the initial state of the application.
    """
    if "model" not in st.session_state:
        st.session_state.setdefault("model", list([]))
    if "train_data" not in st.session_state:
        st.session_state.setdefault("train_data", list([]))
    if "test_data" not in st.session_state:
        st.session_state.setdefault("test_data", list([]))
    if "forecast_data" not in st.session_state:
        st.session_state.setdefault("forecast_data", list([]))
    if "prediction_data" not in st.session_state:
        st.session_state.setdefault("prediction_data", list([]))
    # Initialize the holders of database objects in the session state
    if "db" not in st.session_state:
        st.session_state.setdefault("db", DBManager())


def app() -> None:
    # Initialize the session state with empty list for
    # the types of data that will be used in the application.
    st.set_page_config(layout="wide")
    init_session_state()

    # Set the page layout for the Streamlit application.
    pages = pages_config.pages_config()
    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    app()
