# Introduction
Launching currencies on Verus, and any other PBaaS-chain (Public Blockchains as a Service), is better, faster, cheaper and more secure than any EVM-like protocol out there. There is no coding involved.

There are two types of currencies that can be launched with the Verus Protocol. Basket currencies (e.g. liquidity pools) and simple token currencies. Both can be issued decentralized, or centralized with minting and burning capabilities.

When a currency is launched, subIDs can be created from it. SubIDs are powerful objects on Verus (and other PBaaS-blockchains). They are exactly the same as [VerusIDs](/verusid/), yet can not launch blockchains or currencies.



## Basket currencies (e.g. liquidity pools)
![image-basket-currencies](/images/currencies-reserves.png)

Basket currencies function like automated market makers (AMMs), they have reserves. A reserve can be any currency or token on the Verus network (also bridged). Have a look at the simplified image. If anyone has currency X or Y, they can convert to the basket currency, or convert from reserve to reserve. If anyone has the basket currency, they can go to currency X or Y. A basket currency can have 1 and up to 10 currencies in its reserves.

The basket currency supply is dynamic, depending on how much is converted to the basket currency (supply minted), or back to its reserve(s) (supply burned).

A basket currency can be 100% backed by its reserves, 5%, or anything in between. This is called the reserve ratio, or the weight. The lower the reserve ratio, the more volatile the currency is when people are converting into or out of the basket currency. The value of the basket currency is directly linked to what is in the reserves and what the reserve ratio is.

When a centralized version of this currency is created, the owner of the rootID can mint currencies into existence, while automatically lowering the reserve ratio. Or they can burn currencies and automatically raise the reserve ratio. Anyone can also just burn the currency at will without raising the reserve ratio.

The conversion fees are incredibly low, 0.025% when converting to and from a basket currency, and 0.05% when converting from reserve to reserve currency. These fees go directly to the worldwide miners and stakers of the protocol, and/or they are accrued into the reserves making the basket currency worth more.

| Conversion type | Fee | Fee goes to |
| :-----| :------ | :-------- |
| Basket currency ↔️ reserve | 0.025% | 0.0125% added to reserves of the basket currency, 0.0125% to the block reward for miners and stakers  | 
| Reserve ↔️ reserve | 0.05% | 0.025% added to reserves of the basket currency, 0.025% to the block reward for miners and stakers |


Because all currency conversions are solved simultaneously inside a block, giving all participants the same price, the protocol is MEV-free (no front-running, back-running, sandwich attacks etc.). The protocol doesn’t have any of the problems EVM-like account-based systems have. Verus DeFi is fair, cheap and has no rent-seekers.

Every(!) currency and token on the Verus network (also mapped ERC-20s!), can be used as reserves for basket currencies. As you might start to understand now — basket currencies are unique currencies that can not be found anywhere else and offer an enormous amount of opportunities for value creation.

## Simple token currencies
Simple token currencies and are just currencies without any reserves. They are not as exciting as the basket currencies, yet still offer much value. With all the parameters that can be added, subIDs created and decentralized crowdfund mechanisms, these currencies can support a lot of use cases that are difficult to do with alternative protocols.

The supply of this type of currency is static when it’s a decentralized version. When it’s a centralized version, the owner of the rootID can mint tokens into existence, and anyone can burn them.

This option is also used to create currencies that are mapped to Ethereum ERC-20s. Which means you can send those ERC-20s over to Verus, or from Verus to the ERC-20. This is made possible with the non-custodial Verus-Ethereum Bridge. You can read more about it here.

And of course, a simple token currency can be one of the reserves in a basket currency.

## Ethereum ERC-20 
The Verus-Ethereum Bridge makes it possible for currencies and tokens to be send over to Ethereum, and back to Verus. It is a true non-custodial bridge. All tokens and currencies flowing over the bridge are never in anyone’s custody, and are proven and verified by consensus rules. [Everything on the Verus-Ethereum Bridge here.](/eth-bridge/)

Any currency and token, on Verus or any other PBaaS-blockchain, can be exported to Ethereum as an ERC-20. They can then be used in the Ethereum ecosystem. 

Also, any already existing ERC-20 token can be mapped one-to-one as a Verus currency. Meaning any ERC-20 token can live on the Verus blockchain (or any other PBaaS-chain) and take advantage of all the L1 features.

## Crowdfund mechanisms
All currencies can be launched through decentralized crowdfund mechanisms. [Set required minimum levels](/currencies/launch-currency.html#minpreconversion) of worldwide participation in your preferred currencies. If by the start time of your currency or token, minimums are not met, all participants will automatically get a refund of all of their preconversions, less the network fees.

The launch options also provide for maximum participation in one or more currencies, pre-launch discounts, price neutral [pre-allocations](launch-currency.html#preallocations) to select VerusIDs that increase the reserve ratio to issue currencies, similarly price neutral [carve-outs of proceeds](launch-currency.html#prelaunchcarveout), and [pre-launch discounts](launch-currency.html#prelaunchdiscount) for early participants. Using VerusIDs, launches can also include vesting schedules in the pre-allocations as well.

#