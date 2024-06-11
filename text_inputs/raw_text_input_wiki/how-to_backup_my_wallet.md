# How-To: Backup my wallet?

## Important General Information

## Video:
Watch this video with an explanation how to accomplish the steps below: [Backup your wallet](https://youtu.be/ygPsdK8Trck)


### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

### Instruction Video
External YouTube link: [Backing up the Verus Desktop wallet](https://youtu.be/ygPsdK8Trck)

## Preferred method: Exporting your wallet

Note: The filename you replace`<mywalletexport>` with, can only contain letters and figures, no other characters, so it **cannot** have a file-extension!*

#### Verus Desktop:
  Go to `Settings`, `Coin Settings` and click `Export native wallet backup`.
  Confirm that you want to export after reading the pop-up.
  The green message will tell you where the backup is and what it's name is.
#### linux/MacOS CLI:
  run `./verus z_exportwallet "<mywalletexport>"`
#### windows CLI:
  run `verus z_exportwallet "<mywalletexport>"`

Attention: Pay attention to the feedback this command gives you: it will mention the location where the export file is saved.

The exported wallet should be a file called `<mywalletexport>`, standard in the same directory as your `wallet.dat`. Keep this file secure, it has your plaintext private keys. Verify that the file is there and isn't empty.

## Alternate method: Backing up your wallet

Note: The filename you replace`<DestinationFileName>` with, can only contain letters and figures, no other characters, so it **cannot** have an file-extension

#### Verus Desktop:
   Go to `Settings`, `Coin Settings` and click the text box
   type `run backupwallet "<DestinationFileName>"`
#### linux/MacOS CLI:
   run `./verus backupwallet "<DestinationFileName>"`
#### windows CLI:
   run `verus backupwallet "<DestinationFileName>"`

Attention: Pay attention to the feedback this command gives you: it will mention the location where the backup file is saved.

The backup wallet should be a file called `<DestinationFileName>`, standard in the same directory as your `wallet.dat`. Keep this file secure, it enables full access to all your addresses.
Verify that the file is present and that it is the same size as your `wallet.dat`.

## Extra info for **non-Verus** chains

#### Extra line in `<coin>.conf` required
**Non-Verus** chains like **Komodo** and its asset chains and **Zcash**, need this entry in the coins configuration file to specify the export directory, before you started your wallet.
`exportdir=<dir>`

#### For Komodo the base directory is `komodo`.
* Linux:		`~/.Komodo`
* Mac OS: 	`~/Library/Application Support/Komodo`
* Windows 10: 	`%AppData%\Roaming\Komodo`
For Komodo asset chains it is a folder/directory in the `komodo` base directory (eg `komodo/PIRATE`) with the **official** coin designation.

#### For Zcash the base directory is `zcash` instead of komodo.
* Linux:		`~/.Zcash`
* Mac OS: 	`~/Library/Application Support/Zcash`
* Windows 10: 	`%AppData%\Roaming\Zcash`

#### **non-Verus** chains Verus Desktop
* **before** executing the command in the `run ...` commands, select the appropriate coin in the top right corner.

Information compiled by Oink.vrsc@.

Note: revision date 2022-09-12.
