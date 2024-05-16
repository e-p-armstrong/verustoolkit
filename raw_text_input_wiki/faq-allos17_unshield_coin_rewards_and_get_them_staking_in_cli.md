# Question: How do I unshield my coin rewards and get them staking on CLI?

### Important General Information

`verus command "<userinput>"` needs to be entered literally, with `<userinput>` replaced by your specific userdata. So if the text directs you to use for example `"<Public Address>"`, you replace that (including the `<` and `>`) with the address,
so it looks similar to this: `"RYX6RYU3AAvwVCNyNM4cVyGUhSMUPvKs3r"`.

#### Remarks on Windows command line formatting:

The CLI help shows the command format for Linux and MacOS. On the native windows command prompt (`cmd.com`) the formatting is different.
* In windows command prompt, substitute the shown `'`-character with the `"`-character.
* In windows command prompt, substitute the shown `"`-character with the `\"`-characters.
* In windows command prompt, omit the preceding `./`.

Note: As an example, in Linux the command:
`./verus z_sendmany <my_private_address_without_quotationmarks> '[{"address":"<my_transparent_address>","amount":<95.9998>}]'`
should be entered on the Windows command prompt as:
`verus z_sendmany <my_private_address_without_quotationmarks> "[{\"address\":\"<my_transparent_address>\",\"amount\":<95.9998>}]"`


## Procedure:
1) `./verus z_shieldcoinbase "*"` my_private_address_without_quotationmarks
this capture all so called coinbases, i.e. mined coins that are not yet staking.
you have to wait 100 blocks (minutes) after receiving them before being able to move them.
wait for a few minutes for the tx to be confirmed.
2) `./verus z_getbalance <my_private_address_without_quotationmarks>` this is to substract the 0.0001 VRSC fee from the balance in the next step.
3) `./verus z_sendmany <my_private_address_without_quotationmarks> '[{"address":"<my_transparent_address>","amount":<95.9998>}]'`
amount is minus 0.0001 from balance and without quotation marks.
(4) to verify: `./verus z_gettotalbalance`
after a few minutes (operations from private addresses are a bit time consuming)

Note: I am always using the same private address.

(submitted by @karero, based on @dukeleto)

Note: last revision date 2020-04-12.
