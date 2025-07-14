import os
import streamlit as st
import statsmodels.api as sm
from tinydb import TinyDB
from tinydb.table import Document, Table
from lightbulb.database.struct_base import BaseData, BaseModel
from lightbulb.database.struct_ols_model import OLSModel
from lightbulb.database.struct_train_data import TrainData
from lightbulb.database.struct_test_data import TestData
from lightbulb.database.struct_forecast_data import ForecastsData
from lightbulb.database.struct_prediction_data import PredictionData


class DBManager:
    def __init__(self, db_path: str = "./db/tinydb.json") -> None:
        self._db_path = db_path

        if not os.path.exists(os.path.dirname(self._db_path)):
            os.makedirs(os.path.dirname(self._db_path))

        # Initialize the database
        self.db: TinyDB = TinyDB(self._db_path)
        # Create the tables if they don't exist
        self.db_models: Table = self.db.table("db_models")
        self.db_train: Table = self.db.table("db_train")
        self.db_test: Table = self.db.table("db_test")
        self.db_forecast: Table = self.db.table("db_forecast")
        self.db_prediction: Table = self.db.table("db_prediction")

        # Load the database contents into the session state
        self._load_db()

    def _load_db(self) -> None:
        """
        Private method that loads all the contents of the database
        in the st.session_state
        """

        # Load the models
        # This implies that the model will be loaded in the model attribute
        _models = [
            OLSModel(**doc)
            for doc in self.db_models.all()
            if isinstance(doc, Document) and doc["type"] == "OLS"
        ]

        # For each model, load the .pkl file if it exists
        for _m in _models:
            model_path = os.path.join(os.path.dirname(self._db_path), f"{_m.id}.pkl")
            if os.path.exists(model_path):
                _m.model = sm.load(model_path)

        st.session_state.model = _models

        # Load train data
        st.session_state.train_data = [
            TrainData(**doc) for doc in self.db_train.all() if isinstance(doc, Document)
        ]
        # Load test data
        st.session_state.test_data = [
            TestData(**doc) for doc in self.db_test.all() if isinstance(doc, Document)
        ]
        # Load forecast data
        st.session_state.forecast_data = [
            ForecastsData(**doc)
            for doc in self.db_forecast.all()
            if isinstance(doc, Document)
        ]
        # Load prediction data
        st.session_state.prediction_data = [
            PredictionData(**doc)
            for doc in self.db_prediction.all()
            if isinstance(doc, Document)
        ]

    def insert(self, obj: BaseModel | BaseData) -> None:
        """
        Public method to save data or model objects into db.

        Parameters
        ----------
        data : BaseModel | BaseData
            The object to be saved in the db
        """
        if isinstance(obj, BaseModel):
            self.db_models.insert(Document(obj.as_dict(), doc_id=obj.id))
            # For reliability the model result that is stored in the model attribute
            # will be saved as a .pkl file in the same directory as the database
            if obj.model is not None:
                model_path = os.path.join(
                    os.path.dirname(self._db_path), f"{obj.id}.pkl"
                )
                obj.model.save(model_path)

        elif isinstance(obj, TrainData):
            self.db_train.insert(Document(obj.as_dict(), doc_id=obj.id))

        elif isinstance(obj, TestData):
            self.db_test.insert(Document(obj.as_dict(), doc_id=obj.id))

        elif isinstance(obj, ForecastsData):
            self.db_forecast.insert(Document(obj.as_dict(), doc_id=obj.id))

        elif isinstance(obj, PredictionData):
            self.db_prediction.insert(Document(obj.as_dict(), doc_id=obj.id))

    def delete(self, obj: BaseModel | BaseData) -> None:
        """
        Public method to delete data or model object from the db.

        Parameters
        ----------
        obj : BaseModel | BaseData
            The object to be saved in the db
        """
        if isinstance(obj, BaseModel):
            self.db_models.remove(doc_ids=[obj.id])

        elif isinstance(obj, TrainData):
            self.db_train.remove(doc_ids=[obj.id])

        elif isinstance(obj, TestData):
            self.db_test.remove(doc_ids=[obj.id])

        elif isinstance(obj, ForecastsData):
            self.db_forecast.remove(doc_ids=[obj.id])

        elif isinstance(obj, PredictionData):
            self.db_prediction.remove(doc_ids=[obj.id])
