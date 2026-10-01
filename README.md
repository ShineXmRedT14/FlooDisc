# Floodisc

Floodisc is a command-line tool designed for network packet and HTTP GET method performance and rate-limit testing.

---

## How to install CLi

Just do this:

Windows: run create.bat
Linux: run create.sh

After you can easily use this tool

## Usage & Flags

### Core Flags

| Flag | Alias | Description | Syntax |
| :--- | :--- | :--- | :--- |
| `-h` | `--help` | Show help message and exit. | `floodisc -h` |
| `-type` | `--type` | Layer 4 protocol type: `1` (TCP), `2` (UDP), `3` (ICMP). | `floodisc -type 1` |
| `-http` | `--http` | Enable HTTP GET testing mode. | `floodisc -http` |

### HTTP GET Testing Options (Requires `-http`)

| Option | Alias | Description | Syntax |
| :--- | :--- | :--- | :--- |
| `-u` | `--url` | Target URL for HTTP testing. | `floodisc -http -u https://example.com` |
| `-time` | `--timeout` | HTTP request timeout in seconds. | `floodisc -http -time 1` |
| `-allow` | `--allow` | Enable automatic HTTP redirects (`allow_redirects=True`). | `floodisc -http -allow` |
| `-t` | `--tasks` | Maximum number of concurrent parallel tasks. | `floodisc -http -t 20` |

### Packet Testing Options (Requires `-type`)

| Option | Alias | Description | Syntax |
| :--- | :--- | :--- | :--- |
| `-src` | `--source` | Source IP address. | `floodisc -type 1 -src 192.168.0.1` |
| `-dst` | `--destination` | Destination IP address. | `floodisc -type 1 -dst 192.168.0.2` |
| `-args` | `--args` | Protocol-specific parameters (see syntax below). | `floodisc -type 1 -args ...` |

---

## `-args` Flag Syntax

When using the raw packet testing method, specific parameters for headers must be passed inside the `-args` string using operators.

**Note:** Inside the `-args` string, parameters **do not use** the `--` prefix, preventing terminal parsing conflicts.

* `;` — **AND operator** (parameter separator)
* `*` — **Assignment operator** (key-value separator)

### Supported Parameters by Protocol

| TCP (`-type 1`) | UDP (`-type 2`) | ICMP (`-type 3`) |
| :--- | :--- | :--- |
| `sport` (Source Port) | `sport` (Source Port) | `type` (ICMP Type) |
| `dport` (Destination Port) | `dport` (Destination Port) | `code` (ICMP Code) |
| `flags` (TCP Flags, e.g., `S`, `A`) | *Not supported* | *Not supported* |

### Syntax Examples for `-args`
* **TCP:** `sport*80;dport*443;flags*A`
* **UDP:** `sport*80;dport*443`
* **ICMP:** `type*1;code*1`

---

## Quick Examples

### 1. Raw Packet Method (TCP Flood)
Sends TCP packets from source to destination with custom ports and flags.

```bash
floodisc -type 1 -src 192.168.0.100 -dst 192.168.0.1 -args sport*34566;dport*80;flags*S
```

### 2. HTTP GET Performance Method
Tests an HTTP server with 100 parallel tasks, a 1-second timeout, and allowed redirects:
```bash
floodisc -http -u https://example.com -allow -time 1 -t 100
```

---

## Test Results

All benchmarks and scan logs are automatically saved to the following directory:
📁 `floodisc/src/info/`

Results are generated as **`.json`** files containing:
* Target server rate limits and response statistics.
* Configuration and flags used during the specific test session.

---

## Disclaimer (Denial of Responsibility)

**IMPORTANT: This tool is intended for educational purposes, authorized security research, and infrastructure stress-testing ONLY.**

The author(s) of Floodisc accept **NO responsibility** and assume **NO liability** for any misuse, damage, server downtime, or illegal activity caused by this program. By using this software, you agree that:
* You will only test systems that you own or have explicit, written permission to test.
* You are solely responsible for complying with your local laws and regulations regarding cyber security and network testing.
* The software is provided "as is", without any warranties of any kind.

---

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute.
