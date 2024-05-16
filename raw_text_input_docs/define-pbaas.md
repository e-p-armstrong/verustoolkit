# Defining a PBaaS-blockchain

::: warning Information here is not complete. Need help setting up a blockchain launch? 🤔
[Go to the Verus Discord #pbaas-development channel. The community is happy to assist!](https://www.verus.io/discord) 
:::

There are many options to choose from when defining your blockchain. Combine them in the ``options`` parameter for different use cases.

| # | Options | Details |
| - |:-----|:-----|
| 1 | OPTION_FRACTIONAL | Allows reserve conversion using base calculations when set |
| 2 | OPTION_ID_ISSUANCE | Clear is permissionless, if set, IDs may only be created by controlling ID |
| 4 | OPTION_ID_STAKING | All IDs on chain stake equally, rather than value-based staking |
| 8 | OPTION_ID_REFERRALS | If set, this chain supports referrals |
| 16 | OPTION_ID_REFERRALREQUIRED | If set, this chain requires referrals |
| 32 | OPTION_TOKEN | If set, this is a token, not a native currency |
| 64 | OPTION_SINGLECURRENCY | For PBaaS chains or gateways to potentially restrict to single currency |
| 128 | OPTION_GATEWAY | If set, this routes external currencies |
| 256 | OPTION_PBAAS | This is a PBaaS chain definition|
| 512 | OPTION_GATEWAY_CONVERTER | This means that for a specific PBaaS gateway, this is the default converter and will publish prices |
| 1024 | OPTION_GATEWAY_NAMECONTROLLER | When not set on a gateway, top level ID and currency registration happen on launch chain |
| 2048 | OPTION_NFT_TOKEN | Single satoshi NFT token, tokenizes control over the root ID |


## VerusID Namespace
To create a blockchain of a specific name, you need a VerusID of the same name. The controller of this VerusID is the only one who can create a blockchain of that name, and they can only do so once.

## Examples of blockchain launches

::: danger Limit for all currency supplies (10 billion)
10 billion (-1 SATOSHI) with 8 decimal places (9999999999.99999999) is now the recommended absolute limit for all currency supplies, including over time with conversions and extended tail emissions for blockchains.
:::

### Blockchain 1

``` json
./verus -chain=VRSCTEST definecurrency '{
    "name":"PBaaSChain",
    "options":264,
    "currencies":["VRSCTEST"],
    "conversions":[1],
    "eras":[
        {
            "reward":1200000000,
            "decay":0,
            "halving":0,
            "eraend":0
        }
    ],
    "notaries":[
        "Notary1@",
        "Notary2@",
        "Notary3@"
    ],
    "minnotariesconfirm":2,
    "nodes":[
        {
            "networkaddress":"111.111.111.111:10000",
            "nodeidentity":"Node1@"
        },
        {
            "networkaddress":"111.111.111.112:10000",
            "nodeidentity":"Node2@"
        }
    ],
    "gatewayconvertername":"Bridge",
    "gatewayconverterissuance":1000000
    }' 
    '{
        "currencies":["VRSCTEST","PBaaSChain","USD"],
        "initialcontributions":[371747.20398827,0,1000000],
        "initialsupply":3000000
    }'
```

### Blockchain 2

``` json
./verus -chain=vrsctest definecurrency '{
    "name":"v2",
    "options":264,
    "currencies":["vrsctest"],
    "preallocations":[
        {
            "allnotary1@":800000
        }
    ],
    "conversions":[1],
    "eras":[
        {
            "reward":76800000000,
            "decay":0,
            "halving":525000,
            "eraend":0
        }
    ],
    "blocktime":10,
    "idregistrationfees":25,
    "notaries":[
        "allnotary1@",
        "allnotary2@",
        "allnotary3@"
        ],
    "startblock":9500,
    "minnotariesconfirm":2,
    "nodes":[
        {
            "networkaddress":"45.76.168.133:20022",
            "nodeidentity": "allnotary1@"
        },
        {
            "networkaddress":"149.28.95.28:20022",
            "nodeidentity":"allnotary2@"
        },
        {
            "networkaddress":"45.63.58.171:20022",
            "nodeidentity":"allnotary3@"
        }
    ],
    "gatewayconvertername":"Bridge",
    "gatewayconverterissuance":800000
    }' 
    '{
        "currencies":["VRSCTEST","v2"],
        "initialcontributions":[2500,0],
        "initialsupply":800000
    }'
```

::: warning Need help setting up a blockchain launch? 🤔
[Go to the Verus Discord #pbaas-development channel. The community is happy to assist!](https://www.verus.io/discord)
:::