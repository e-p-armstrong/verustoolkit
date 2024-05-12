# How do I know when an immature block will "unlock" (mature)?

You can use the following scripts to automate it (prints, for each block, how many blocks remaining and the estimated date).
Keep in mind that the actual number of blocks per day is not always exactly 1440. It varies and the estimated dates may change slightly over time. Below you will find the Linux script that will calculate the extimated time for you:

## Script:

```bash

#!/bin/bash

#Config
verus_path="/XXXX/verus-cli/"
verus_cli="verus"

get_transactions=( $($verus_path$verus_cli listtransactions "" 1000 0|grep blockstomaturity|sed 's/.e: //;s/,//g'|awk '{ print $2 }'|sort -n) )
cur_block=( $($verus_path$verus_cli getmininginfo|grep blocks":|sed 's/.e: //;s/,//g'|awk '{ print $2 }') )
arr_idx="0"

for i in "${get_transactions[@]}"
do
        days_to_mature=$(( ($i )/1440 ))
        mature_to_date=$(date +"%m-%d-%Y" -d "+$days_to_mature days")
        echo ""Block #" $arr_idx "will mature in approximately"$days_to_mature "days" "(" $mature_to_date ")" "
        ((arr_idx++))
done
```

You'll need to enter the correct path to your verus directory and you will need to have the verus daemon running in order to sucessfully run this script.

(submitted by @TexWiller, edited by @bigtom, reviewed by @Englal)

Note: last revision date 2020-04-24.
