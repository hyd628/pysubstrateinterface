from substrateinterface import SubstrateInterface

# Define the Ethereum TxHash to Check Finality
wallet = '0x8c3efb060ab1f725145f03bCEe8bF300baD41817'

# Point API Provider to Moonriver Network
moonbeamAPIProvider = SubstrateInterface(
    url="wss://wss.moonriver.moonbeam.network",
)

if __name__ == "__main__":

    # Get the transaction receipt of the given tx hash through a custom RPC request
    txReceipt = moonbeamAPIProvider.rpc_request('eth_getTransactionCount', [wallet, '938930'])
    print(txReceipt["result"])

