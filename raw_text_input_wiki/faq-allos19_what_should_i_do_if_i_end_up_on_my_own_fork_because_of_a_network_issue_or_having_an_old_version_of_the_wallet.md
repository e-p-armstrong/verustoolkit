# Question: What should I do if I end up on my own fork because of a network issue or having an old version of the wallet?

This solution can be solved in 2 ways: you can simply install the latest bootstrap file (less work, big download) or search manually for the forked block and invalidate that block (time-consuming, no download needed.)

## Procedure 1 (Easy, installing bootstrap)

For all GUI or CLI users.
1.  Stop the wallet/mining process by cleanly shutting down the program.
2.  Update your wallet if necessary.
3.  Follow the procedure in [HOW-TO Backup, Install or Update and Bootstrap your wallet.md](#!how-to/how-to_bootstrap.md) to efficiently rectify the problem.
4.  Do not be dismayed if it seems that your mining rewards suddenly seem to come to a halt.  Remember, when you mine to the wrong chain rewards can come in very quickly, but they are worth nothing.

## Procedure 2 (Time consuming, no extra download)

### Verus-Desktop
1.  The commands are **all** entered in the *Native Client Terminal* that is located under `Settings`, `Coin Settings`.
2.  Search for the **earliest** block that not matches the blockchain:
    `run getblockhash <suspected blocknumber>` will show you the blockhash for the blocknumber you filled in
    The response shown in the *Native Client Terminal* will be similar to this:
    `5cc7844973fb95ef17f1772ea4aba579f0d8273fb0ee6064cd8e707d1056c646`
3.  Check the blockhash your command gave you against the blockhash the [explorer](https://explorer.verus.io) shows.
4.  If the blockhash from the explorer is different than yours, repeat steps 2 & 3 until you find the earliest block that is different.
5.  Use the **earliest incorrect blockhash** from your system to invalidate that block:
    `run invalidateblock <earliest incorrect blockhash>`
    The *Native Client Terminal* will not give feedback on this command.
6.  Now use the **correct blockhash** that the explorer gave you for the block you just locally invalidated:
    `run reconsiderblock <correct blockhash>`
    Again the *Native Client Terminal* will not give feedback on this command.
7.  Once your wallet connects to a node that is on the correct chain, it will quicly synchronize.
    If needed you can either restart your wallet to force new connections or manually disconnect bad nodes.

### CLI
1.  Search for the **earliest** block that not matches the blockchain:
    `./verus getblockhash <suspected blocknumber>` will show you the blockhash for the blocknumber you filled in
    The response will be similar to this:
    `5cc7844973fb95ef17f1772ea4aba579f0d8273fb0ee6064cd8e707d1056c646`
2.  Check the blockhash your command gave you against the blockhash the [explorer](https://explorer.verus.io) shows.
3.  If the blockhash from the explorer is different than yours, repeat steps 1 & 2 until you find the earliest block that is different.
4.  Use the **earliest incorrect blockhash** from your system to invalidate that block:
    `./verus invalidateblock <earliest incorrect blockhash>`
    The deamon will not give feedback on this command.
5.  Now use the **correct blockhash** that the explorer gave you for the block you just locally invalidated:
    `./verus reconsiderblock <correct blockhash>`
    Again the daemon will not give feedback on this command.
6.  Once your daemon connects to a node that is on the correct chain, it will quicly synchronize.
    If needed you can either restart your daemon to force new connections or manually disconnect bad nodes.


(submitted by @jimboscott, Edited by Oink.vrsc@)

Note: last revision date 2020-11-11.
