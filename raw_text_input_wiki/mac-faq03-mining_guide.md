# Start mining on MacOS.

Attention: Read it completely before use.

`VRSC Wallet and Data location` on Mac OS: `/Users//Library/Application Support/Komodo/VRSC`

### Software needed to mine

Prerequisite: [VerusCoin wallets](https://verus.io/wallet.html)
Needed: [VerusCoin miners](https://verus.io/getVRSC.html)

## Prerequisites:

To start mining with your Mac, you will need to have an address to mine to. Possibilities are:

~~An exchange address~~ (__***NOT***__ recommended. This is asking for trouble.)
An address from a web-wallet
An address from a mobile wallet
An address from a Verus-Desktop Lite wallet
An address from a Verus-Desktop Native wallet

## Procedure:

To start mining on your Mac, you should already have a wallet and and access to an address to mine to. Now to start mining we will need to download the miner first:
  1. Go to the `Veruscoin miners` link above and download `CLI nheqminer` for MacOS.
  2. Open the download folder in finder.
  3. doubleclick `nheqminer-MacOS-v0.8.0.tar.gz` to unpack it in your download folder.
  4. Open the `nheqminer` folder that appeared in your download folder

Now we need to configure things so the miner connects to a mining pool (listed on the download page, below the miner download) and mines to your address. In the instructions below I will use the VerusCoin community pool and the address for the Veruscoin foundation. make sure to use your own address and if desired the details of a different pool:
  5. click `start.sh` and open with `TextEdit.app`
  6. On the 2nd line, change `PoolHost=` into `Poolhost=pool.verus.io`
  7. On the 3rd line, change `Port=` into 'Port=9999'
  8. On the 4th line, change 'PublicVerusCoinAddress=' into `PublicVerusCoinAddress=RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ`
        (make sure you use your own address!!!!)
  9. On the 5th line, change `WorkerName=` into `WorkerName=MacOS` (or any name you want to identify your system)

In the next step we will set how many processor threads the miner will use. Make sure to use less threads than your processor has virtual cores. If you allow the miner to use all cores, your system will become sluggish at times, or it may even become completely unresponsive:
 10) On the 6th line, change `Threads=` into `Threads=7` (fill in the amount of virtual cores you want to use)
 11) Save and exit the file.

We have all the settings ready to go, but the file we just edited is not executable right now.
 12. Click `Start.sh` and click `copy "Start.sh"`
 13. Click in an empty space in you folder and click `Paste items`, which will result in a new `start copy.sh` file.
 14. rename `start copy.sh` to `start.command`
Now we have an executable file that will run when you doubleclick.
 15. Doubleclick `start.command` and your machine will start mining.

Created by Oink.vrsc@.

Note: last revision date 2020-02-26.
