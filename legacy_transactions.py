from bitcoinrpc.authproxy import AuthServiceProxy
import json

rpc_user = "user"
rpc_password = "password"
rpc_port = 18443
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}")

wallet_name = "legacy_wallet"

loaded_wallets = rpc_connection.listwallets()
if wallet_name in loaded_wallets:
    print(f"Wallet '{wallet_name}' already loaded.")
else:
    wallet_dir_info = rpc_connection.listwalletdir()
    existing_wallets = [w["name"] for w in wallet_dir_info.get("wallets", [])]
    if wallet_name not in existing_wallets:
        print(f"Wallet '{wallet_name}' not found. Creating wallet...")
        rpc_connection.createwallet(wallet_name)
    wallet_info = rpc_connection.loadwallet(wallet_name)

rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}/wallet/{wallet_name}")

addr_A = rpc_connection.getnewaddress("", "legacy")
addr_B = rpc_connection.getnewaddress("", "legacy")
addr_C = rpc_connection.getnewaddress("", "legacy")
print(f"Address A: {addr_A}, Address B: {addr_B}, Address C: {addr_C}")

rpc_connection.generatetoaddress(101, addr_A)

fund_txid = rpc_connection.sendtoaddress(addr_A, 10)
print(f"Fund TxID: {fund_txid}")
rpc_connection.generatetoaddress(1, addr_A)

utxos = rpc_connection.listunspent()
input_utxo = utxos[0]
print("UTXO for A:", input_utxo)

from decimal import Decimal

fee = Decimal("0.0002")
input_value = input_utxo['amount']
send_amount = input_value - fee

inputs = [{"txid": input_utxo['txid'], "vout": input_utxo['vout']}]
outputs = {addr_B: send_amount}
raw_tx = rpc_connection.createrawtransaction(inputs, outputs)
signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
final_txid = rpc_connection.sendrawtransaction(signed_tx['hex'])
print(f"Transaction A -> B TxID: {final_txid}")
rpc_connection.generatetoaddress(1, addr_A)

# Decode and analyze
decoded_tx = rpc_connection.decoderawtransaction(signed_tx['hex'])
print("Decoded Transaction A -> B:")
print(json.dumps(decoded_tx, indent=4, default=str))



utxos = rpc_connection.listunspent()
input_utxo_B = next(utxo for utxo in utxos if utxo['address'] == addr_B)
print("UTXO for B:", input_utxo_B)


fee_BC = Decimal("0.0002")
input_B_value = input_utxo_B['amount']
send_amount_BC = input_B_value - fee_BC

inputs_BC = [{"txid": input_utxo_B['txid'], "vout": input_utxo_B['vout']}]
outputs_BC = {addr_C: send_amount_BC}
raw_tx_BC = rpc_connection.createrawtransaction(inputs_BC, outputs_BC)
signed_tx_BC = rpc_connection.signrawtransactionwithwallet(raw_tx_BC)
final_txid_BC = rpc_connection.sendrawtransaction(signed_tx_BC['hex'])
print(f"Transaction B -> C TxID: {final_txid_BC}")
rpc_connection.generatetoaddress(1, addr_A)

# Decode and analyze
decoded_tx_BC = rpc_connection.decoderawtransaction(signed_tx_BC['hex'])
print("Decoded Transaction B -> C:")
print(json.dumps(decoded_tx_BC, indent=4, default=str))
