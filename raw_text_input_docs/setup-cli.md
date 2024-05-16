# Setup verus-cli

### [Download verus-cli for Windows, macOS and Linux](https://verus.io/wallet/)

The CLI (command-line-interface) wallet is an alternative to Verus Desktop, and is used through the terminal.

In the packaged file you find ``verusd``, ``verus``, ``fetch-bootstrap``, ``fetch-params`` and accompanying text files to [verify](https://verus.io/signatures) signatures. 

Run ``verusd`` to start the blockchain. The ``d`` stands for daemon. A daemon is a program that runs as a background process. 

Run ``verus`` to interact with the blockchain. 

::: warning New System 
Run ``fetch-params`` before using ``verusd`` when you are running a new system. It downloads the zcash parameters needed to get started.
:::

::: tip Bootstrap Blockchain
Downloading the blockchain can take up a long time, to speed it up you can bootstrap the blockchain. Run ``fetch-bootstrap``.
:::

Extract the packaged file on your computer, preferably where you can find it back easily. 

## Use Commands
In your terminal, go into the directory where you extracted verus-cli.

### Start Verus Blockchain

``` 
./verusd
```

### Start Testnet Blockchain
``` 
./verusd -chain=VRSCTEST
```