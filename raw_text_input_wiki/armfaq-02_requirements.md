# Hardware and Software requirement for ARM.
There are minimum requirements on your hardware and software for running a Verus Wallet on ARM-devices. If your platform does not meet the minimum requirements, you may not be able to run the required software.

The listed requirements are for running **one** chain. Additional PBaaS chains require more resources.

## Verus Wallet on CLI

#### Absolute minimum requirements:
* 64-bit processor
* 64-bit Operating system (Raspbian is standard 32 bit)
* 2 GB memory + 6 GB Swap available to the CLI Wallet
* 20 GB storage space for Verus Blockchain and CLI wallet
* internet connectivity
* `libgomp1` and `zlib1g-dev` libraries installed

#### Recommended requirements
* 64-bit processor with AES functions enabled
* 64-bit Operation system (Raspbian is standard 32 bit)
* 4 GB memory or more + 6 GB Swap available to the CLI Wallet
* 50 GB storage on a *fast* medium (like NVMe device) for the Verus Blockchain & CLI wallet. This supplies room for blockchain growth over time and the ability to bootstrap the wallet.
* internet connectivity
* `libgomp1` and `zlib1g-dev` libraries installed

## Verus Wallet on GUI
#### Absolute minimum requirements:
* 64-bit processor
* 64-bit Operating system (Raspbian is standard 32 bit) with GUI interface
* 2 GB memory + 8 GB Swap available to the Verus Desktop Wallet
* 25 GB storage space for Verus Blockchain and Verus Desktop.
* internet connectivity
* `libgomp1` and `zlib1g-dev` libraries installed


#### Recommended requirements
* 64-bit processor with AES functions enabled
* 64-bit Operation system (Raspbian is standard 32 bit) ) with GUI interface
* 8 GB memory or more + 6 GB Swap available to the CLI Wallet
* 50 GB storage on a *fast* medium (like NVMe device) for the Verus Blockchain & CLI wallet. This supplies room for blockchain growth over time and the ability to bootstrap the wallet.
* internet connectivity
* `libgomp1` and `zlib1g-dev` libraries installed

## Staking
#### Absolute minimum requirements:
* All requirements to run a wallet

#### Recommended requirements
* All requirements to run a wallet
* A fully configured and functioning NTP client, to keep your clock synchronized
* Low latency internet connectivity

## Solo Mining
#### Absolute minimum requirements:
* All requirements to run a wallet

#### Recommended requirements
* All requirements to run a wallet
* 64-bit processor with AES functions enabled
* Low latency internet connectivity

## Pool Mining
* 64-bit processor with AES functions enabled
* 64-bit Operation system (Raspbian is standard 32 bit)
* ARM release of CCMiner or NHEQminer
* Low latency internet connectivity
* A public address to mine to
* A public mining pool to connect to

Note: Revision date 2023-01-12.
