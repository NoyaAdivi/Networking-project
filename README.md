<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="docs/readme/banner-en.svg" width="100%" alt="TCP Chat: a multi-client chat with Wireshark analysis"></a>
</p>

<p align="center"><a href="README.he.md"><img src="docs/readme/lang-he.svg" height="44" alt="לגרסה בעברית"></a></p>

<p align="center">
  <a href="Summary_Report.pdf"><img src="https://img.shields.io/badge/Summary_report-FFD5C9?style=for-the-badge&logo=adobeacrobatreader&logoColor=A8483A" alt="Summary report"></a>
  <a href="packets.pcapng"><img src="https://img.shields.io/badge/Wireshark_capture-DAD5FF?style=for-the-badge&logo=wireshark&logoColor=5548C8" alt="Wireshark capture"></a>
  <a href="#run-it"><img src="https://img.shields.io/badge/Run_it-D9F3E7?style=for-the-badge&logo=python&logoColor=1F7350" alt="Run it"></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/NoyaAdivi/Networking-project?color=DAD5FF&labelColor=5548C8" alt="License"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project/commits/main"><img src="https://img.shields.io/github/last-commit/NoyaAdivi/Networking-project?color=FFD5C9&labelColor=A8483A" alt="Last commit"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/github/languages/top/NoyaAdivi/Networking-project?color=D9F3E7&labelColor=1F7350" alt="Top language"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/github/repo-size/NoyaAdivi/Networking-project?color=FBD5E0&labelColor=A03A5C" alt="Repo size"></a>
</p>

<h3 align="center">A real client-server chat, and proof of every byte on the wire.</h3>

<p align="center">
  A TCP server and GUI clients that chat in real time, with private messages and a live user list,<br>plus a <b>Wireshark capture</b> that shows the handshake, the payloads and the goodbye. Computer Networks course project.
</p>

<table align="center">
  <tr>
    <td align="center" width="25%"><a href="#run-it"><b>🔌 TCP</b></a><br><sub>port 12345</sub></td>
    <td align="center" width="25%"><a href="#how-it-works"><b>👥 Multi</b></a><br><sub>clients at once</sub></td>
    <td align="center" width="25%"><a href="#how-it-works"><b>🧵 1</b></a><br><sub>thread per client</sub></td>
    <td align="center" width="25%"><a href="packets.pcapng"><b>🦈 .pcapng</b></a><br><sub>real traffic capture</sub></td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="docs/readme/showcase-en.png" width="100%" alt="TCP Chat: a multi-client chat with Wireshark analysis"></a>
</p>

<a name="highlights"></a>
<p align="center"><a href="server.py"><img src="docs/readme/highlights-en.svg" width="100%" alt="Highlights"></a></p>

<table>
  <tr valign="top">
    <td width="33%"><p><b>💬 A complete chat</b></p><ul><li><b>Broadcast</b> messages to everyone</li><li><b>Private messages</b> with <code>/dm</code></li><li><b>Who's online</b> with <code>/users</code></li></ul></td>
    <td width="33%"><p><b>🧵 Asynchronous by design</b></p><ul><li><b>Server:</b> a separate thread for each client</li><li><b>Client:</b> receiving runs in the background</li><li><b>GUI stays responsive</b> while messages arrive</li></ul></td>
    <td width="33%"><p><b>🦈 Seen on the wire</b></p><ul><li><b>Three-way handshake</b> and graceful close</li><li><b>Sequence numbers and ACKs</b> in a real capture</li><li><b>Annotated notebook</b> of the TCP/IP analysis</li></ul></td>
  </tr>
</table>

<a name="how-it-works"></a>
<p align="center"><a href="Summary_Report.pdf"><img src="docs/readme/how-it-works-en.svg" width="100%" alt="How it works"></a></p>

```mermaid
sequenceDiagram
  participant A as 🧑 Client A
  participant S as 🖥️ Server
  participant B as 👩 Client B
  A->>S: SYN · SYN-ACK · ACK (connect)
  B->>S: SYN · SYN-ACK · ACK (connect)
  A->>S: /users
  S-->>A: Noya, Amit
  A->>S: Hello everyone!
  S-->>B: [A] Hello everyone!
  A->>S: /dm Noya see you at 8
  S-->>B: [private from A] see you at 8
  A->>S: FIN (disconnect)
```

| Command | What it does |
|---|---|
| `/users` | Show connected users |
| `/dm <username> <message>` | Send a private message |
| free text | Send to everyone |

