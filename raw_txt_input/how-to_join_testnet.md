# How-To Join VRSC testnet.

Attention: Read it completely before using.

#### Important General Information

`VRSCTEST data location`:
Linux GUI: `~/.komodo/VRSCTEST`
Mac OS: `/Users//Library/Application Support/Komodo/VRSCTEST`
Windows 10: `%AppData%\Roaming\Komodo\VRSCTEST\`

#### General remarks on CLI wallet:

On Windows command line enter the commands as shown without the surrounding quotation marks
In Linux shell preceed the commands without surrounding quotation marks with `./`
In MacOS shell preceed the commands without surrounding quotation marks with `./`
Example: the windows version `verus listtransactions` transforms in Linux or MacOS to `./verus listtransactions`.

#### General remarks on Windows command line formatting:

The CLI help shows the command format for Linux and MacOS.
For windows substitute the shown `'`-character with the `"`-character.
For windows substitute the shown `"`-character with the `\"`-characters.

### Necessary files:

Link 1: [Download latest Wallet](https://verus.io/wallet.html)

## Procedure:

Joining Verus testnet to test the latest capabilities before they are released to mainnet or simply test if your goals are possible without spending VRSC (testnet coins hold no value) is easy.

### Download a wallet

The first thing you need is a VRSC wallet. The CLI-wallet and Verus Desktop GUI wallet are available on the link above for Windows,
Linux and MacOS. If you already have a wallet verify that the wallet is the most recent version and update if needed.

### Verus Desktop Wallet ###

1. Start your Verus Desktop wallet.
2. If you have never run Verus testnet on your system before:
  1. Go to `settings` (cogwheel icon) and select `General Settings`.
  2. Select `Enable VRSCTEST`.
  3. Click `Save Changes`
  4. Restart Verus desktop
3. When logged in, click `Add Coin`, select `Verus Testnet` and click `Continue`.
4. Select the startup parameters you desire (Native (Lite mode is not available on testnet), Staking, mining (specify number of threads), reindex blockchain and/or rescan wallet) and click `Add Coin`.


**CLI wallet**
1. start CLI walletdaemon using these parameters:
   `verusd -chain=VRSCTEST`  
   Any extra parameter that you are used to for VRSC (like `-mint` or `-pubkey=`) can be appended as well.
2. commands through the CLI are in the following format:
   `verus -chain=VRSCTEST`  
   The only difference with the normal VRSC chain is the `-chain=VRSCTEST` option, that is added.



Created by Oink.vrsc@, inspired by 0x03.vrsc@.

Note: revision date 2020-11-11.
