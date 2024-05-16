# Export currency to Ethereum (as ERC-20)

Any currency on Verus can be exported to Ethereum as an ERC-20. The currency can then be used in the complete Ethereum ecosystem, and on the Verus network. Sending to and from Verus and Ethereum couldn't be easier. [More on the Verus-Ethereum Bridge.](/eth-bridge/)

::: tip ↔️ Verus-Ethereum Bridge 👨‍🔧 For Testnet!
[👉 Access the Verus-Ethereum Testnet Bridge](https://ethbridge.verustest.net/) (⚠️ Goerli testnet)
:::

::: tip ↔️ Verus-Ethereum Bridge ✅ For Mainnet!
[👉 Access the Verus-Ethereum Mainnet Bridge](https://eth.verusbridge.io)
:::

### Exporting the currency
Now, let’s export a currency from Verus to Ethereum as an ERC-20 over the non-custodial bridge. We must have enough funds to pay for the export. 

The command to export a currency to Ethereum as an ERC-20:

``` json
./verus -chain=VRSCTEST sendcurrency "myVerusID@" '[{
    "address":"0x85a7dE2278E52327471e174AeeB280cdFdC6A68a", 
    "currency":"myCurrency", 
    "amount":0, 
    "exportto":"veth", 
    "exportcurrency":true, 
    "feecurrency":"veth"
}]'
```

Let's break the command down with what you can change.

**``myVerusID@``** is the from- and change-address. Can be a VerusID, R-address or i-address. The fee to pay for the export comes from here, and if you paid too much fees the rest will be returned here.

**``address``** You can fill in any ETH-address here, it is actually not important what is here.

**``currency``** is the name of the currency you wish to export as an ERC-20. E.g. `MyCurrency`, `MyCurrency.vETH`.


### Wait for notarization

After the bridge has been notarized to the blockheight where you have exported the currency, you can choose it from the token dropdown on the [Bridge website mainnet](https://eth.verusbridge.io) or [Bridge website Goerli testnet](https://ethbridge.verustest.net/)
