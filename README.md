
# Thief

Thief is a Python project that leverages the Internet Control Message Protocol (ICMP) to send and receive text data over networks. The project consists of two main files: `sender.py` for sending messages and `receiver.py` for receiving them.

## Introduction to ICMP

ICMP (Internet Control Message Protocol) is a network layer protocol used to send error messages and operational information indicating success or failure when communicating with another IP address. It is commonly used for diagnostic and control purposes in network devices.

### Message Format

ICMP messages consist of a header and a data section. The header contains the following fields:

- **Type:** Specifies the type of ICMP message (e.g., Echo Request, Echo Reply, Destination Unreachable).
- **Code:** Further specifies the type of message.
- **Checksum:** Used for error-checking of the header and data.
- **Rest of Header:** Additional fields depending on the type of ICMP message.

#### ICMP Message Format Diagram

```
+--------+--------+--------------+---------------------------+
|  Type  |  Code  |  Checksum    |       Rest of Header      |
+--------+--------+--------------+---------------------------+
|                         Data (if present)                  |
+------------------------------------------------------------+
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shubham16sky/Thief.git
   ```

2. Install the required dependencies under superuser permission:
   ```sh
   sudo pip install -r requirements.txt
   ```

## Usage

### Sender

The `sender.py` script sends text data over ICMP to a specified destination address. **Note:** Requires superuser permission.

```sh
sudo python3 sender.py [destination_addr] [text]
```

- `destination_addr`: The IP address of the destination.
- `text`: The text message to be sent. Limited to 32 characters.

### Receiver

The `receiver.py` script listens for ICMP packets containing text data and prints the received messages. **Note:** Requires superuser permission.

```sh
sudo python3 receiver.py
```

- **Note:** By default, the receiver listens on the loopback interface (`lo`). You can modify the `interface` parameter in `receiver.py` to listen on a different network interface.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


