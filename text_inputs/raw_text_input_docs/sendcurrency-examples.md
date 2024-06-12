# API commands
All functionality is easily accessible by doing API commands. Here are a few examples:


## Converting (DeFi)

### Estimate conversion price
The ``estimateconversion`` API estimates what you might receive for a certain conversion.

Example:
``` json
./verus -chain=VRSCTEST estimateconversion '{
    "currency":"vrsctest",
    "convertto":"veth",
    "via":"bridge.veth",
    "amount":1000
}'
```

Example:
``` json
./verus -chain=VRSCTEST estimateconversion '{
    "currency":"vrsctest",
    "convertto":"bridge.veth",
    "amount":500
}'
```


### Get currency converters
The ``getcurrencyconverters`` API retrieves all currencies that have at least 1000 VRSC in reserve, are greater than 10% VRSC reserve ratio, and have all listed currencies as reserves.

Example ``btc`` and ``eth``:
``` json
./verus -chain=VRSCTEST getcurrencyconverters btc eth
```


### Converting VRSCTEST to basket currency
Converting VRSCTEST to a basket currency, VRSC-BTC, using IDs as a funding source:
``` json
./verus -chain=VRSCTEST sendcurrency "*i" '[{
    "address":"bob@",
    "amount":10,
    "convertto":"VRSC-BTC"
}]'
```

### Converting VRSCTEST to BTC via basket currency
Converting VRSCTEST to another reserve, BTC through a basket currency, VRSC-BTC:
``` json
./verus -chain=VRSCTEST sendcurrency "*" '[{
    "address":"bob@",
    "amount":10,
    "convertto":"BTC",
    "via":"VRSC-BTC"
}]'
```
### Preconverting
Preconverting to new currency, NEWCOIN, before it is active:
``` json
./verus -chain=VRSCTEST sendcurrency "*" '[{
    "address":"alice@",
    "amount":10,
    "convertto":"NEWCOIN",
    "preconvert":true,
    "refundto":"alice@"
}]'
```

### Converting VRSCTEST cross-chain to PBaaS-chain
``` json
./verus -chain=VRSCTEST sendcurrency "*" '[{
    "address":"RXLYm4J6qi7yam9zXtkEkRwbvCrnWKGZuv",
    "amount":10,
    "convertto":"PBaaSChain",
    "exportto":"Bridge.PBaaSChain",
    "via":"Bridge.PBaaSChain"
}]'
```

### Converting PBaaS-chain to VRSCTEST
``` json
./verus -chain=PBaaSChain sendcurrency "*" '[{
    "address":"RXLYm4J6qi7yam9zXtkEkRwbvCrnWKGZuv",
    "amount":10,
    "convertto":"VRSCTEST",
    "exportto":"VRSCTEST",
    "via":"Bridge.PBaaSChain"
}]'
```

## Sending
Sending VRSCTEST from a single address (bob@) to a single recipient (alice@):
``` json
./verus -chain=VRSCTEST sendcurrency "bob@" '[{
    "currency":"vrsctest",
    "address":"alice@",
    "amount":10
}]'
```

Sending VRSCTEST from all private wallet funds to two recipients with friendly-name z-addresses (alice@:private and bob@:private):
``` json
./verus -chain=VRSCTEST sendcurrency "*Z" '[{
    "currency":"vrsctest",
    "address":"alice@:private",
    "amount":10
},
{
    "currency":"VRSCTEST",
    "address":"bob@:private",
    "amount":10
}]'
```

Sending VRSCTEST cross-chain to PBaaSChain:
``` json
./verus -chain=VRSCTEST sendcurrency "*" '[{
    "address":"RXLYm4J6qi7yam9zXtkEkRwbvCrnWKGZuv",
    "amount":10,
    "exportto":"Bridge.PBaaSChain"
}]'
```
