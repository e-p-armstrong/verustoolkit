# Guide to install Bootstrap for your Verus Wallet.

Attention: Read it completely before using.

## Important General Information

### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

Tip: The easiest way is to copy the location above and paste it into your address bar of your file browser. Your operation system will accept the input, interpret where that location is and bring you there.


## Verus-Desktop Procedure
1. In Verus-Desktop, exit your profile, by selecting the exit icon at ther top right.
2. Wait a minute or two, allowing the wallet to close completely in the background.
3. click `help`, `Bootstrap VRSC`. That opens up a new window.
4. Follow the instructions and when finished successfully, select your preferred profile and enter Verus Desktop.

## Verus CLI Procedure
1. Go to the folder where your daemon is extracted (standard `verus-cli`)
3. Shutdown `verusd` and wait for it to close completely
4. doubleclick `fetch-bootstrap` in your file browser.
5. Follow the instructions and when finished, start your `verusd` daemon as usual


## Optional:
Watch this video with an explanation how to accomplish the steps above: [Bootstrapping your wallet using the supplied script](https://youtu.be/xgLxzel5t04)


## Manual Bootstrap Procedure

### Necessary files:

Link 1: [Download latest Wallet](https://verus.io/wallet.html)
Link 2: [Download Verus Bootstrap](https://bootstrap.verus.io/)

### Procedure:
1. Make sure your wallet is not active.
2. If you already had you wallet running, backup essential files:
	a. Go to `VRSC Wallet location`
	b. copy `wallet.dat` to a *SAFE* location
	c. copy `VRSC.conf` to a *SAFE* location
	d. Verify that both files are copied to your safe location
3. Make sure the latest version of your Wallet for Verus is installed
	a. Download the latest Verus Wallet from link 1, supplied above.
	b. Verify the SHA256 checksum & signature of your download, to verify you have an untampered installer.
	c. extract the file you just downloaded to a suitable location.
	  On MacOS and Linux you will have extracted an **AppImage** which can be run directly. Windows users need to run the **installer**.
4. Installing the bootstrap:
  a. Download the bootstrap from Link 2.
  b. (Optional, but recommended) Verify the md5, sha256 or sha512 checksum and the signature of your download, to verify that you downloaded an untampered Bootstrap archive.
  c. Remove all files and folders from `VRSC Wallet Location` except `wallet.dat`, `debug.log`, `VRSC.conf` and if applicable `VRSC-bootstrap.*`.
  d. Extract the downloaded archive to `VRSC Wallet location`.  Make absolutely sure the folders `blocks` and `chainstate` are extracted into the correct folder. If the end up in a different folder (eg. `VRSC-bootstrap`-folder) move them to `VRSC Wallet location`.
5. If you had a VRSC wallet running before, restore essential files:
	a. Go to `VRSC Wallet location`
	b. Verify that your `wallet.dat` is bigger than the one in this folder (if any is present)
	c. copy `wallet.dat` from your *SAFE* location
6. Start your wallet

If you followed these steps, you will have installed/updated the latest version of a wallet for verus, made a backup of your wallet and installed the bootstrap. If desired you can remove the downloaded bootstrap archive to free up space on your hard drive.

### Optional:
Watch this video with an explanation how to accomplish the steps above: [Bootstrapping your wallet manually](https://youtu.be/ILr8vDgfPHI)


Information compiled by Oink.vrsc@.

Note: revision date 2024-04-07.
