# Question: ERROR: Your wallet.dat is not matching the blockchain. Please restart the wallet with -reindex param.

It seems you probably trying to move coinbase coins that you must move them through a private address (zaddress) first by shielding your coinbases, which is required by Verus blockchain rules.

## Procedure

1. go to the "Receive" screen and make sure you have a private address (starting with `zs`), if you don't have that create one.
2. Copy the new private address to your clipboard
3. Go to the "Mining" screen, select Verus and select "Shield Rewards"
4. Leave "All unshielded funds" as the source and paste the new zaddress into the destination
5. Click on "Continue"
6. Wait a while until you have a private balance showing on the Wallet screen
7. Send again, this time from your private address to any normal transparent receive address that you have.

(submitted by @keda666, solution written by mikeout.vrsc@)

Note: revised 2020-04-24
