import os
from tinydb import TinyDB
from tinydb.table import Document, Table
import streamlit as st
from moonlight.database.struct_base import BaseData, BaseModel
from moonlight.database.struct_ols_model import OLSModel
from moonlight.database.struct_train_data import TrainData
from moonlight.database.struct_test_data import TestData
from moonlight.database.struct_forecast_data import ForecastsData
from moonlight.database.struct_prediction_data import PredictionData


def init_db(db_path: str = "./db/tinydb.json") -> None:
    # See if the db_paht exists, if not create it
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    # Initialize the database
    db: TinyDB = TinyDB(db_path)
    # Create the tables if they don't exist
    db_models: Table = db.table("db_models")
    db_train: Table = db.table("db_train")
    db_test: Table = db.table("db_test")
    db_forecast: Table = db.table("db_forecast")
    db_prediction: Table = db.table("db_prediction")

    # Store the database in the session state
    if not isinstance(st.session_state.db, db.__class__):
        st.session_state.db = db
    if not isinstance(st.session_state.db_models, db_models.__class__):
        st.session_state.db_models = db_models
    if not isinstance(st.session_state.db_train, db_train.__class__):
        st.session_state.db_train = db_train
    if not isinstance(st.session_state.db_test, db_test.__class__):
        st.session_state.db_test = db_test
    if not isinstance(st.session_state.db_forecast, db_forecast.__class__):
        st.session_state.db_forecast = db_forecast
    if not isinstance(st.session_state.db_prediction, db_prediction.__class__):
        st.session_state.db_prediction = db_prediction


def load_db(db_path: str = "./db/tinydb.json") -> None:
    """
    Load the objects from the database into the session state.
    If the database does not exist, it raises an error.
    """
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file {db_path} does not exist.")
    db_models = st.session_state.db_models
    db_train = st.session_state.db_train
    db_test = st.session_state.db_test
    db_forecast = st.session_state.db_forecast
    db_prediction = st.session_state.db_prediction

    # Load models and fit them if needed
    _models = [
        OLSModel(**doc)
        for doc in db_models.all()
        if isinstance(doc, Document) and doc["type"] == "OLS"
    ]

    _models = [
        model.train(TrainData(**db_train.get(model.ref_train[0])))
        for model in _models
        if isinstance(model, OLSModel)
    ]
    st.session_state.model = _models

    # Load train data
    st.session_state.train_data = [
        TrainData(**doc) for doc in db_train.all() if isinstance(doc, Document)
    ]
    # Load test data
    st.session_state.test_data = [
        TestData(**doc) for doc in db_test.all() if isinstance(doc, Document)
    ]
    # Load forecast data
    st.session_state.forecast_data = [
        ForecastsData(**doc) for doc in db_forecast.all() if isinstance(doc, Document)
    ]
    # Load prediction data
    st.session_state.prediction_data = [
        PredictionData(**doc)
        for doc in db_prediction.all()
        if isinstance(doc, Document)
    ]


def save_model(model: BaseModel) -> None:
    # Save the model __dict__ to the database
    if not hasattr(st.session_state, "db"):
        raise ValueError("Database is not initialized. Call init_db() first.")

    db_models = st.session_state.db_models
    db_models.insert(Document(model.as_dict(), doc_id=model.id))
