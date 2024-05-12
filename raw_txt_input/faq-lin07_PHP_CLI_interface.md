# PHP staking interface for coinshielding nodes.
Attention: Read it completely before using.

### Important General Information
`VRSC Wallet and Data location` on Linux: `~/.komodo/VRSC`

### Necessary files:
Link 1: [Download latest Wallet](https://verus.io/wallet)
Link 2: [Download Bootstrap](https://bootstrap.verus.io/)
Link 3: [Go to Verus-Staking-CLI](https://github.com/kbs1/verus-staking-cli)

## Procedure:
These tools will help you stake on your permanently running machine using Verus CLI, instead of running the Agama GUI wallet.

### Features
  automatic shielding and unshielding of coinbase (staking, solo mining)
  automatic tracking of total coins generated (also present in e-mail notifications)
  optional e-mail notifications on newly generated coins
  optional periodical wallet.dat backups, also as an encrypted ZIP archive
  optional periodical wallet balance e-mail notifications

Initial Verus daemon configuration
  Follow the guide in link 3 above to set-up your daemon for the first time. You will need a transparent address, a zs address  and the daemon running with correct parameters (`-mint -cheatcatcher=zs...`).

  Do not stake with the same `wallet.dat` on multiple nodes.

Submitted by @kbs1

Note: last revision date 2020-11-11.
