
# Standard file location for Verus Desktop

The installer for Verus-Desktop suggests a standard location to install to Applications

## Anyone who uses the computer

`/Applications/Verus-Desktop.app`

## Deamons

The daemons are located in the `komodod`, `verusd` and `zcashd` folders that can be found in
`/Applications/Verus-Desktop.app/Contents/Resources/app/assets/bin/osx`

## Program settings

Verus Desktop saves its program settings in your home folder:
`~/Library/Application\ Support/Verus-Desktop`
The users settings are stored in `appdata/config.json` in the program settings folder.

## Standard chain data and wallet locations

Verus Desktop saves its chain and wallet data in your home folder:
#### KMD

`~/Library/Application\ Support/Komodo`

### Verus

`~/Library/Application\ Support/Komodo/VRSC`

#### Komodo asset chains
Any Komodo asset chain will create a subfolder in the KMD chain data and wallet folder, which is standard named. The names will be in capitals and are identical to the **official** asset-chain name.
`~/Library/Application\ Support/Komodo/<CHAIN-NAME>`

Note: examples
Pirate: `~/Library/Application\ Support/Komodo/PIRATE`
Utrum: `~/Library/Application\ Support/Komodo/OOT`
Zexo: `~/Library/Application\ Support/Komodo/ZEXO`
And so on...

For easy access to the binaries folders, Verus-Desktop program settings and VRSC chain folder and all binary folders, you can use the help menu in Verus-Desktop.

note: created at 2020-12-03 by Oink.vrsc@