> [!NOTE]
> Everything runs in memory. No database is needed.

<a name="tech-stack"></a>
<p align="center"><a href="https://docs.python.org/3/library/socket.html"><img src="docs/readme/tech-stack-en.svg" width="100%" alt="Tech Stack"></a></p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-CFE6FA?style=for-the-badge&logo=python&logoColor=3F6D9F" alt="Python"></a>
  <a href="https://docs.python.org/3/library/socket.html"><img src="https://img.shields.io/badge/Sockets-DAD5FF?style=for-the-badge&logo=python&logoColor=5548C8" alt="Sockets"></a>
  <a href="https://docs.python.org/3/library/threading.html"><img src="https://img.shields.io/badge/Threading-FBD5E0?style=for-the-badge&logo=python&logoColor=A03A5C" alt="Threading"></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/Tkinter-D9F3E7?style=for-the-badge&logo=python&logoColor=1F7350" alt="Tkinter"></a>
  <a href="https://www.wireshark.org"><img src="https://img.shields.io/badge/Wireshark-FFD5C9?style=for-the-badge&logo=wireshark&logoColor=A8483A" alt="Wireshark"></a>
  <a href="https://jupyter.org"><img src="https://img.shields.io/badge/Jupyter-FFD5C9?style=for-the-badge&logo=jupyter&logoColor=A8483A" alt="Jupyter"></a>
</p>

<a name="run-it"></a>
<p align="center"><a href="client_gui.py"><img src="docs/readme/run-it-en.svg" width="100%" alt="Run it"></a></p>

Requires **Python 3** (no extra packages) and [Wireshark](https://www.wireshark.org) for the analysis.

1. **Start the server** (listens on TCP port 12345):
   ```bash
   python3 server.py
   ```
2. **Start a client** in each extra terminal:
   ```bash
   python3 client_gui.py
   ```
3. In the window: pick a unique username, host `127.0.0.1`, port `12345`, and click **Connect**.

**🦈 Capture it:** on the **Loopback** interface, filter with `tcp.port == 12345` (or `ip.addr == 127.0.0.1 && tcp.port == 12345`).

<details>
<summary><b>📂 Files</b></summary>

| File | What it is |
|---|---|
| [`server.py`](server.py) | TCP server that manages connections and routes messages |
| [`client_gui.py`](client_gui.py) | GUI client |
| [`Summary_Report.pdf`](Summary_Report.pdf) | Full project summary and architecture |
| [`packets.pcapng`](packets.pcapng) | Wireshark capture of the traffic |
| [`group06_ttp_chat_input.csv`](group06_ttp_chat_input.csv) | Chat input data |
| [`raw_tcp_ip_notebook_fallback_annotated-v1.ipynb`](raw_tcp_ip_notebook_fallback_annotated-v1.ipynb) | Annotated TCP/IP analysis notebook |
</details>

<sub>🤖 AI tools were used only to support learning, planning and documentation. All code was reviewed, understood and adapted by the authors.</sub>

<a name="contact"></a>
<p align="center"><a href="https://www.linkedin.com/in/noya-adivi/"><img src="docs/readme/footer-en.svg" width="100%" alt="Built by Noya Adivi"></a></p>

<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/badge/Open_project-FFD5C9?style=for-the-badge&logo=github&logoColor=A8483A" alt="Open project"></a>
  <a href="https://www.linkedin.com/in/noya-adivi/"><img src="https://img.shields.io/badge/LinkedIn-DAD5FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iIzU1NDhDOCIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU2di01LjU3YzAtMS4zMy0uMDMtMy4wNC0xLjg1LTMuMDQtMS44NiAwLTIuMTQgMS40NS0yLjE0IDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjh6TTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTN6TTcuMTIgMjAuNDVIMy41NlY5aDMuNTZ2MTEuNDV6TTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1Yy45OCAwIDEuNzgtLjc3IDEuNzgtMS43M1YxLjczQzI0IC43NyAyMy4yIDAgMjIuMjIgMHoiLz48L3N2Zz4=" alt="LinkedIn"></a>
  <a href="https://noyaadivi.github.io/noya-website"><img src="https://img.shields.io/badge/Portfolio-D9F3E7?style=for-the-badge&logo=githubpages&logoColor=1F7350" alt="Portfolio"></a>
  <a href="https://github.com/NoyaAdivi"><img src="https://img.shields.io/badge/More_projects-FBD5E0?style=for-the-badge&logo=github&logoColor=A03A5C" alt="More projects"></a>
</p>
