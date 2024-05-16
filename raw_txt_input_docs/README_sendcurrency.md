
# Introduction
Verus DeFi is incredibly simple, low-cost, MEV-resistant and without any middleman. You can convert into a currency that has reserves (you are now "providing liquidity"), and you can convert out of the currency again, back into its reserves. Furthermore you can convert from reserve to reserve. [Learn more about basket currencies (DeFi AMMs).](/currencies/#basket-currencies)

| Verus DeFi | Details | 
| :-----| :------ | 
| ✅ **MEV-resistant** | Because of protocol design there is no front/back running. Every participant gets the same, fair conversion rate in one or more blocks. | 
| ✅ **Protocol level security** | All DeFi operations take place on the consensus layer of the protocol, and are verified by miners and stakers. There is no smart contract risk. | 
| ✅ **Low fees** | Protocol conversion fees are as low as 0.025%, or as high as 0.05%.  | 

Two conversion types:

| Conversion type | Fee | Fee goes to |
| :-----| :------ | :-------- |
| Basket currency ↔️ reserve | 0.025% | 0.0125% added to reserves of the basket currency, 0.0125% to the block reward for miners and stakers | 
| Reserve ↔️ reserve | 0.05% | 0.025% added to reserves of the basket currency, 0.025% to the block reward for miners and stakers |

## L1 DeFi
Verus is a ``UTXO-based`` blockchain with ``smart transactions``. All smart capabilities are implemented on the protocol level. This has many advantages over blockchain projects that use layer two solutions. [Read "Smart Transactions vs. Smart Contracts"](https://medium.com/veruscoin/verus-smart-transactions-vs-smart-contracts-f98079c00ed0)

Advantages of DeFi at the protocol level:

* Increased security at the application level - Verus DeFi is not implemented by having many smart contract authors creating smart contracts on top of the protocol, so there can be no exploits by searching for unintended "cracks" in the seams between contracts.

* Increased security at the protocol level - Verus DeFi is implemented in the protocol as part of the consensus, following the fundamental systems design principle which says that the most important security layers should be located in the system/protocol itself.

## MEV-resistance

The Verus protocol solves all transactions ``simultaneously`` within a block (as opposed to serially, in order, as is done on Ethereum and all other systems which use the VM-model). This has important implications for security, fairness, and efficiency:

* Elimination of front-running, back-running and sandwich attacks.

* Enhancing system-wide liquidity, thus reducing slippage, as conversions going to and from any given currency within the same block are offset against each other.

* Providing all users converting to and from a currency within the same block the same fair price with no spread.



