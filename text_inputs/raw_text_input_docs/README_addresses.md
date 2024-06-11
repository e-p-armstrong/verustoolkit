
# Introduction

VerusID is the first decentralized and self-sovereign identity of its kind, the permanent namespace for the Verus Protocol, and the building block to create Web3 Dapps.

## Feature List

| Feature | Details | 
| :-----| :------ | 
| **Namespace** | VerusID is the permanent namespace for the Verus Protocol and can be registered by anyone. | 
| **Self-sovereign identity** | VerusID can function as a self-sovereign identity for anyone in the world, empowering individuals with complete autonomy both online and offline. |
| [**Blockchain launches**](/blockchains/) | With the VerusID namespace anyone can launch fully interconnected, customizable, independent and secure blockchains, without any coding needed (just simple commands). | 
| [**Currency & token launches**](/currencies/) | With the VerusID namespace anyone can launch powerful currencies and tokens, including basket currencies (DeFi AMMs). |
| [**Publish & store data**](/vdxf/README) | Use VerusID and VDXF as a controlled public storage system. Publish and store data with multiple levels of nesting. | 
| [**Revoking & recovering**](/verusid/#revoke-recover) | Each VerusID has revocation and recovery authorities (which are also VerusIDs). Autonomously revoke access to a VerusID, and recover all assets and data on a VerusID. | 
| [**Friendly name address**](/verusid/#friendly-name) | A VerusID is a friendly name address that can send, receive and hold assets.  | 
| [**Verus Vault**](/verusid/#verus-vault) | Enable theft-proof Verus Vault. Set locks or timelocks to secure assets on a VerusID. | 
| [**Marketplace**](/verusid/#marketplace) | Peer-to-peer decentralized marketplace for VerusIDs and currencies and tokens. | 
| **Privacy** | Point a private address to a VerusID. Send and receive native assets with full anonimity.  | 
| **Signatures** | Create unforgable, verifiable signatures with VerusID. Sign files, hashes and messages. | 
| **Multisig** | Multiple organizations or people can manage a VerusID.  | 
| **Messages** | Send and receive completely private messages through VerusID private addresses. | 
| [**SSID login**](/verusid/login/) | Login to supported VerusID services without ever needing a password. |
| **SubID** | Under each launched currency and token subIDs can be registered. SubIDs have the exact same features as VerusIDs, although they can not launch blockchains, currencies or tokens. | 


VerusIDs can be anything you want. They can be bound digitally to many things. They can be bound to you, or other VerusIDs they have authority or ownership of. They can be bound to an unlimited amount of content, data, and provable information, both public and private. Including provable contracts and rights that can be bound to ownership of the VerusID itself.

VerusIDs can hold funds. They can be personal profiles, corporate websites, or government portals. VerusIDs are much more than identities or today's NFTs. They are owned assets of all kinds on the Verus blockchain.

A VerusID can be revoked and recovered, set (time)locks and can be controlled by any number of identities. Sign and verify data, files and messages. VerusID has privacy through added z-addresses and can send and receive messages. Identities can communicate in standardized ways through the novel [Verus Data Exchange Format (VDXF)](/vdxf/README).

## Real Estate
A VerusID is **premium** real estate on the Verus blockchain. To create PBaaS-chains, tokens and currencies on the Verus blockchain, a VerusID is necessary. The name you assign to the VerusID is also the name of the PBaaS-chain, token or currency.

Each PBaaS-chain has standard VerusID support and creators of these chains can assign the costs of identites themselves. The costs will then be paid in the native coin of the PBaaS-chain.

## Friendly Name
Each VerusID can have an easy to remember name, chosen by the user. It has never been easier to send and receive funds.

::: tip Supporting Worldwide Adoption
All characters from **all character sets** (except ``/`` ``:`` ``*`` ``?`` ``"`` ``<`` ``>`` ``|`` ``@`` ``.`` ) are available to create a VerusID.
:::

## Costs
**On the Verus blockchain** a VerusID costs 100 VRSC. These costs can be discounted with referrals. All costs paid are going to the [miners and stakers of the ecosystem](/economy/) and to the referrals if used.

|  | VerusID Cost |
| :----------------------- | --: | 
| **Base cost** | 100 VRSC | 
| **Cost with referral used** | 80 VRSC | 


### Referrals
A referral system is implemented to reward users with identities. For each VerusID a user creates, the referral identity receives 20 VRSC. The referral system goes three levels down. 

If one owns three identities that are stringed together through its referrals, one can receive 60 VRSC with each VerusID creation. This way an identity only has to cost 20 VRSC. 

::: tip Support the Verus Vision
Use ``Verus Coin Foundation@`` when creating a VerusID on the Verus blockchain. All proceeds will go to the further development of the Verus vision.
:::

## Structure
An example of a VerusID:
| Structure | Information |
| :----------------------- | :--------------------- | 
| **VerusID Name** | The name is a unique namespace and human readable cryptocurrency address.  | 
| **Primary Address** | The primary address is the owner of the VerusID, as it contains the private key. It can contain more than one VerusID. | 
| **Identity Address** | The identity address is, next to the name, the identifier of the VerusID. | 
| **Private Address** | An optional attached private z-address | 
| **Revocation Authority** | The identity address that can revoke the VerusID | 
| **Recovery Authority** | The identity address that can recover the VerusID | 
| **Contentmap** | VDXF key/value data | 

Input:
```
./verus getidentity "Verus Coin Foundation@"
```
Output:
``` json
{
"fullyqualifiedname": "Verus Coin Foundation.VRSC@",
"identity": {
"version": 3,
"flags": 0,
"primaryaddresses": ["REpxm9bCLMiHRNVPA9unPBWixie7uHFA5C"],
"minimumsignatures": 1,
"name": "Verus Coin Foundation",
"identityaddress": "i5v3h9FWVdRFbNHU7DfcpGykQjRaHtMqu7",
"parent": "i5w5MuNik5NtLcYmNzcvaoixooEebB6MGV",
"systemid": "i5w5MuNik5NtLcYmNzcvaoixooEebB6MGV",
"contentmap": {

},
"contentmultimap": {
"i5Zkx5Z7tEfh42xtKfwbJ5LgEWE9rEgpFY": [{
"i5Zkx5Z7tEfh42xtKfwbJ5LgEWE9rEgpFY": {
"version": 1,
"action": 2,
"entrykey": "73960afaad96f923c616b26f9646c059021d4ffa",
"valuehash": "10230fb3df7c507f062593c55d94d1442f937b68b71e045c442e1e49647cfc6a"
}
},
{
"i5Zkx5Z7tEfh42xtKfwbJ5LgEWE9rEgpFY": {
"version": 1,
"action": 2,
"entrykey": "73960afaad96f923c616b26f9646c059021d4ffa",
"valuehash": "9ed2b3516d4ccd2d419bfb12f325902e1a3f566d222445c97005e4e8fee5903a"
}
}],
"iSJ38vYX7qoCtotc9wBHb1vZdR3oTgoHCX": ["0186ff9300d99a27d51944ef1563b8c3b7445bc67ce91cebc8809cff0000"]
},
"revocationauthority": "i5v3h9FWVdRFbNHU7DfcpGykQjRaHtMqu7",
"recoveryauthority": "i5v3h9FWVdRFbNHU7DfcpGykQjRaHtMqu7",
"privateaddress": "zs1dycegwse0x67qvy2fksukcng3ekkgvly2qwjckj8fxraam33xu2y5jyh3yva0e4ywec9quedcud",
"timelock": 0
},
"status": "active",
"canspendfor": false,
"cansignfor": false,
"blockheight": 2588672,
"txid": "802e3e5e928038bdabae648f0690d919bce85759b3ecc845db458cc1dba0fe83",
"vout": 0
}
```



## Revoke & Recover
Revoking and recovering identities are essentials in a decentralized system. Users need to have full self-sovereignty to move around in an ecosystem without central control. VerusID is the first decentralized identity system where users have full control over their identities. 

When creating a VerusID users can assign a ``RevokeID`` and a ``RecoveryID`` to their VerusID. They can be the same identities, different ones or appointed ``self``. These assigned identities are also VerusIDs and thus must be purchased.

| Action | Outcome |
| :----------------------- | :-- | 
| Revoking | Funds can not be spent anymore | 
| Recovering | Recover all assets to a new address. Funds and UTXOs can be spent again | 


::: danger Be Careful
Don't assign a ``RecoveryID`` to ``self`` when the ``RevokeID`` is assigned to another identity. This way when you revoke an identity, you can not recover it anymore.
:::

## Verus Vault
The Verus Vault for identities is a unique feature to create extra security. Set locks or timelocks to safeguard funds on a VerusID. Locked identities can not spend funds.

### How it Works
There are three stages the Vault can be set to. When the vault is locked it can not spend funds.

| Action | Outcome |
| :----------------------- | :-- | 
| Locked until x blocks | Funds can not be spent, until a predetermined number of blocks have passed | 
| Locked with delay | Funds can not be spent, until an unlock has been requested + predetermined number of blocks have passed | 
| Unlocked | Funds can be spent | 

When a VerusID is locked or timelocked, it can still receive, hold and stake funds. It can also still be used for signing. 

[Learn here how to set up Verus Vault in Verus Desktop](/guides/setup-vault-v2/)

::: warning Revoking Locked VerusID
Even when a VerusID is locked, it can still be [revoked and recovered](/verusid/specifications#revoke-recover/). 
:::

### Vault Use Case Examples

:::tip Safe Staking
Put funds to stake with on a VerusID. Use Vault to lock the identity with a delay of 10,080 blocks ( ~1 week). Now whenever someone gains access to the private keys of the locked VerusID, they have to unlock the identity in order to spend the funds. When someone makes an unlock request that isn't you, you are warned. The intruder has to wait 10,080 blocks before he can spend the funds. If you have set up revocation and recovery authorities, you now have one week to safeguard your funds away from prying hands, back into your control.
:::

:::tip Trusts
Setting up a trust fund for your children. Give your child a time locked VerusID with funds on them. When he or she turns 18, the VerusID unlocks and the funds can be spent. Keep revocation and recovery authorities with yourself or a trustee.
:::

:::tip Vesting Periods
When doing a currency or chain launch, development funds can be diverted to a locked VerusID. After two years the VerusID unlocks and the funds can only be spent with signatures of other developers. You can also spread the funds across multiple identities with different unlock periods.
:::

## Marketplace
With the VerusID Marketplace protocol, anyone is able to buy and sell VerusIDs. You can look for offers on any VerusID (buy or sell offers). If you like the best offer on your VerusID, or if someone likes an offer you made on theirs, the deal is made 100% peer-to-peer, decentralized on the blockchain, without any middleman or contract controller.

For total payment privacy, you can even pay or receive payment using private addresses and zero knowledge transactions based on the Zcash Sapling protocol.

### Exchanging in Private

In addition to advertising worldwide on the blockchain to buy or sell VerusIDs, you can also make an exchange with the Marketplace without ever posting the offer on the blockchain until it is agreed and signed by all parties. Combine that with zero knowledge transactions, and it's a great way to transact worldwide, escrow-free in private.

:::tip Use Case Example
A business sells subscriptions for exclusive content. They make VerusIDs with contracts that give access to the exclusive content. They now create a transaction that would pay for the VerusID. They give the transaction to the buyer who then executes it. The buyer now owns the VerusID that gives access to the exclusive content.
:::

Now imagine how you can do this for a VerusID that can be any kind of asset. A new way for everyone to engage in peer-to-peer, escrow-free commerce has arrived.

### RPC APIs
| API | What it does | 
| :- |:-----|
| makeoffer | define what you offer and for what. What you offer can be funds, VerusIDs, or when PBaaS goes live even other currencies. What you want in return can also be funds, VerusIDs or currencies. In exchange for what you offer, you also define what VerusID or how much you want for it and in what currency | 
| takeoffer | take a specific offer in exchange for its request | 
| getoffers | specify which VerusID or currency you want to see offers for or on offer, and it returns all offers (buy and sell) in all currencies, sorted by highest to lowest price | 
| closeoffers | close expired or unexpired offers which you opened with makeoffer |
| listopenoffers | list all offers that you have opened with makeoffer |

## Privacy
A VerusID can contain a pointer to a ``z-address``. These are private addresses that can not be checked on the public blockchain. Attach any z-address to a VerusID. 

## Signatures
Create unforgable, verifiable signatures with VerusID. Sign files, hashes and messages. Use the protocol to verify those signatures for free.

## Multisig
Multiple VerusIDs can have spending or signing ability of one VerusID. This means that multiple organizations or people can manage a VerusID.

## Messages
Send private messages to VerusIDs. 