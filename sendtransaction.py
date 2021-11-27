from substrateinterface import SubstrateInterface, Keypair, KeypairType
from substrateinterface.exceptions import SubstrateRequestException




if __name__ == "__main__":

    # Point API Provider to Moonriver Network
    moonbeamAPIProvider = SubstrateInterface(
        url="wss://wss.testnet.moonbeam.network",
    )

    # Define the Ethereum TxHash to Check Finality
    privatekey = bytes.fromhex("b516d07cbf975a08adf9465c4864b6d7e348b04c241db5eb8f24d89de629d387")
    mnemonic = 'episode together nose spoon dose oil faculty zoo ankle evoke admit walnut'


    moonbeamAPIProvider.init_runtime()
    moonbeamAPIProvider.runtime_config.update_type_registry({
        "types": {
            "Address": "H160",
            "LookupSource": "H160",
            "AccountId": "H160",
            "ExtrinsicSignature": "EcdsaSignature",
        }
    })

    keypair = Keypair.create_from_private_key(privatekey, crypto_type=KeypairType.ED25519)
    #keypair = Keypair.create_from_mnemonic(mnemonic, crypto_type=KeypairType.ED25519)

    signature = keypair.sign("Test123")

    print(signature)

    call = moonbeamAPIProvider.compose_call(
        call_module='Balances',
        call_function='transfer',
        call_params={
            'dest': '0x44236223aB4291b93EEd10E4B511B37a398DEE55',
            'value': 1 * 10**12
        }
    )

    #extrinsic = moonbeamAPIProvider.create_signed_extrinsic(call=call, keypair=keypair)

    #try:
        #receipt = moonbeamAPIProvider.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        #print("Extrinsic '{}' sent and included in block '{}'".format(receipt.extrinsic_hash, receipt.block_hash))

    #except SubstrateRequestException as e:
        #print("Failed to send: {}".format(e))

