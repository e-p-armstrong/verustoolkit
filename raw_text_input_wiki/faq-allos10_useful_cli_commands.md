# Useful Verus CLI commands.
Note: This list is by no means complete, it highlites only the most commonly used commands. A complete list of commands can be obtained by running `verus help`

### Important General Information

`verus command "<userinput>"` needs to be entered literally, with `<userinput>` replaced by your specific userdata. So if the text directs you to use for example `"<Public Address>"`, you replace that (including the `<` and `>`) with the address,
so it looks similar to this: `"RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r"`.

##### General remarks on CLI wallet:
On Windows command line enter the commands as shown without the surrounding quotation marks
In Linux shell preceed the commands without surrounding quotation marks with ./
In MacOS shell preceed the commands without surrounding quotation marks with ./
for example the windows version verus listtransactions transforms in Linux or MacOS to ./verus listtransactions.

#####General remarks on Windows command line formatting:
The CLI help shows the command format for Linux and MacOS.
For windows substitute the shown '-character with the "-character.
For windows substitute the shown "-character with the \"-characters.

## Handy verus-cli commands:
Getting a new Public address:
`verus getnewaddress`

Listing your available public addresses:
`verus listaddressgroupings`

Getting a new Private address:
`verus z_getnewaddress`

Listing your available private addresses:
`verus z_listaddresses`

Importing a VRSC private key of a R-address into your wallet:
`verus importprivkey "<PRIVATE_KEY>"`

Importing a VRSC private key of a z-address into your wallet:
`verus z_importkey "<PRIVATE_KEY>"`

Getting your current VRSC balance:
`verus getbalance`

or for somewhat more information:
`verus z_gettotalbalance`

or for any specific address:
`verus z_getbalance "<z-, i- or P-ADDRESS>"`

get info about your wallet, (immature & staking) balances:
`verus getwalletinfo`

Sending VRSC coins from your verus wallet to and another VRSC address (only public address in this case, seperate command for z-addresses I think):
`verus sendtoaddress "<VRSC_address>" <AMOUNT> "<Some comments here>"`

Listing the latest VRSC transactions:
`verus listtransactions`

Shield reward coins from all public addresses:
`verus z_shieldcoinbase "*" "<z-ADDRESS>"`

Transfer X VRSX from any (P-, i- and z-) address to any (P-, i- and z-) address:
`verus z_sendmany "<z-, i- or P-ADDRESS>" '[{"amount":<X>, "address":"<Z-, i- or P-ADDRESS>"}]'`

Check the Operation Status of your z_sendmany command (or z_shieldconbase):
`verus z_getoperationstatus`

Disclaimer: Always read up before using a verus-cli command, more info on each command can be found using the following:
`verus help`

Added by @Crupti, @Oliver Westbrook and Oink.vrsc@
note: last revision date 2020-05-09.
