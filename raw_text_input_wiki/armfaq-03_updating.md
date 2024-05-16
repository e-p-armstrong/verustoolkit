# Updating the ARM CLI wallet.

Attention: Read it completely before use.

## Necessary files:

Link 1: [Download latest Wallet](https://verus.io/wallet)

## Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * ARM Linux:		`~/.komodo/VRSC`

Note: Due to the size of the blockchain, on an ARM installation this directory is usually stored on a mounted external hard drive.
This will have its own file path that was specified when the drive was mounted.
Thus the path to `~/.komodo/VRSC` directory is likely to be user-specified & thus non-standard on an ARM.

---

(NB This version is aimed at inexperienced users, so it includes the associated routine/basic Linux commands.
You will need access to the relevant directories, which may require sudo priveleges)

(NB Raspberry Pi ARM boards lack some instruction sets to mine, though the Pi3 & Pi4 are ARM64 & can be used as staking devices if an ARM64 operating system is installed)

---

## Procedure:

1. Navigate to the directory which contains the verus daemon binary file (the default is in the home directory - ie ~/verus-cli)
        cd verus-cli
2. Check the Verus daemon is running - you will need to keep it running to check the downloaded file's signature
        top
    (`verusd` should appear as one of the processes in the list. If you need to start it use the command `./verusd`.)
3. Download the latest ARM64 version. Check https://verus.io/wallet/command-wallet
    (The commands below are for v0.7.3-10) Don't forget to change the version number to whichever one you are updating.
        wget https://github.com/VerusCoin/VerusCoin/releases/download/v0.7.3-10/Verus-CLI-Linux-v0.7.3-10-arm64.tgz
4. unpack/unzip the download into the signature file and the binaries tar/zipped file
        tar -xvf Verus-CLI-Linux-v0.7.3-10-arm64.tgz
5. Check it has unpacked/unzipped & open the signature file
        ls -la
        cat Verus-CLI-Linux-v0.7.3-3-arm64.tar.gz.signature.txt-file
    This will display the signature information to verify the downloaded file is authentic.

6. CHECK the signature by using the data in the signature file
        ./verus verifyfile "Verus Coin Foundation Releases@" "[signature string from signature.txt-file]" [your home directory file path]Verus-CLI-Linux-v0.7.3-10-arm64.tar.gz
    The return should be **`true`**. If you have an issue add "" around the file path.

7. STOP the Verus daemon
        ./verus stop
    Check whether it has stopped running with this command. (To be doubly sure you can also look in the debug file in the )
        top
    (This time `verusd` should **NOT** appear in this list.)
8. Rename the old versions of the binaries (replace the version numbers with the version being replaced)
    (This ensures you can easily revert to the old version by renaming these files.)
        mv verus verus-v0.7.3-9
        mv verusd verusd-v0.7.2-9
9. Check they have been renamed
        ls-la
10. Unpack/unzip the binaries for the latest version
        tar -xvf Verus-CLI-Linux-v0.7.3-10-arm64.tar.gz
11. Check if they have unpacked/unzipped in the directory
        ls -la
12. If the directory where your Verus wallet.dat, Chaindata & VRSC.conf files are stored is in a non standard place - eg on a mounted external hard drive - you may have a datadir specified in your VRSC.conf file.
    Navigate to that directory to check your datadir is still correct. The VRSC.conf file may have been overidden in the update. This ensures the Verus daemon knows where to find the blockchain you have currently saved on your system.
        cat VRSC.conf
    If it requires editing, use nano to edit this file
        nano VRSC.conf
    & append this to the VRSC.conf file :   
        datadir=[your custom file path for your mounted hard drive]
13. Start the Verus daemon again on the new version (add any other start options from https://wiki.verus.io/#!faq-cli/clifaq-01_verusd_options.md)
        ./verusd
14. Check the version
        ./ verus getwalletinfo
15. Once you are satisfied the new version is working, clean up the older binares (from step 8) by deleting them (or just move them to another directory using the same mv command as step 8)
        rm verus verus-v0.7.3-9
        rm verus verusd-v0.7.3-9

Information compiled by `Mercadinaut.vrsc@`.

Note: creation date 2021-05-16.
