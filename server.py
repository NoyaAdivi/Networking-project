import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

# clients[name] = (conn, addr)
clients = {}
clients_lock = threading.Lock()


def send_line(conn: socket.socket, text: str) -> None:
    try:
        conn.sendall((text + "\n").encode("utf-8"))
    except Exception:
        pass


def broadcast(sender: str, msg: str) -> None:
    with clients_lock:
        items = list(clients.items())
    for name, (c, _a) in items:
        if name != sender:
            send_line(c, f"FROM {sender}: {msg}")


def send_private(sender: str, target: str, msg: str) -> None:
    with clients_lock:
        target_entry = clients.get(target)
        sender_entry = clients.get(sender)

    if not target_entry:
        if sender_entry:
            send_line(sender_entry[0], f"SYS User '{target}' is not connected.")
        return

    send_line(target_entry[0], f"DM {sender}: {msg}")


def list_users(conn: socket.socket) -> None:
    with clients_lock:
        names = sorted(clients.keys())
    send_line(conn, "SYS Users: " + (", ".join(names) if names else "(none)"))


def remove_client(name: str) -> None:
    with clients_lock:
        entry = clients.pop(name, None)
    if entry:
        conn, _addr = entry
        try:
            conn.close()
        except Exception:
            pass


def recv_line(conn: socket.socket):
    """
    Reads until '\n'. Returns:
    - str line (without '\n')
    - "" on timeout (no data yet, keep connection)
    - None on disconnect/error
    """
    data = b""
    try:
        while True:
            chunk = conn.recv(1)
            if not chunk:
                return None
            if chunk == b"\n":
                return data.decode("utf-8", errors="replace")
            data += chunk
            if len(data) > 8192:
                return None
    except socket.timeout:
        return ""
    except (ConnectionResetError, OSError):
        return None


def handle_client(conn: socket.socket, addr):
    # Short timeout so "silence" doesn't kill the connection
    conn.settimeout(1.0)

    name = None
    try:
        send_line(conn, "SYS Welcome. Please identify: HELLO <your_name>")

        # Handshake: wait for HELLO, ignoring timeouts
        while True:
            first = recv_line(conn)
            if first is None:
                return
            if first == "":
                continue
            first = first.strip()
            if first:
                break

        if not first.startswith("HELLO "):
            send_line(conn, "SYS Expected: HELLO <your_name>. Closing.")
            return

        name = first[6:].strip()
        if not name:
            send_line(conn, "SYS Name cannot be empty. Closing.")
            return

        with clients_lock:
            if name in clients:
                send_line(conn, "SYS Name already in use. Choose another. Closing.")
                return
            clients[name] = (conn, addr)

        send_line(conn, f"SYS Hello {name}. Commands: /users, /dm <name> <msg>, /all <msg>")
        broadcast("SERVER", f"{name} joined the chat.")

        # Main loop
        while True:
            line = recv_line(conn)
            if line is None:
                break           # real disconnect
            if line == "":
                continue        # just a timeout (no data yet)

            line = line.strip()
            if not line:
                continue

            if line == "/users":
                list_users(conn)
                continue

            if line.startswith("/dm "):
                parts = line.split(" ", 2)
                if len(parts) < 3:
                    send_line(conn, "SYS Usage: /dm <name> <message>")
                    continue
                target, msg = parts[1], parts[2]
                send_private(name, target, msg)
                continue

            if line.startswith("/all "):
                msg = line[5:].strip()
                if msg:
                    broadcast(name, msg)
                continue

            # default: broadcast
            broadcast(name, line)

    except Exception:
        pass
    finally:
        if name:
            remove_client(name)
            broadcast("SERVER", f"{name} left the chat.")
        try:
            conn.close()
        except Exception:
            pass


def main():
    print(f"Server starting on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(50)
        print("Server listening...")

        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()


if __name__ == "__main__":
    main()
