
# Standard file location for Verus Desktop

The Linux version of Verus Desktop is supplied as an AppImage, so it does not get installed, but mounted in the `/tmp` folder on execution.
The folder it is mounted to will look like `.mount_Verus-xxxxx` where the `xxxxx` part will be a random set of characters, changing on every start of the wallet.
(It is a hidden folder: in order to see it, `<CTRL>-H` will toggle the display of hidden folders)

Normally you don't need to worry about these locations, but in some instances you will be asked by community members providing support to look up a file in a folder in your Verus-Desktop installation.

note: changing files in these folders or subfolders may result in a corrupt installation. Only do so when instructed by our support community members.

## Deamons

The daemons are located in the `komodod`, `verusd` and `zcashd` folders that can be found in the
`resources/app/assets/bin/linux64` subfolder of your (mounted) program folder.

## Program settings

Verus Desktop saves it program settings on a different folder:
`~/.verus-desktop`
The users settings are stored in `appdata/config.json` in the program settings folder.

## Standard chain data and wallet locations

#### KMD

`~/.komodo`

### Verus

`~/.komodo/VRSC`

#### Komodo asset chains
Any Komodo asset chain will create a subfolder in the KMD chain data and wallet folder, which is standard named. The names will be in capitals and are identical to the **official** asset-chain name.
`~/.komodo/<CHAIN-NAME>`

Note: examples
Pirate: `~/.komodo/PIRATE`
Utrum: `~/.komodo/OOT`
Zexo: `~/.komodo/ZEXO`
And so on...

For easy access to the binaries folders, Verus-Desktop program settings and VRSC chain folder and all binary folders, you can use the debug menu in Verus-Desktop.

note: created at 2020-12-03 by Oink.vrsc@
