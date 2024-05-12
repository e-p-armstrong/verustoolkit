# Shielding Verus Coin via the CLI.

Attention: Read it completely before use.

Note: Shielding is no longer required for coinbase rewards after block 800200. Earlier timelocked coins will still need to be shielded in order to use them.

### Important General Information

`verus command "<userinput>"` needs to be entered literally, with `<userinput>` replaced by your specific userdata. So if the text directs you to use for example `"<Public Address>"`, you replace that (including the `<` and `>`) with the address,
so it looks similar to this: `"RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r"`.

#### General remarks on CLI wallet:

On Windows command line enter the commands as shown without the surrounding quotation marks
In Linux shell preceed the commands without surrounding quotation marks with `./`
In MacOS shell preceed the commands without surrounding quotation marks with `./`
Example: the windows version `verus listtransactions` transforms in Linux or MacOS to `./verus listtransactions`.

#### General remarks on Windows command line formatting:

The CLI help shows the command format for Linux and MacOS.
For windows substitute the shown `'`-character with the `"`-character.
For windows substitute the shown `"`-character with the `\"`-characters.

## Procedure:

You must first "shield coins" (send from a transparent R-addr to a shielded zaddr) to be able to use them in staking, when they first unlock.
This is part of the Zcash protocol itself. The commands below assume you are in the Verus source code directory

  `verus z_shieldcoinbase`

You can either use an existing zaddr or use a new zaddr. To make a new zaddr:

  `verus z_getnewaddress`

Use the address the above command outputs in the `z_shieldcoinbase` command

To shield all coinbase in your wallet, you can use `"*"` (quotes are important) and zaddr that is getting the funds:

  `verus z_shieldcoinbase "*" <YOUR zs-ADDRESS>`

To just shield a single address, specify that as the first argument:

  `verus z_shieldcoinbase <YOUR R-ADDRESS> <YOUR zs-ADDRESS>`

Once the funds have moved to the zaddr and are confirmed, you can freely send them to any address, They will be eligble for staking id sent to a transpartent address (R-address).

To send from a certain zaddr to a transparent address, use z_sendmany. The following command sends 10 Verus to a given transparent address, ID address or ID-name.
Example: `verus z_sendmany zcZpfuzzJqmNJ3fUJekvbnyuxuJe9eAURAHrMCvN2Nr7VuWjakb1LEw6j2etPcCnr45BRot7MaMbipuS5da162BfuUkFGxx '[{"amount":10,"address":"Verus Coin Foundation@"}]'`


Note: revision date 2020-02-12.
