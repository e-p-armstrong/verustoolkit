# What versions of OSX/macOS are supported?

## Verus Desktop

Currently only macOS 10.12.x and up are tested and supported for Verus Desktop. Installing Verus Desktop on OSX 10.11.x or earlier may be possible but the wallet does not function and never completes the initial sync.

## Verus CLI wallet

The CLI wallet should run on lower versions without problems.

## File location

`VRSC Wallet and Data location` on Mac OS: `/Users//Library/Application Support/Komodo/VRSC`

### Necessary files:

Link 1: [How-To install the latest Wallet](#!/how-to/how-to_bootstrap.md)

## Procedure:

If you installed on OSX 10.11.x or earlier and need to remove it:

1. Quit your Wallet.
2. Eject the wallet dmg.
3. Make a backup of `wallet.dat` & `VRSC.conf` if necessary (Only if you had a wallet on this machine or if you used an existing `wallet.dat`)
4. If you installed the `Agama.app` in Applications, move this to the trash.
5. Move `~/Library/Application Support/Agama` to the trash or use the following command in terminal
`rmdir /Users//Library/Application\ Support/Agama`.
6. Move `~/Library/Application Support/Komodo` to the trash or use the following command in terminal
`rmdir /Users//Library/Application\ Support/Komodo`.
7. Upgrade OS.
8. Install Agama (Check `Link1` for a smooth install)

(submitted by @bigtom, edited by Oink.vrsc@)

Note: last revision date 2020-02-26.
