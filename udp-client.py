import socket
import time
#import os
#UDP IS NOW FASTER THAN TCP FOLLOWING THE CHANGES DESCRIBED IN COMMENTS
#Im the GOAT

def main():
    HOST = '127.0.0.1'  
    PORT = 12346        

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)  #1-sec timeout

    num_msg = 1000
    latencies = []
    tbs = 0
    lpackets = 0 # lost

    for i in range(1, num_msg + 1):
        payload = ("X" * 1400).encode() #same change as in tcp-client
        start = time.time()
        client_socket.sendto(payload, (HOST, PORT))
        tbs += len(payload)
        try: #added error handling
            data, addr = client_socket.recvfrom(2048) #increased buffer size bcs of incr msgs
            end = time.time()
            rtt = end - start
            latencies.append(rtt)
            print(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec") #not printing full payload (so as not to clutter the logfile)
        except socket.timeout:
            lpackets += 1
            print(f"Message {i}: Sent 1400 bytes, No response (packet lost)") #same as above

    client_socket.close()

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        total = sum(latencies)
    else:
        avg_latency = 0
        total_time = 0
    throughput = tbs / total if total > 0 else 0

    print("\nUDP Test Summary:")
    print(f"Average RTT (for received packets): {avg_latency:.6f} sec")
    print(f"Packet Loss Rate: {lpackets / num_msg * 100:.2f}%")
    print(f"Throughput (approx.): {throughput:.2f} bytes/sec")

if __name__ == "__main__":
    main()
