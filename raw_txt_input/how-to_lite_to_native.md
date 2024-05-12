# Guide to change Verus-Desktop from Lite Mode to Native Mode.

Attention: Read completely before use.

#### Important General Information

### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

#### Necessary files & links:

Link 1: [Download Verus Bootstrap](https://bootstrap.verus.io)
Link 2: [Import Lite wallet address in Verus Desktop native](https://wiki.verus.io/#!how-to/how-to_convert-seed-to-wif.md)
Link 3: [Checking the signature](https://verus.io/verify-signatures)

## Procedure:
1. Make sure you have your seed phrase and password you use to log into your Lite mode wallet available.
2. First of all make a notition of your address and balance of VRSC you have in your wallet, before closing Verus Desktop.
3. Make sure the latest version of Verus-Desktop is installed.
 1. Download the latest Verus-Desktop.
 2. Verify the signature of your download, so you have an untampered installer. [Link 3](https://verus.io/verify-signatures) or [Video](https://youtu.be/sFUnKCnHx98)
 3. Run the file you just downloaded to install it.
4. Getting Verus-Desktop ready for Native mode:
	1. Start Verus-Desktop and enter your profile (if not loaded automatically).
  2. If present in your profile, `deactivate` Verus Lite.
  3. Click `+ Add Coin`, select **Verus** from the dropdown list and continue.
  4. Select **Native**, tick the option `bootstrap` and optionally tick the options `Start staking`, `Start Mining` and fill in the amount of threads to mine with.
  5. Click `Add Coin`. Verus-Desktop will add Verus as Native chain to your screens.
	6. You may get a red warning message about Zcash params. (Verus Desktop will detect if you have the necessary ZCash parameter files and download them if needed)
	7. As soon as the download is finished, Verus-Desktop will continue and bring you into your wallet. It will automatically start to synchronize the blockchain. Since we already put the majority of the chain in place, this will take just a few minutes.
6. Importing your existing Address:
	* This procedure is described in detail in: [Import Lite wallet address in Verus Desktop native](https://wiki.verus.io/#!how-to/how-to_convert-seed-to-wif.md).

If you followed these steps, installed the bootstrap, switched from Lite to Native mode and imported your existing address into Verus-Desktop. You can now stake your balance and use Private (sapling) addresses.

Created by Oink.vrsc@

Note: last revision date 2023-06-03.
