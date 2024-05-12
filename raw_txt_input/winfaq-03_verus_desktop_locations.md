
# Standard file location for Verus Desktop

The installer for Verus-Desktop suggests a standard location to install to, depending on the choice whether you want to install it for all users or just yourself.

## Anyone who uses the computer (All Users)

`%ProgramFiles%\Verus-Desktop`

## Only me:

`%USERPROFILE%\AppData\Local\Programs\Verus-Desktop`

Normally you don't need to worry about these locations, but in some instances you will be asked by community members providing support to look up a file in a folder in your Verus-Desktop installation.

note: changing files in these folders or subfolders may result in a corrupt installation. Only do so when instructed by our support community members.

## Deamons

The daemons are located in the `komodod`, `verusd` and `zcashd` folders that can be found in the
`resources\app\assets\bin\win64\` subfolder of your installation folder.

## Program settings

Verus Desktop saves it program settings on a different folder:
`%AppData%\Verus-Desktop`
The users settings are stored in `appdata\config.json` in the program settings folder.

## Standard chain data and wallet locations

#### KMD

`%AppData%\Komodo`

### Verus

`%AppData%\Komodo\VRSC`

#### Komodo asset chains
Any Komodo asset chain will create a subfolder in the KMD chain data and wallet folder, which is standard named. The names will be in capitals and are identical to the **official** asset-chain name.
`%AppData%\Komodo\<CHAIN-NAME>`

Note: examples
Pirate: `%AppData%\Komodo\PIRATE`
Utrum: `%AppData%\Komodo\OOT`
Zexo: `%AppData%\Komodo\ZEXO`
And so on...

For easy access to the binaries folders, Verus-Desktop program settings and VRSC chain folder and all binary folders, you can use the debug menu in Verus-Desktop.

note: updated at 2020-12-03 by Oink.vrsc@
