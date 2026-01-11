# TCP Chat Project – Computer Networks

## Description
This project implements a TCP-based Client–Server chat system that demonstrates real network traffic creation, asynchronous communication, and traffic analysis using Wireshark.  
The system includes a central server and multiple GUI-based clients.

## Features
- Client–Server architecture over TCP
- Multiple concurrent clients
- Asynchronous handling using threads
- Graphical User Interface (GUI) for clients
- Private messaging between users
- List of connected users
- Network traffic capture and analysis with Wireshark

## Project Structure
```
.
├── server.py        # TCP server – manages connections and routes messages
├── client_gui.py    # GUI-based TCP client
├── README.md        # Project documentation
```

> Note: The system operates fully in-memory. No database is used or required.

## Requirements
- Python 3
- No external Python libraries required
- Wireshark (for traffic analysis)

## How to Run

### Start the Server
```bash
python3 server.py
```
The server listens on TCP port 12345.

### Start Clients
Run each client in a separate terminal:
```bash
python3 client_gui.py
```

In the GUI:
- Enter a unique username
- Host: 127.0.0.1
- Port: 12345
- Click **Connect**

## Client Commands
- `/users` – Show connected users
- `/dm <username> <message>` – Send a private message
- Free text – Broadcast message to all users

## Asynchronous Design
- Server: Each client is handled in a separate thread.
- Client: Message receiving runs in a background thread, keeping the GUI responsive.

## Wireshark Traffic Analysis
When running locally, capture traffic on the **Loopback** interface.

Recommended filters:
```
tcp.port == 12345
```
or
```
ip.addr == 127.0.0.1 && tcp.port == 12345
```

Visible in Wireshark:
- TCP three-way handshake
- TCP packets carrying chat messages (payload)
- Sequence numbers and ACKs
- Graceful connection termination

## Use of AI Tools
AI tools were used only as supportive aids for learning, architectural planning, code examples, and documentation refinement.  
All code was reviewed, understood, and adapted by the project authors.

## Summary
This project demonstrates a complete TCP-based chat system, combining networking theory with practical implementation, asynchronous programming, GUI design, and real network traffic analysis.
