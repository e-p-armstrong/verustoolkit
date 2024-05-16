# Question: I accidentally send funds to my b-address and cannot move those funds

Funds sent to a b-address get locked in the same manner as the original coinbase reward was. However, because they were not sent using a script to lock those coins, they can be retrieved, without waiting the full unlock period (typically between 3 and 27 months).

Warning: DO NOT send to a b-address, unless you kow what you're doing.

## procedure

### First you need to determine the **TXID** of the locked funds.

1. The easiest way is to obtain the TXID from the send transaction you did in Verus-Desktop to the b-address. Make a copy of the TXID: you will need it for this procedure
2. The next easiest way is look up the b-address on the [explorer](https://explorer.verus.io) and examine the transactions to this address. The youngest transaction is usually the one you need. On the explorer the hash in the transaction is the TXID. Make a copy of the TXID: you will need it for this procedure
3. In Verus Desktop, go to `Settings` --> `Coin Settings` and make sure `VRSC` is selected in the top right. Run the command:
```bash
run listunspent 0 <BLOCKCOUNT> '["<YOUR-b-ADDRESS"]'
```
 Replace `<BLOCKCOUNT>` with the current blockcount your wallet is on.
 Replace `<YOUR-b-ADDRESS` with the actual b-address where the coins are.
 You will receive a result similar to this:
 ```json
 [{
"txid": "fa5962ebf61ef31867ba73b173433841f8f68578d53b4bb30cfe1432b5820f15",
"vout": 10,
"generated": false,
"address": "iBSUZSgXHEGGz65GTT6BGgchtkTHoFBs57",
"amount": 2.20005763,
"interest": 0,
"scriptPubKey": "050403000000cc1b04030001011504575dc6ae7484c83c0dc97a4218f88e2cbe9b659c75",
"confirmations": 159,
"spendable": true
}]
```
Make a copy of the TXID: you will need it for this procedure

note: The above result is an example. ***DO NOT*** use data from it.

### Now we need to create a raw transaction

To create a raw transaction, we will need to use the CLI-interface. In Verus Desktop
`run createrawtransaction '[{"txid": "yourtxid here", "vout": fill in too}]' "{"destination addr": <amount>}" <current Blockheight -5>`

1. adapt the above `createrawtransaction` command, making sure to subtract the 0.0001 VRSC free from the amount that is in the original TXID, similar to this example:
```bash
run createrawtransaction '[{"txid": "fa5962ebf61ef31867ba73b173433841f8f68578d53b4bb30cfe1432b5820f15", "vout": 10}]' '{"Oink@": 2.20004763}' 890450
```
In this example, the result is a long HEX-string:
```json
0400008085202f8901150f82b53214fe0cb34b3bd57885f6f841384373b173ba6718f31ef6eb6259fa0a00000000feffffff019b011d0d0000000024050403000000cc1b04030001011504575dc6ae7484c83c0dc97a4218f88e2cbe9b659c7552960d006e960d000000000000000000000000
```
Copy the string that your command gave as response, from the CLI interface of your wallet. You will need it in the next step.

note: The above command and its result are examples. ***DO NOT*** use data from it. Use the results from your own wallet!

2. In the CLI interface adapt and issue this command`run signrawtransaction <string from step 1>`
In our example, that would look like this:
```bash
run signrawtransaction 0400008085202f8901150f82b53214fe0cb34b3bd57885f6f841384373b173ba6718f31ef6eb6259fa0a00000000feffffff019b011d0d0000000024050403000000cc1b04030001011504575dc6ae7484c83c0dc97a4218f88e2cbe9b659c7552960d006e960d000000000000000000000000
```
and your command will show a result similar to this example:
```json
{
"hex": "0400008085202f8901150f82b53214fe0cb34b3bd57885f6f841384373b173ba6718f31ef6eb6259fa0a000000694c67010101012102c9ca37dac14c819a99ce4a71533ab8d3d5e37643ede9c4da0981081a074f75df40531ea63fb3de6111949652111bbe524506999c97c06302715e85aa5c5813519b3eace4ac15bb3950600f968c0c555a935fd826f1a51e00bd2a7f12d035757fc5feffffff019b011d0d0000000024050403000000cc1b04030001011504575dc6ae7484c83c0dc97a4218f88e2cbe9b659c7552960d006e960d000000000000000000000000",
"complete": true
}
```

note: The above command and its result are examples. ***DO NOT*** use data from it. Use the results from your own wallet!

3. In the CLI interface adapt and issue this command `sendrawtransaction <"hex"-string from step 2>`.
In our example that would look like this:
```bash
run sendrawtransaction 0400008085202f8901150f82b53214fe0cb34b3bd57885f6f841384373b173ba6718f31ef6eb6259fa0a000000694c67010101012102c9ca37dac14c819a99ce4a71533ab8d3d5e37643ede9c4da0981081a074f75df40531ea63fb3de6111949652111bbe524506999c97c06302715e85aa5c5813519b3eace4ac15bb3950600f968c0c555a935fd826f1a51e00bd2a7f12d035757fc5feffffff019b011d0d0000000024050403000000cc1b04030001011504575dc6ae7484c83c0dc97a4218f88e2cbe9b659c7552960d006e960d000000000000000000000000
```
and your command will show a result similar to this example:
```json
4a5202327e6ed2ce20d3b146155ec92e52fae6c4481362faf6f8a072017b41f1
```
The result of this command is the TXID of the coins moving out of your b-address. You can monitor the progress in your wallet or look up the TXID in the [explorer](https://explorer.verus.io).

note: The above command and its result are examples. ***DO NOT*** use data from it. Use the results from your own wallet!

Some words of advice after succesfully removing funds locked in a b-address:
* Pay attention to which addresses you send.
* It may be an idea to import the addresses you use into a fresh wallet, omitting all unused (b-) addresses.

note: Created 2020-11-11 by Oink.vrsc@
