# What is the Verus-Ethereum Bridge
The Verus-Ethereum Bridge (fully operational since Oct 20, 2023) allows for the secure transfer and conversion of cryptocurrencies between Verus and Ethereum. It's **trustless** and **non-custodial**, meaning it doesn't require users to trust a third party with their funds, and **no single entity has control over the assets being transferred**.

The Bridge stands out because it avoids common security issues found in other cryptocurrency bridges by using the decentralized network of miners and stakers to verify and account for funds crossing the bridge.

👉 Access the Verus-Ethereum Bridge [with MetaMask or WalletConnect](https://eth.verusbridge.io), or download Verus Mobile for [iOS](https://apps.apple.com/en/app/verus-mobile/id6447361908) and [Android](https://play.google.com/store/apps/details?id=org.autonomoussoftwarefoundation.verusmobile.android&hl=en&gl=US).

## What can the Verus-Ethereum Bridge do
The trustless and non-custodial Verus-Ethereum Bridge can be used for the following things:

| What              |          Details           |
| :------------------ | :----------------------------------------- |
| **Conversions**| Convert VRSC, ETH (vETH), DAI (DAI.vETH) & MKR (MKR.vETH) with each other into any direction (on/to Verus & Ethereum), or to and from the Bridge.vETH currency.|
| **Launch mapped currencies**|  Launch currencies on Verus that are 1:1 mapped to any ERC-20. [Learn how](/currencies/mapping-1:1-eth.html)|
| **Export currencies as ERC-20**| Export any launched currency (simple tokens, basket currencies) on Verus as an ERC-20. [Learn how](/currencies/export-to-eth.html)|
| **Cross-chain sends**| Send any tokens, basket currencies (e.g. liquidity pools), mapped currencies etc. that are exported to Ethereum across the bridge.|
| **Export tokenized ID control**| Export a tokenized VerusID to Ethereum as ERC-721.|
| **Map VerusID to Ethereum NFT**| Launch a tokenized ID with a mapping of an Ethereum ERC-721 or ERC-1155.|

Then there is the bridge currency Bridge.vETH, a 100% backed currency with 4 currencies in its reserves (VRSC, ETH, DAI, MKR). The Bridge.vETH currency function is to make the bridging of assets simple. From wherever you send it converts the fees that you need seamlessly. [More on Bridge.vETH below.](/eth-bridge/#bridge-veth-currency)


## What makes the Verus-Ethereum Bridge secure
The Verus-Ethereum Bridge is different because the assets are never in anyone’s custody. This is done through the seamless cooperation between the block producers (worldwide miners and stakers), community notary witnesses, [the Bridgekeeper software](https://github.com/VerusCoin/Verusbridgekeeper) and the [Ethereum smart contract](https://etherscan.io/address/0x71518580f36FeCEFfE0721F06bA4703218cD7F63). At each step during cross-chain transactions the assets are verified and proven by consensus rules, with safeguards in place to prevent hacks.

Every 10 blocks the block producers create a notarization (when there is traffic over the bridge). They create these digital receipts for both Verus and Ethereum. The digital receipts, called “notarizations", contain, among other things: the “stateroot” ([Merkle Mountain Range](https://www.investopedia.com/terms/m/merkle-root-cryptocurrency.asp) for Verus, [Merkle Patricia Trie](https://ethereum.org/en/developers/docs/data-structures-and-encoding/patricia-merkle-trie/) for Ethereum), the blockheight, blockhash and the gas price for Ethereum. The notarizations have to be agreed to by the block producers (miners and stakers) and are then mined into the Verus blockchain.

👉 [Read more here](https://medium.com/veruscoin/verus-internet-protocol-vip-provable-decentralized-cross-chain-communication-8d9414a429c5?source=rss----4869a79d7e7f---4) on how the Verus Protocol handles cross-chain communication (PBaaS-chains and more) in a decentralized and provable way.

### Safeguards against bridge hacks
Threats caused by malicious notary witnesses, or stolen keys to drain funds are not viable against the Verus-Ethereum Bridge. To successfully mount an attack on the bridge, if a majority of witnesses were colluding or got their private keys stolen the following would need to happen:

- Colluding, malicious witnesses.
- Fake block producers with more combined hash and stake power than the publicly validated Verus blockchain. [👉 Verus Paper: A Provable Hybrid Solution to 51% Hash Attacks](https://verus.io/papers/VerusPoP.pdf)
- Developers helping them by creating an alternate protocol for the shadow chain.

These requirements are very close to the requirements of attacking any blockchain. The bridge even provides a way to defend against such an unlikely scenario.

The notary witnesses are also monitoring notarizations, and if they were to sign for something that they themselves do not agree with, they can auto-revoke their identities, using the VerusID protocol, which cannot be stopped by an attacker unless they have stolen both the keys for the notary ID and those for its revocation ID as well. This serves as a prevention for stolen key attacks, ensuring that notaries are extremely hard targets to compromise.


## Bridge.vETH currency
Bridge.vETH is a 100% backed currency with 4 currencies in its reserves (VRSC, ETH, DAI, MKR), [read more on basket currencies](/currencies/). The Bridge.vETH currency function is to make the bridging of assets simple. From wherever side on the bridge you send it converts the fees that you need seamlessly.

The value of Bridge.vETH increases relative to reserves when fees or interest are added to the reserves without there being new Bridge.vETH minted. 

| 📈 Accrued fees              |          Details           |
| :------------------ | :----------------------------------------- |
| [**Dai Savings Rate**](https://blog.makerdao.com/an-update-on-the-dai-savings-rate-in-multi-collateral-dai/)| 5% interest (at the time of writing, the rate is subject to change by MakerDAO) is earned automatically when holding Dai in the DSR (Dai Savings Rate) contract. Dai in Bridge.vETH and in the complete Verus ecosystem get this savings rate. The DSR is being passed through 100% to the DAI reserves of Bridge.vETH.|
| **.vETH subID registrations**| A .vETH subID costs 0.01 vETH worth of Bridge.vETH. When registering the subID the Bridge.vETH is burned, meaning the Bridge.vETH supply decreases. |
| **Conversion fees**| 50% of the conversion fees go into the reserves of Bridge.vETH: 0.025% when it's a reserve to reserve conversion, 0.0125% when it's a reserve to Bridge.vETH conversion (or vice versa). |
| **Cross-chain send fees**| A share of the cross-chain send fees go into the reserves of Bridge.vETH. |

Bridge.vETH had an initial supply of 100,000. During the preconversion timeframe which lasted 10 days, anyone could add VRSC, ETH, DAI and MKR into its reserves. When the preconversion period ended everyone got their share of the 100,000 Bridge.vETH, distributed by the protocol. 

The supply of Bridge.vETH is dynamic. The currency gets minted when people convert VRSC, ETH, DAI or MKR to Bridge.vETH, and the currency gets burned when they convert from Bridge.vETH back to VRSC, ETH, DAI or MKR.

Converting currencies using Bridge.vETH (or other basket currencies) has many advantages. It is MEV-resistant, has no smart contract risks due to protocol level security and has low fees (max. 0.05%). [More on Verus DeFi here.](/sendcurrency/)

See statistics for Bridge.vETH here: [verus.io/eth-bridge](https://verus.io/eth-bridge)

## .vETH subID
Register a .vETH subID to launch a currency with a 1-to-1 mapping of an ERC-20. The cost is 0.01 vETH worth of Bridge.vETH. 

[Learn here how to register a VerusID / subID.](/verusid/verusid-create/)

## Contract addresses

| What              |          Contract address           |
| :------------------ | :----------------------------------------- |
| Verus-Ethereum Bridge smart contract **mainnet**| [0x71518580f36FeCEFfE0721F06bA4703218cD7F63](https://etherscan.io/address/0x71518580f36FeCEFfE0721F06bA4703218cD7F63) |
| **VRSC** token address| [0xBc2738BA63882891094C99E59a02141Ca1A1C36a](https://etherscan.io/token/0xbc2738ba63882891094c99e59a02141ca1a1c36a) |
| **Bridge.vETH** token address| [0xE6052Dcc60573561ECef2D9A4C0FEA6d3aC5B9A2](https://etherscan.io/token/0xE6052Dcc60573561ECef2D9A4C0FEA6d3aC5B9A2) |


