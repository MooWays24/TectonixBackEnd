from flask import Flask, request, jsonify
from mcrcon import MCRcon

app = Flask(__name__)

# RCON server configuration
RCON_HOST = "127.0.0.1"  # Replace with your server's IP
RCON_PORT = 25575        # Replace with your server's RCON port
RCON_PASSWORD = "your_rcon_password"  # Replace with your RCON password

def execute_rcon_command(command):
    """Helper function to execute RCON commands."""
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
        return response
    except Exception as e:
        return str(e)

@app.route("/rcon/shutdown", methods=["POST"])
def shutdown_server():
    """Shut down the server after a specified number of seconds with an optional message."""
    data = request.json
    seconds = data.get("seconds", 0)
    message = data.get("message", "")
    command = f"/Shutdown {seconds} {message.replace(' ', '_')}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/doexit", methods=["POST"])
def force_stop_server():
    """Force stop the server immediately."""
    command = "/DoExit"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/broadcast", methods=["POST"])
def broadcast_message():
    """Send a message to all players on the server."""
    data = request.json
    message = data.get("message", "")
    command = f"/Broadcast {message.replace(' ', '_')}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/kick", methods=["POST"])
def kick_player():
    """Kick a player from the server using their SteamID."""
    data = request.json
    steam_id = data.get("steam_id", "")
    command = f"/KickPlayer {steam_id}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/ban", methods=["POST"])
def ban_player():
    """Ban a player from the server using their SteamID."""
    data = request.json
    steam_id = data.get("steam_id", "")
    command = f"/BanPlayer {steam_id}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/unban", methods=["POST"])
def unban_player():
    """Unban a player from the server using their SteamID."""
    data = request.json
    steam_id = data.get("steam_id", "")
    command = f"/UnBanPlayer {steam_id}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/teleport_to_player", methods=["POST"])
def teleport_to_player():
    """Teleport yourself to the location of another player using their SteamID."""
    data = request.json
    steam_id = data.get("steam_id", "")
    command = f"/TeleportToPlayer {steam_id}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/teleport_to_me", methods=["POST"])
def teleport_player_to_me():
    """Teleport another player to your current location using their SteamID."""
    data = request.json
    steam_id = data.get("steam_id", "")
    command = f"/TeleportToMe {steam_id}"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/show_players", methods=["GET"])
def show_players():
    """Display information on all connected players."""
    command = "/ShowPlayers"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/info", methods=["GET"])
def server_info():
    """Show server information."""
    command = "/Info"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

@app.route("/rcon/save", methods=["POST"])
def save_world():
    """Save the world data."""
    command = "/Save"
    response = execute_rcon_command(command)
    return jsonify({"command": command, "response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
