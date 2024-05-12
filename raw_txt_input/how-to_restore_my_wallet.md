# How-To: Restore my wallet from a backup?

## Important General Information

### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

`verus command "<userinput>"` needs to be entered literally, with `<userinput>` replaced by your specific userdata. So if the text directs you to use for example `"<Public Address>"`, you replace that (including the `<` and `>`) with the address,
so it looks similar to this: `"RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r"`.

### Instruction Video
External YouTube link: [Restoring the Verus Desktop wallet](https://youtu.be/EO6EdPY32Rk)

## Procedure
### Using a backup of your `wallet.dat`.

1. Stop verusd. For Windows-Desktop or Agama, just exit and wait for it to close completely. For the linux cli run `./verus stop`, or for the windows cli run `verus stop`.
2. Once your wallet is finished closing copy the backup of your `wallet.dat` file from your backup location to the directory listed in the start of this document (see above).
3. Now restart your wallet by launching Verus Desktop, Agama or running verusd for the CLI.

### Using a `walletexport` file.

Note: The filename you replace`<mywalletimport>` with, can only contain letters and figures, no other characters, so it **cannot** have an file-extension

Attention: The command `z_importwallet` triggers the wallet to rescan in order to make all transactions to the freshly imported wallet addresses visible.
Rescanning your wallet may take a considerable time, during which your wallet may not respond to other commands. Please be patient.

The `<PATH>` in the `z_importwallet` command needs to be the **full absolute** path to the file. replace `LOGINNAME` with the actual loginname.

#### Verus Desktop:
   Go to `Settings`, `Coin Settings` and click `Import native wallet backup`.
   Click `Choose file`, browse to your backup file, select it and click `Open`
   Click `Import` to start the inport process
#### Agama:
   Go to settings, scroll to the bottom and click CLI, select VRSC in that section.
   Then below type `z_importwallet "<PATH><mywalletimport>"` and click the button below to run it.
#### linux/MacOS CLI:
   run `./verus z_importwallet "<PATH><mywalletimport>"`
#### Windows CLI:
   run `verus z_importwallet \"<PATH><mywalletimport>\"`

### Using individual seeds / WIF-keys
Importing individual keys is explained in detail in this wiki: [import your Lite wallet address into your native Verus Desktop](#!how-to/how-to_convert-seed-to-wif.md).

Information compiled by Oink.vrsc@.

Note: revision date 2022-09-12.
