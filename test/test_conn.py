import sys
import os

from src.db_conn import DBEngine
from unittest.mock import patch, MagicMock

# Add the path to the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@patch('connection.psycopg2.connect')
def test_db_engine_init(mock_connect):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    db_engine = DBEngine()

    mock_connect.assert_called_once_with(
        dbname=os.getenv('DATABASE_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    assert db_engine.connection == mock_connection
    assert db_engine.cursor == mock_cursor


@patch('connection.psycopg2.connect')
def test_db_engine_del(mock_connect):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    db_engine = DBEngine()

    del db_engine

    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()
