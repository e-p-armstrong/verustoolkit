# ﻿Question: How can I tell the difference between staked and mined coins?

## CLI:

You can check this in the VerusExplorer https://explorer.verus.io/
1. Check last 10 transactions in the </>CLI. Use `listtransactions`.
2. Copy the blockhash of the received award
3. Add it at the end of https://explorer.verus.io/api/getblock?

Hint: An example: https://explorer.verus.io/api/getblock?hash=9e6fa91356211a554c580c90ec9c2067dd420ff74c7d33481775793f7b0e7f03 – so this one is minted....

## Verus Desktop:

In Verus Desktop, simply go to your Mining Dashboard and enter into Verus details.
Scroll down to the bottom of the page. It will list the rewards as `mined` or `minted` in green.
The TXIDs that staked the  minted rewards are shown in blue.

## Verus Agama (Deprecated):

In the GUI you can also click yourself thru to that information.
1. Click on the magnifying glass all the way on the right of the transaction.
2. On the pop-up click on "Open in the VRSC Explorer" bottom left.
3. In the VRSC explorer click on the block hash value (in light blue) – now the block hash is displayed as the title of the box.
4. Click on the info "i" on the right and click on "search": in the result displayed for blocktype 'mined' or 'minted'.(edited)

(submitted by karero, edited by Oink.vrsc@)

Note: last revision date 2020-11-11.
