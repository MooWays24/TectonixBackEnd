import pytest
from unittest.mock import patch, MagicMock
from app import app  # Replace 'app' with the name of your Flask app module

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.MCRcon")
def test_shutdown(mock_mcrcon, client):
    """Test the /rcon/shutdown route."""
    mock_instance = MagicMock()
    mock_instance.command.return_value = "Server shutting down in 60 seconds"
    mock_mcrcon.return_value.__enter__.return_value = mock_instance

    response = client.post(
        "/rcon/shutdown",
        json={"seconds": 60, "message": "Server restarting soon"},
    )

    assert response.status_code == 200
    assert response.json["response"] == "Server shutting down in 60 seconds"
    mock_instance.command.assert_called_with("/Shutdown 60 Server_restarting_soon")

@patch("app.MCRcon")
def test_broadcast_message(mock_mcrcon, client):
    """Test the /rcon/broadcast route."""
    mock_instance = MagicMock()
    mock_instance.command.return_value = "Broadcast sent"
    mock_mcrcon.return_value.__enter__.return_value = mock_instance

    response = client.post(
        "/rcon/broadcast",
        json={"message": "Welcome to the server!"},
    )

    assert response.status_code == 200
    assert response.json["response"] == "Broadcast sent"
    mock_instance.command.assert_called_with("/Broadcast Welcome_to_the_server!")

@patch("app.MCRcon")
def test_kick_player(mock_mcrcon, client):
    """Test the /rcon/kick route."""
    mock_instance = MagicMock()
    mock_instance.command.return_value = "Player kicked"
    mock_mcrcon.return_value.__enter__.return_value = mock_instance

    response = client.post(
        "/rcon/kick",
        json={"steam_id": "1234567890"},
    )

    assert response.status_code == 200
    assert response.json["response"] == "Player kicked"
    mock_instance.command.assert_called_with("/KickPlayer 1234567890")

@patch("app.MCRcon")
def test_show_players(mock_mcrcon, client):
    """Test the /rcon/show_players route."""
    mock_instance = MagicMock()
    mock_instance.command.return_value = "Player list: Player1, Player2"
    mock_mcrcon.return_value.__enter__.return_value = mock_instance

    response = client.get("/rcon/show_players")

    assert response.status_code == 200
    assert response.json["response"] == "Player list: Player1, Player2"
    mock_instance.command.assert_called_with("/ShowPlayers")

@patch("app.MCRcon")
def test_server_info(mock_mcrcon, client):
    """Test the /rcon/info route."""
    mock_instance = MagicMock()
    mock_instance.command.return_value = "Server info: Online, 10 players"
    mock_mcrcon.return_value.__enter__.return_value = mock_instance

    response = client.get("/rcon/info")

    assert response.status_code == 200
    assert response.json["response"] == "Server info: Online, 10 players"
    mock_instance.command.assert_called_with("/Info")
