import string

class SafeFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, str):
            return kwargs.get(key, '{' + key + '}')
        else:
            return super().get_value(key, args, kwargs)

    def parse(self, format_string):
        try:
            return super().parse(format_string)
        except ValueError:
            return [(format_string, None, None, None)]

def safe_format(format_string, *args, **kwargs):
    formatter = SafeFormatter()
    return formatter.format(format_string, *args, **kwargs)


format_string = '''Text to make questions from: 
"""
```
./verus -chain=VRSCTEST sendcurrency "*" '[{"address":"mike@","convertto":"gold","preconvert":1,"amount":100}]'
```
that would effectively park my conversion until the token launches, at which point, I will either find 0.975 GOLD in my wallet, or I will have my VRSCTEST back.
Assuming it launches, and I later want to create mycoin, which can be converted to with either GOLD or VRSCTEST, I can create mycoin with:

    ```
./verus -chain=VRSCTEST definecurrency '{"name":"mycoin","options":33, "proofprotocol":2,"currencies":["vrsctest", "gold"],"minpreconversion":[10000,5.1298]}, "initialsupply":20000'
```
In "mycoin", I set proofprotocol to 2, which is PROOF_CHAINID. That means that the controller of the chain ID can mint new coins as follows:

    ```
./verus -chain=VRSCTEST sendcurrency "mycoin@" '[{"address":"mike@","currency":"mycoin","mintnew":1,"amount":10000}]'
```

#### Defining a PBaaS blockchain
```json
    {
    "name": "PBaaSChain",
    "options": 264,
    "currencies": [
    "VRSCTEST"
    ],
    "conversions": [
    1
    ],
    "eras": [
    {
        "reward": 1200000000,
        "decay": 0,
        "halving": 0,
        "eraend": 0
    }
    ],
    "notaries": [
    "Notary1@",
    "Notary2@",
    "Notary3@"
    ],
    "minnotariesconfirm": 2,
    "nodes": [
    {
        "networkaddress": "111.111.111.111:10000",
        "nodeidentity": "Node1@"
    },
    {
        "networkaddress": "111.111.111.112:10000",
        "nodeidentity": "Node2@"
    }
    ],
    "gatewayconvertername": "Bridge",
    "gatewayconverterissuance": 1000000
}
```
The bridge definition has overridable defaults
```json
    {
    "currencies": [
    "VRSCTEST",
    "PBaaSChain",
    "USD"
    ],
    "initialcontributions": [
    380228.12033701,
    0,
    1000000
    ],
    "initialsupply": 3000000
}
```

Now pass those definitions to `definecurrency`
```shell
./verus -chain=vrsctest definecurrency '{"name":"PBaaSChain","options":264,"currencies":["VRSCTEST"],"conversions":[1],"eras":[{"reward":1200000000,"decay":0,"halving":0,"eraend":0}],"notaries":["Notary1@","Notary2@","Notary3@"],"minnotariesconfirm":2,"nodes":[{"networkaddress":"111.111.111.111:10000","nodeidentity":"Node1@"},{"networkaddress":"111.111.111.112:10000","nodeidentity":"Node2@"}],"gatewayconvertername":"Bridge","gatewayconverterissuance":1000000}' '{"currencies":["VRSCTEST","PBaaSChain","USD"],"initialcontributions":[371747.20398827,0,1000000],"initialsupply":3000000}'
```
#### Exporting an ID to a PBaaS chain
```
verus -chain=VRSCTEST sendcurrency "*" '[{"address":"IDNAME@","exportto":"PBaaSChainName","exportid":"true","amount":100,"currency":"vrsctest"}]'
```

### Signing transactions from multi-signature IDs (testnet and mainnet)
Create transaction, get raw transaction data:
    ```
verus sendcurrency <multi-signature-ID>@ '[{"address":"<destination_address>","amount":<transaction_amount>}]'
verus z_getoperationstatus <operation_id_returned_by_sendcurrency>
```
Take the raw hex transaction data provided by z_getoperationstatus to each additional wallet(s) containing the additional signing addresses/IDs:
    ```
verus signrawtransaction <raw_hex_transaction>
```
After the last necessary signature is applied, broadcast on the network using:
    ```
verus sendrawtransaction <raw_hex_signed_transaction>
```
"""'''
result = safe_format(format_string, name="Alice", age=25)
print(result)  # Output: "Name: Alice, Age: 25, Data: {'key': 'value'}"