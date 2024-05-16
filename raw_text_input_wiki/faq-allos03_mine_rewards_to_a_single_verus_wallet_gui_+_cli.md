
# Question: How do I direct all my solo mined rewards to a single Verus wallet?

Attention: Read it completely before using.

## Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

## Prerequisites
* Have a __native__ VRSC wallet running

## In Verus Desktop
In Verus Desktop, there is at this moment no way to enter an address to mine to. However, editing the `VRSC.conf` can be done to achive our goal:
* In the receive window of your wallet, click the hamburger (three vertical dots) next to the address you want to receive your rewards in and click `Copy Public Key`.
* Close down Verus Desktop.
* Edit `VRSC.conf`(see standard locations at the top) and add the line `pubkey=THELONGSTRINGCOPIED`.
* Save and exit.
* Start Verus Desktop as you normally do.

## In Agama Wallet
Step 1 - First get your wallet address you want to mine to:
* If you don't have an address, click "Receive", click "Get New Address" and choose "Transparent Address" from the drop down.

Step 2 - Next we need to retrieve our pubkey,
* click on the hamburg next to the address that you want to receive the rewards in and click `copy pubkey`

Step 3 - Set your PubKey
* Go to 'Settings', 'App Config (config.json)' and enter your pubkey(THELONGSTRINGCOPIED) into the 'Pubkey VRSC mining key' field.
* Click 'Save app config' to save these settings.
* Restart Agama

## In Verus CLI
Step 1 - First get your wallet address you want to mine to:
You can find an address if you already have previous transactions, or you can create a new one.  To find an address from a previous transaction, use the command line verus listtransactions and copy the address found after "address".
To generate a new wallet address, use the command line `verus getnewaddress` and a new address will be created.

Step 2 - Next, using your new address, enter the command with verus-cli `verus validateaddress`. From the output find the long string after "pubkey", copy without the quotation marks.

Step 3 - Set your PubKey
* Option 1: use this pubkey when starting your daemon by adding the following line to the end of your command, just before the "&" sign: -pubkey=THELONGSTRINGCOPIED
* Option 2: edit your `VRSC.conf` and add the line `pubkey=THELONGSTRINGCOPIED`. Then start your whallet as you are used to.

Your rewards will now be mined to that address.  It would be a good idea to keep notes and associate the wallet address with the pubkey...also to double check that you did validate the correct pubkey for the wallet address, making sure you made no errors.

(submitted by @Oliver Westbrook, edited by Oink.vrsc@)

note: last revision date 2020-02-24.
