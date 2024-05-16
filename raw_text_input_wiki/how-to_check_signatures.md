# Guide to verify a new wallet download.

Attention: Read it completely before using.

## Important General Information
Wallet download page: [https://verus.io/wallet](https://verus.io/wallet)

## Using Verus-Desktop

1. download the new version
2. extract the archive
3. verify the signature using the data in the `*.signature.txt`-file through your existing Verus-Desktop, *VerusID* tab, Verify Signed Data and choose to verify a file. Only continue when this verification returns True.
4. stop your Verus-Desktop wallet
5. install the verified installer (Windows).
6. start your wallet.

## Using CLI Wallet


1. download the new version
2. extract the archive
3. verify the signature using the data in the `*.signature.txt`-file with the command `./verus verifyfile "address or identity" "signature" "filepath/filename"` command. Only continue when this verification returns True.
4. stop your verusdaemon verus stop
5. extract the verified archive to your current CLI-wallet location
6. start your wallet (verusd)

Compiled by: Oink@

Note: creation date 2020-11-11.
