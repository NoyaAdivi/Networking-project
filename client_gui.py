import socket
import threading
import queue
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 12345


class ChatClientGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("TCP Chat Client")

        self.sock = None
        self.running = False
        self.inbox = queue.Queue()

        # --- Top: connection
        top = tk.Frame(root)
        top.pack(fill="x", padx=10, pady=8)

        tk.Label(top, text="Name:").pack(side="left")
        self.name_var = tk.StringVar(value="Yonatan")
        tk.Entry(top, textvariable=self.name_var, width=18).pack(side="left", padx=6)

        tk.Label(top, text="Host:").pack(side="left")
        self.host_var = tk.StringVar(value=HOST)
        tk.Entry(top, textvariable=self.host_var, width=15).pack(side="left", padx=6)

        tk.Label(top, text="Port:").pack(side="left")
        self.port_var = tk.StringVar(value=str(PORT))
        tk.Entry(top, textvariable=self.port_var, width=8).pack(side="left", padx=6)

        self.connect_btn = tk.Button(top, text="Connect", command=self.connect)
        self.connect_btn.pack(side="left", padx=6)

        self.disconnect_btn = tk.Button(top, text="Disconnect", command=self.disconnect, state="disabled")
        self.disconnect_btn.pack(side="left")

        # --- Middle: chat log
        mid = tk.Frame(root)
        mid.pack(fill="both", expand=True, padx=10)

        self.text = tk.Text(mid, height=18, wrap="word", state="disabled")
        self.text.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(mid, command=self.text.yview)
        scroll.pack(side="right", fill="y")
        self.text.config(yscrollcommand=scroll.set)

        # --- Bottom: message entry
        bottom = tk.Frame(root)
        bottom.pack(fill="x", padx=10, pady=8)

        self.msg_var = tk.StringVar()
        self.entry = tk.Entry(bottom, textvariable=self.msg_var)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda _e: self.send_message())

        self.send_btn = tk.Button(bottom, text="Send", command=self.send_message, state="disabled")
        self.send_btn.pack(side="left", padx=6)

        hint = tk.Label(root, text="Tips: /users | /dm <name> <msg> | /all <msg> (or just type to broadcast)")
        hint.pack(padx=10, pady=(0, 8))

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.after(100, self.process_inbox)

    def log(self, line: str):
        self.text.config(state="normal")
        self.text.insert("end", line + "\n")
        self.text.see("end")
        self.text.config(state="disabled")

    def connect(self):
        if self.running:
            return

        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Error", "Name is required.")
            return

        host = self.host_var.get().strip()
        try:
            port = int(self.port_var.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Port must be a number.")
            return

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            # Short timeout so idle doesn't disconnect; we ignore timeouts
            self.sock.settimeout(1.0)
        except Exception as e:
            messagebox.showerror("Connection failed", str(e))
            self.sock = None
            return

        self.running = True
        self.connect_btn.config(state="disabled")
        self.disconnect_btn.config(state="normal")
        self.send_btn.config(state="normal")

        # Receive server welcome (optional, may timeout)
        self._recv_into_log_once()

        # Send HELLO
        self._send_line(f"HELLO {name}")

        threading.Thread(target=self.receiver_loop, daemon=True).start()
        self.log(f"[connected to {host}:{port} as {name}]")

    def disconnect(self):
        if not self.running:
            return
        self.running = False
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
        self.sock = None

        self.connect_btn.config(state="normal")
        self.disconnect_btn.config(state="disabled")
        self.send_btn.config(state="disabled")
        self.log("[disconnected]")

    def send_message(self):
        if not self.running or not self.sock:
            return
        msg = self.msg_var.get().strip()
        if not msg:
            return
        self.msg_var.set("")
        self._send_line(msg)
        self.log(f"ME: {msg}")

    def receiver_loop(self):
        while self.running and self.sock:
            line = self._recv_line()
            if line is None:
                self.inbox.put("SYS Connection closed by server.")
                break
            if line == "":
                continue  # timeout -> no data yet, keep listening
            self.inbox.put(line)

        self.root.after(0, self.disconnect)

    def process_inbox(self):
        try:
            while True:
                line = self.inbox.get_nowait()
                self.log(line)
        except queue.Empty:
            pass
        self.root.after(100, self.process_inbox)

    def _send_line(self, text: str):
        try:
            self.sock.sendall((text + "\n").encode("utf-8"))
        except Exception:
            self.inbox.put("SYS Failed to send (connection issue).")

    def _recv_line(self):
        """
        Returns:
        - str line (without '\n')
        - "" on timeout (no data yet)
        - None on disconnect/error
        """
        data = b""
        try:
            while True:
                bch = self.sock.recv(1)
                if not bch:
                    return None
                if bch == b"\n":
                    return data.decode("utf-8", errors="replace")
                data += bch
                if len(data) > 8192:
                    return None
        except socket.timeout:
            return ""
        except Exception:
            return None

    def _recv_into_log_once(self):
        line = self._recv_line()
        if line and line != "":
            self.log(line)

    def on_close(self):
        self.disconnect()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClientGUI(root)
    root.mainloop()
