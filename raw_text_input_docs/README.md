# Introduction
In Verus, there are two kinds of addresses: **public** and **private**. This doc guides you through understanding these address types and how they're involved in transactions.

Understanding the distinctions between public and private addresses in the Verus ecosystem is crucial for making informed decisions about transaction privacy. 

## Public addresses
You can use the following public address types to send and receive funds.

| Address type | Details | 
| :-----| :------ | 
| **R-address** | A R-address is a public cryptocurrency address derived from a private key. The private key is essential for accessing and controlling the R-address.| 
| [**VerusID@**](/verusid/) | A VerusID is a public friendly-name cryptocurrency address. It is controlled by a primary address, which is a R-address.| 
| **i-address** | An i-address is a public cryptocurrency address derived from a VerusID.| 

Public addresses and their transactions are visible on blockchain explorers because they're recorded on the public ledger, unlike private z-addresses.

## Private addresses
You can use the following private address type for confidential exchange of funds and data.

| Address type | Details | 
| :-----| :------ | 
| **z-address** | A z-address is a private cryptocurrency address derived from a private key. The private key is essential for accessing and controlling the z-address. Only the person who has the private key can spend and see its balance. Or provide visibility in the balance through a ``viewing key``. | 

Balances and transactions associated with private addresses are confidential. They do not appear on the blockchain or any explorer.

ℹ️ A VerusID can contain a pointer to a z-address. You can then send coins to ``VerusID@:private``. 

::: warning Only native currencies
Z-addresses can only contain the native blockchain currency. Simple token currencies or basket currencies can **not** be held in a z-address.
:::

# Transaction scenarios

## Public-to-public
``VerusID@``, ``R-address``, or ``i-address`` ➡️ ``VerusID@``, ``R-address``, or ``i-address``

- Sender's address and the amount sent are visible 
- Recipient's address(es) and received amount(s) are visible
     
## Public-to-private
``VerusID@``, ``R-address``, or ``i-address`` ➡️ ``z-address`` or ``VerusID@:private``

- Sender's address and the amount sent are visible
- Recipient's address(es) and received amount(s) are **not** visible

*Note: Correlating transactions by time and amounts between public and private addresses is still possible, potentially linking two public addresses based on transaction patterns.*

## Private-to-public
``z-address`` ➡️ ``VerusID@``, ``R-address``, or ``i-address``

- Sender's address and the amount sent are **not** visible 
- Recipient's address(es) and received amount(s) are visible

*Note: Like public-to-private transactions, there remains a possibility of correlating transactions based on timing and value, potentially linking two public addresses.*

## Private-to-private
``z-address`` ➡️ ``z-address`` or ``VerusID@:private``

- Sender's address and the amount sent are **not** visible 
- Recipient's address(es) and received amount(s) are **not** visible