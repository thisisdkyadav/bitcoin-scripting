# Bitcoin Transactions - Legacy and SegWit

## Team Members

- Devesh Kumar - 230001024
- Harshith Jai Surya Ganji - 230041010
- Aarav Gupta - 230008001

## How to Run the Program

### Prerequisites:

- Bitcoin Core installed
- Python installed
- `python-bitcoinrpc` package installed
  ```bash
  pip install python-bitcoinrpc
  ```

### Bitcoin Core Configuration:

Create or update `bitcoin.conf` file in your Bitcoin data directory (commonly located at `~/.bitcoin` or specified directory in regtest):

```
regtest=1
server=1
rpcuser=user
rpcpassword=password
rpcallowip=127.0.0.1
rpcport=18443
fallbackfee=0.0002
mintxfee=0.00001
paytxfee=0.0001
txconfirmtarget=1
maxtxfee=0.01
```

Start `bitcoind` in regtest mode:

```bash
bitcoind -regtest
```

### Running the Programs:

1. **Part 1: Legacy Transactions**

Run the following command:

```bash
python legacy_transactions.py
```

This script:

- Creates a legacy wallet.
- Generates addresses A, B, C (P2PKH format).
- Funds Address A.
- Sends transactions: A ➔ B ➔ C.
- Displays transaction details and decodes transactions.

2. **Part 2: SegWit Transactions**

Run the following command:

```bash
python segwit_transactions.py
```

This script:

- Creates a SegWit wallet.
- Generates addresses A', B', C' (P2SH-P2WPKH format).
- Funds Address A'.
- Sends transactions: A' ➔ B' ➔ C'.
- Displays transaction details and decodes transactions.

---

## Notes:

- Each transaction fee: **0.0002 BTC**
- Blocks are generated after each transaction to confirm them.
- Make sure `bitcoind` is running before executing the scripts.
