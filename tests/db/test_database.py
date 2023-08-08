from unittest.mock import patch

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.db.base import create_db_engine


def test_create_db_engine_success():
    with patch("time.sleep"):
        with patch("builtins.print") as mock_print:
            with patch("sqalchemy.create_engine") as mock_create_engine:
                mock_create_engine.return_value = "mock_engine"
                result = create_db_engine()
                assert mock_create_engine.call_count == 1
                assert mock_print.call_count == 1
                assert result == "mock_engine"


def test_create_engine_error():
    with patch("time.sleep"):
        with patch("builtins.print") as mock_print:
            with patch("sqlalchemy.create_engine") as mock_create_engine:
                mock_create_engine.side_effect = SQLAlchemyError()
                result = create_db_engine()
                assert mock_create_engine.call_count == 5
                assert mock_print.call_count == 5
                assert result is None
