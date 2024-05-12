# How to make a cloud daily backup of wallet.dat?
Note: I use Google Cloud for my staking wallet and backups but the script works regardless of what you use; if you have timelocked coins, you will have to keep your wallet.dat file secure for a long, long time: it's crucial to maintain secure the staking instance as well as the storage..

### Important General Information
`VRSC Wallet and Data location` on Linux: `~/.komodo/VRSC`

## Procedure:
If you use GCloud:
* create a new directory where we'll upload the backups (ie: mkdir /home/user/backup)
* create a storage bucket via GCloud console (ie bucket_verus)
* mount the bucket on your local machine (syntax is: gcsfuse  ; ie gcsfuse bucket_verus /home/user/backup)

The script can be crontab scheduled to run daily or you can run it manually; if you schedule it, you have to hardcode the encryption passphrase; otherwise you can input it manually each time. You will have to install gnupg2 to encrypt (`sudo apt-get install gnupg2 gnupg-agent`). As always: be sure to fully understand what the script does and why I left some echos to demonstration/test purposes, you can sefely remove all of them.
```bash
#!/bin/bash

# Customize the SOURCE and the DEST folders
SOURCE_FOLDER=/home/XXXXX/.komodo/VRSC/
DEST_FOLDER=/home/XXXX/backup/

BCK_DATE=date +%Y-%m-%d.%H:%M

SOURCE_FILE=wallet.dat
DEST_FILE=$SOURCEFILE""$BCK_DATE

ENCRYPT_EXT=".gpg"

# all echo are for test purposes, feel free to delete them
echo check variable
echo SOURCE - $SOURCE_FOLDER
echo SOURCE_FILE - $SOURCE_FILE
echo DEST FILE - $DEST_FILE
echo DEST - $DEST_FOLDER
echo TO_BE_DEL - $DEST_FOLDER$SOURCE_FILE

sleep 1

cp  $SOURCE_FOLDER$SOURCE_FILE $DEST_FOLDER$DEST_FILE
sleep 1
# Customize the passphrase!!
gpg2 --batch --yes -c --cipher-algo AES256 --passphrase="XXXXXX" $DEST_FOLDER$DEST_FILE
sleep 1
rm $DEST_FOLDER$DEST_FILE

# Keep only last 6 days - BE SURE to fully understand how it works, as every "rm" command!
find $DEST_FOLDER/wallet* -type f -mtime +6 -exec rm {} ;
```          

(submitted by @TexWiller)

Note: last revision date 2020-02-26.
