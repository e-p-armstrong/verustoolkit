# Question: How to consolidate multiple `wallet.dat` files in one?

Attention: Read it completely before using.

### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

## Procedure

1. With one of the wallets loaded, issue the following command: `z_exportwallet FILENAME` (ie z_exportwallet export_instance01, the filename cannot have a `.` in it.)
2. Copy the generated file to the machine that hosts your main wallet. This file will either be in the same directory as the config file and wallet.dat file, or in a location specified by exportdir in VRSC.conf.
3. Issue the following command (on the "main" verus-cli): `z_importwallet /LOCAL_PATH/EXPORTFILENAME` (ie /home/user/export_instance01)

note: Older versions of verusd required `expordir` to be set in VRSC.conf before exporting a wallet. If you get an error about your export directory not being set, please upgrade immediately.

#### These commands can be given in:

* CLI wallet: `./verus z_exportwallet FILENAME`& `./verus z_importwallet /LOCAL_PATH/FILENAME`
* Verus Desktop in `settings`, `coin settings`: `run z_exportwallet FILENAME`& `run z_importwallet /LOCAL_PATH/FILENAME`
* Verus Agama in `settings`, `<CLI>`: `z_exportwallet FILENAME`& `z_importwallet /LOCAL_PATH/FILENAME`

(submitted by @TexWiller, revised by @englal)

note: last revision date 2020-09-30.
