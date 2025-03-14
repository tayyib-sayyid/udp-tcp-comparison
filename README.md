```markdown
# TCP vs UDP Performance Comparison

This project compares the performance of TCP and UDP in terms of **latency**, **throughput**, and **packet loss** by sending messages of approximately **1400 bytes** between a client and server. The experiment measures **Round-Trip Time (RTT)** and **data transmission efficiency** for both protocols.

---

## 📌 How to Run the Programs

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/tayyib-sayyid/udp-tcp-comparison.git
cd udp-tcp-comparison
```

### 2️⃣ **Run the TCP Server**
Open a terminal and start the TCP server:
```bash
python3 tcp-server.py > tcp_server.log 2>&1 &
```
This runs the TCP server in the background and logs the output to `tcp_server.log`.

### 3️⃣ **Run the TCP Client**
Open a new terminal and start the TCP client:
```bash
python3 tcp-client.py > tcp_client.log 2>&1
```
This sends **1000 messages** of **1400 bytes** each and logs the results to `tcp_client.log`.

---

### 4️⃣ **Run the UDP Server**
Start the UDP server in a terminal:
```bash
python3 udp-server.py > udp_server.log 2>&1 &
```
This runs the UDP server in the background and logs its output.

### 5️⃣ **Run the UDP Client**
Open another terminal and start the UDP client:
```bash
python3 udp-client.py > udp_client.log 2>&1
```
This sends **1000 messages** of **1400 bytes** each via UDP and logs results to `udp_client.log`.

---

## 📌 Expected Outputs

After running the TCP and UDP programs, check the log files for results:
```bash
cat tcp_client.log
cat udp_client.log
```

Each log should contain:
- **Sent messages count**  
- **Received message count (UDP might have losses)**  
- **RTT (Round-Trip Time) for each message**  
- **Average latency**  
- **Throughput (bytes per second)**  

### Example Output (TCP):
```
Message 1: Sent 1400 bytes, Received 1400 bytes, RTT: 0.003456 sec
...
TCP Test Summary:
Average RTT: 0.004123 sec
Throughput: 512000.24 bytes/sec
```

### Example Output (UDP):
```
Message 1: Sent 1400 bytes, Received 1400 bytes, RTT: 0.002921 sec
Message 5: Sent 1400 bytes, No response (packet lost)
...
UDP Test Summary:
Average RTT: 0.002876 sec
Packet Loss Rate: 5.40%
Throughput: 680200.12 bytes/sec
```

---

## 📌 Observations & Comparison: TCP vs UDP

| Feature         | TCP | UDP |
|----------------|-----|-----|
| **Connection Type** | Connection-oriented | Connectionless |
| **Reliability** | Guaranteed (ACKs, retransmission) | No guarantees, packet loss may occur |
| **Speed** | Generally slower due to acknowledgments | Faster as there is no connection setup |
| **Latency (RTT)** | Slightly higher due to extra overhead | Lower, but can be affected by packet loss |
| **Throughput** | Lower due to reliability mechanisms | Higher since there is no overhead of acknowledgments |
| **Packet Loss** | None, unless network fails | Can happen due to congestion or server not responding |

### Key Findings:
1. **TCP has a higher RTT** because it requires acknowledgments and ensures ordered, reliable delivery.
2. **UDP has a lower RTT** and **higher throughput**, but some messages may be lost due to lack of retransmission.
3. **For small messages**, TCP and UDP performance differences are minimal. However, **for larger messages (1400 bytes)**, UDP is significantly faster in terms of throughput.
4. **Packet loss in UDP** depends on network conditions. If no packet loss simulation is added, UDP appears much faster.

---

## 📌 How This Was Accomplished

This project was implemented using **Python’s socket library** to create TCP and UDP client-server models. The understanding of networking concepts was strengthened using references from:

- [Beej’s Guide to Network Programming](https://beej.us/guide/bgnet/)  
- [Computer Networking: A Top-Down Approach - Kurose & Ross](https://www.pearson.com/en-us/subject-catalog/p/computer-networking-a-top-down-approach/P200000003043/9780136681557)  
- Official Python Documentation for `socket` ([link](https://docs.python.org/3/library/socket.html))  

By implementing both protocols and analyzing their performance, this project provides a hands-on approach to understanding the fundamental differences between **reliable** and **unreliable** data transmission in computer networks.

---

## 📌 Future Enhancements

- Simulate **real-world network conditions** using **network delays and congestion**.
- Implement **multi-threaded servers** to handle multiple clients.
- Optimize UDP by implementing **custom reliability mechanisms** at the application layer.

---

💻 **Developed by:** Tayyib Bin Hisham Sayyid  
📅 **Date:** March 14, 2025  
🔗 **GitHub Repository:** [udp-tcp-comparison](https://github.com/tayyib-sayyid/udp-tcp-comparison)
```
