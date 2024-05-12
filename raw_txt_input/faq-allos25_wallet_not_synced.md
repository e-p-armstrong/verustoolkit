# My wallet is stuck on block number XXXX. It does not synchronize properly anymore.

note: Read it completely before use.

### Verus `Wallet.dat`, Chaindata & `VRSC.conf` standard locations
 * Linux:		`~/.komodo/VRSC`
 * Mac OS: 	`~/Library/Application Support/Komodo/VRSC`
 * Windows 10: 	`%AppData%\Roaming\Komodo\VRSC\`
 * OS independent through Verus Desktop: Click `help`, `Show Verus data folder (default)`

#### Usefull links:
Link 1: [Download latest Wallet](https://verus.io/wallet.html)
Link 2: [Show current blockheight](https://explorer.verus.io/api/getblockcount)

## Procedure:
In case your wallet is not synchronized with the blockchain and restarting doesn't connect to any peers:

Compare your blockheight with the one Link 2 above is showing to make sure you are
not synchronized anymore. If the blockheight of the link above is significantly higher (more than 10) than
the blockheight your wallet is showing, follow the rest of the procedure.
If the numbers are equal or close, your wallet is synchronized and the procedure below will not solve any problems.

Close your wallet.
Go to the appropriate location for your OS as mentioned above.

Add a similar list to the bottom of your `VRSC.conf`, just below `rpcallowip=127.0.0.1`:
```
  addnode=157.90.113.198:27485
  addnode=95.217.1.76:27485
```
Save and exit the file.
An up-to-date list of working nodes can be found in Verus Discord in the #tipbot channel, by messaging `/peerinfo` in that channel.

After you added nodes, remove `peers.dat` that is in the VRSC folder.
(At least rename or move to a different location).
Make sure you don't remove any other files/folders, or you'll have to [bootstrap](http://blacksquare/#!how-to/how-to_bootstrap.md) your wallet.
Then start your wallet as you're used to.

If the problem persists, continue with this WIKI: [Recover from forking, network or old wallet problems](https://wiki.verus.io/#!faq-allos/faq-allos19_what_should_i_do_if_i_end_up_on_my_own_fork_because_of_a_network_issue_or_having_an_old_version_of_the_wallet.md)

Submitted by Oink.vrsc@ & Thoskk.vrsc@

Note: last revision date 2023-06-03.
