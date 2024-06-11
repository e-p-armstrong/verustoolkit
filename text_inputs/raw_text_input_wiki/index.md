# ![Verus Coin](https://wiki.verus.io/img/favicon.png "Verus Coin Wiki") Verus Coin Wiki
In this WIKI we collected the most frequently asked questions and useful guides that are related to Verus.

On the bottom of each document, you may find a revision and/or creation date. If no date is mentioned the document originates from before february 12th, 2020 and may apply to older situations.

If you have any questions about the information here, need help or have suggestions on the content, don't hesitate to contact us through [Discord](https://verus.io/discord).


## Information
[Verus Welcome Information](#!information/verus-welcome.md)
[Verus Information Page](#!how-to/how-to_verus_info.md)
[Verus Release Notes](#!information/release_notes.md) ***`UPDATED to v1.0.7`***
[VerusIDs](#!information/verusid.md)
[Verus Digital Signatures](#!information/signatures.md)
[VerusHash 2.1](#!information/verushash_2.1.md)
[VerusPay](https://github.com/monkins1010/VerusPay/wiki)
[Verus Discord verification](https://youtu.be/YVOfIMjRf30) ***`Video`***
[Bootstrap video](https://youtu.be/xgLxzel5t04) ***`Video`***

## How-To
[Bootstrap your wallet](#!how-to/how-to_bootstrap.md) ***`TIP`***
[Verifying the signature of an updated wallet](#!how-to/how-to_check_signatures.md)
**[Backing up my wallet](#!how-to/how-to_backup_my_wallet.md)** ***`HIGHLY RECOMMENDED`***
**[Restoring my wallet](#!how-to/how-to_restore_my_wallet.md)**
[Change Verus-Desktop from Lite Mode to Native Mode](#!how-to/how-to_lite_to_native.md)
[import your Lite wallet address into your native Verus Desktop](#!how-to/how-to_convert-seed-to-wif.md)
[Verus Wallet installation guide (Linux)](#!faq-linux/faq-lin01_install_linux_cli.md)
[Verus Beginners Staking guide (External)](https://medium.com/veruscoin/verus-beginners-staking-guide-efbbdc4de951)
[Verus Beginners Mining guide (External)](https://medium.com/veruscoin/how-to-earn-vrsc-solo-mining-with-your-cpu-and-staking-mined-coins-aa27da76882c)
[Shield Verus Coins via Command Line Interface](#!how-to/how-to_shield_via_cli.md)
[Create an ID on Verus Desktop (pdf)](https://wiki.verus.io/how-to/how-to_create_verus_id_with_verus_desktop.pdf)
[Create an ID on command Line (pdf)](http://wiki.verus.io/how-to/how-to_create_verus_id_with_cli.pdf)
[Join Verus Testnet](#!how-to/how-to_join_testnet.md)
[Reset Verus Testnet](#!how-to/how-to_reset_testnet.md)

## Frequently Asked Questions (General)
[How do I know when an immature block will "unlock" (mature)?](#!faq-allos/faq-allos01_immature_block_unlock_time_calculation_manual_calculation.md)
[I'm mining since XYZ with XYZ, why I haven't found a block yet?](#!faq-allos/faq-allos02_average_time_to_find_a_block_manual_calculation.md)
[How do I direct all my mined rewards to a single Verus wallet?](#!faq-allos/faq-allos03_mine_rewards_to_a_single_verus_wallet_gui_+_cli.md)
[How to consolidate multiple `wallet.dat` files in one?](#!faq-allos/faq-allos04_consolidate_multiple_wallet.dat_files_in_one.md)
[What reward do I get for staking (PoS) or Mining (PoW) a block?](#!faq-allos/faq-allos05_reward_received_per_blocknummer.md)
[Stake estimates, halving and block-rewards](#!faq-allos/faq-allos06_pos,_halving,_block_reward.md)
[What's the value of VRSC?](#!faq-allos/faq-allos07_what_are_my_vrsc_worth.md)
[Is mining profitable?](#!faq-allos/faq-allos08_mining_profitability.md)
[How do you know a block was minted (staking reward)?](#!faq-allos/faq-allos09_how_do_you_know_a_block_was_minted_staking_reward.md)
[Useful Verus CLI commands](#!faq-allos/faq-allos10_useful_cli_commands.md)
[How does staking work?](#!faq-allos/faq-allos13_how_does_staking_work.md)
[How can I tell the difference between staked and mined coins?](#!faq-allos/faq-allos15_how_can_i_tell_the_difference_between_staked_and_mined_coins.md)
[How can I check my immature balance in the Graphic User Interface?](#!faq-allos/faq-allos16_how_can_i_check_my_immature_balance_in_the_gui.md)
[How do I unshield my coin rewards and get them staking on CLI?](#!faq-allos/faq-allos17_unshield_coin_rewards_and_get_them_staking_in_cli.md)
[ERROR: Your wallet.dat is not matching the blockchain. Please restart the wallet with -reindex param.](#!faq-allos/faq-allos18_your_wallet.dat_is_not_matching_the_blockchain._please_restart_the_wallet_with_-reindex_param.md)
[What should I do if I end up on my own fork because of a network issue or having an old version of the wallet?](#!faq-allos/faq-allos19_what_should_i_do_if_i_end_up_on_my_own_fork_because_of_a_network_issue_or_having_an_old_version_of_the_wallet.md)
[I followed the previous procedure and am still having problems with my wallet.](#!faq-allos/faq-allos20_i_followed_the_procedure_in_faq_19_and_am_still_having_problems_with_my_wallet.md)
[What are the mining pools that I can join?](#!faq-allos/faq-allos21_mining_pools.md)
[What are the staking pools that I can join?](#!faq-allos/faq-allos22_staking_pools.md)
[Verus Wallet & VRSC.conf standard locations](#!faq-allos/faq-allos24_wallet.dat_and_vrsc.conf_location.md)
[My wallet is stuck on block number XXXX. It does not synchronize properly anymore.](#!faq-allos/faq-allos25_wallet_not_synced.md)
[I accidentally send funds to a B-address and cannot move those funds](#!faq-allos/faq-allos26_sent_funds_to_b-address.md)

## Frequently Asked Questions (Windows specific)
[Remarks on Windows command line formatting](#!faq-windows/winfaq-01_cli_formatting.md)
[Windows pool-mining on low priority](#!faq-windows/winfaq-02_low_priority_mining.md)
[Standard locations for Verus-Desktop installations](#!faq-windows/winfaq-03_verus_desktop_locations.md)

## Frequently Asked Questions (Linux specific)
**[Install the Linux CLI wallet](#!faq-linux/faq-lin01_install_linux_cli.md)** ***`TIP`***
[Script calculating time to unlock for immature rewards](#!faq-linux/faq-lin02_immature_block_unlock_time.md)
[Linux Bash scripts to make mining life easier](#!faq-linux/faq-lin03_linux_scripts_make_life_easy.md)
[ERROR: Cannot obtain lock on data directory](#!faq-linux/faq-lin04_cannot_obtain_lock.md)
[Cloud daily backup of Wallet.dat](#!faq-linux/faq-lin05_daily_cloud_backup.md)
[Compile Monkins Verus enhanced CCMiner for various hardware](#!faq-linux/faq-lin06_compile_ccminer.md)
[PHP staking interface for coinshielding nodes](#!faq-linux/faq-lin07_PHP_CLI_interface.md)
[Low priority pool-mining](#!faq-linux/faq-lin08_low_priority_mining.html.md)
[error while loading shared libraries: libgomp.so.1 and/or zlib1g-dev](#!faq-linux/faq-lin09_libgomp.so.1.md)
[Standard locations for Verus Desktop installations](#!faq-linux/faq-lin10_verus_desktop_locations.md)

## Frequently Asked Questions (MacOS specific)
[ERROR: Cannot Get a lock on data directory /root/.komodo/VRSC.](#!faq-macos/mac-faq01_obtain_lock.md)
[What versions of OSX/macOS are supported?](#!faq-macos/mac-faq02_what_versions_osx.md)
[Start mining on MacOS](#!faq-macos/mac-faq03-mining_guide.md)
[MacOS pool-mining on low priority](#!faq-macos/mac-faq04_low_priority_mining.md)
[Standard locations for Verus Desktop installations](#!faq-macos/mac-faq05_verus_desktop_locations.md)

## Frequently Asked Questions (ARM specific)
**[Updating CLI wallet](#!faq-arm/armfaq-03_updating.md)**
[Hardware and software requirements](#!faq-arm/armfaq-02_requirements.md)
[error while loading shared libraries: libgomp.so.1 and/or libz.so](#!faq-arm/armfaq-01_libgomp.so.1.md)

## CLI wallet specific Information
[Verusd options list](#!faq-cli/clifaq-01_verusd_options.md) ***`UPDATED to v1.2.2-4`***
[Verus command list](#!faq-cli/clifaq-02_verus_commands.md) ***`UPDATED to v1.2.2-4`***
[Remarks on Windows command line formatting](#!faq-windows/winfaq-01_cli_formatting.md)

## Q&A Archive
[Q&A questions channel Verus-WhiteBIT 2020-07-28](#!q-a/veruscoin-q-a-questions-20200728.html)
[Q&A reward channel Verus-WhiteBIT 2020-07-28](#!q-a/veruscoin-q-a-reward-20200728.html)

Note: last revision date 2024-05-03.
