# How to import your Lite wallet address into your native Verus Desktop?

Attention: Read it completely before using.

### Important General Information

`verus command "<userinput>"` needs to be entered literally, with `<userinput>` replaced by your specific userdata. So if the text directs you to use for example `"<Public Address>"`, you replace that (including the `<` and `>`) with the address,
so it looks similar to this: `"RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r"`.

This method is confirmed to work on Verus and all Komodo assetchains.

## Prerequisites

In order to convert your seedphrase into a Private key (WIF), you need to have a running native wallet first, that is fully synchronized. The earliest wallet that supports these functions is **Verus Desktop v0.6.4-beta-1**.

If needed, use this guide to quickly synchronize your wallet: https://wiki.verus.io/#!how-to/how-to_bootstrap.md

## Converting Seed to WIF
If you have a seed, you can retrieve your Private key (WIF) by having the Verus Desktop wallet convert it for you.
To convert your *seed phrase* in Verus Desktop, go to `settings` --> `Coin Settings`, select the chain you want to use in the top-right corner and enter the following command:
```
run convertpassphrase "word_1 word_2 word_3 ... word_n"
```

Note: Make sure you replace `Word1 word2 word3 ... word_n` with the actual seedphrase (12 or 24 words) of the address you want to import!

You will receive a response __similar__ to this:
```
{
"walletpassphrase": "seedphrase",
"address": "RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r",
"pubkey": "02ffc2f4b071afdec631e3fb7d435a0047be14a81ea1a269e4206b0068c0c1fa6f",
"privkey": "d899ed88e9ee2e90c2cf51cb47e7b4495ec1e1cb10763bb1c111b0bde48bf86c",
"wif": "UwGb5KvGPfMUr1tu74Desjh87ZeJM4wq5goLyThcogeLifc5aJqT"
}
```
Copy that information and store it somewhere **SAFE**. With this information anyone having access to it will have full control over that address.

The 52-character string after **"wif":** that is shown, is what you want to import in the next step.


## Importing a single WIF for a public (transparent) address
To import your address, go to `settings` --> `Coin Settings`, select the chain you want to use in the top-right corner and enter the following command:
```
run importprivkey "<wif>" "" true
```
Replace `<wif>` with the actual **wif** you got from the `convertpassphrase` command earlier.

Note: Don't use the WIF from the example above, but use the one from the CLI-interface in Verus Desktop.

Note: The GUI wallet will not show any progress on the import and may give messages that the RPC daemon is not reacting. It will take quite some time for the process to finish in the background, especially if the address has many transaction on it.

## Importing multiple WIFs in one batch for public (transparent) addresses
To import your address, go to `settings` --> `Coin Settings`, select the chain you want to use in the top-right corner and enter the following command for every WIF except for the final one:
```
run importprivkey "<wif>" "" false
```
Import the final WIF with this command:
```
run importprivkey "<wif>" "" true
```
The last command triggers the chain to rescan all addresses in your wallet, including all the addresses you just imported.
Replace `<wif>` with the actual **wif** (like the one you got from the `convertpassphrase` command earlier).

Note: Don't use the WIF from the example above, but use the one from the CLI-interface in Verus Desktop.

The GUI wallet will not show any progress on the import and may give messages that the RPC daemon is not reacting. It will take quite some time for the process to finish in the background, especially if the address has many transaction on it.

## Importing a single WIF for a private address
To import your address, go to `settings` --> `Coin Settings`, select the chain you want to use in the top-right corner and enter the following command:
```
run z_importkey "<wif>" "yes" 1
```
Replace `<wif>` with the actual **wif** you got from the `convertpassphrase` command earlier.

Note: Don't use the WIF from the example above, but use the one from the CLI-interface in Verus Desktop.

The GUI wallet will not show any progress on the import and may give messages that the RPC daemon is not reacting. It will take quite some time for the process to finish in the background, especially if the address has many transaction on it.

## Importing multiple WIFs in one batch for private addresses
To import your address, go to `settings` --> `Coin Settings`, select the chain you want to use in the top-right corner and enter the following command for every WIF except for the final one:
```
run z_importkey "<wif>" "no"
```
Import the final WIF with this command:
```
run z_importkey "<wif>" "yes" 1
```
The last command triggers the chain to rescan all addresses in your wallet, including all the addresses you just imported.
Replace `<wif>` with the actual **wif** (like the one you got from the `convertpassphrase` command earlier).

Note: Don't use the WIF from the example above, but use the one from the CLI-interface in Verus Desktop.

### The GUI wallet will not show any progress on the import and may give messages that the RPC daemon is not reacting. It will take quite some time for the process to finish in the background, especially if the address has many transaction on it.


Information compiled by Oink.vrsc@.

Note: revision date 2021-05-02.
