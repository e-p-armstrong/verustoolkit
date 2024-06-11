# Register VerusID / subID

Register a VerusID or subID. First a name needs to be committed, this costs a transaction fee (0.0001), after a block has passed the VerusID or subID can be registered. 

### VerusID name commitment
Commit a VerusID name by using the following command below. If no referral is available leave it empty.

``` json
./verus -chain=VRSCTEST registernamecommitment "YOUR_ID_NAME" "YOUR_R_ADDRESS" "REFERRAL_ID[OPTIONAL]"
```

Using the command above gives an output. Take that output and add the highlighted lines from below:

### VerusID registration

``` json{11-16}
./verus -chain=VRSCTEST registeridentity '{
  "txid": "2a614ae147a8abcb870eb45d5ddbfc1e1d283b942a5e77340d0d268c7fd47260",
  "namereservation": {
    "version": 1,
    "name": "test-id",
    "parent": "iJhCezBExJHvtyH3fGhNnt2NhU4Ztkf2yq",
    "salt": "bf5b76bb38cefd2bec266bdcc2f2f37cb321c9aab103e4aa802fdef90224a2f7",
    "referral": "",
    "nameid": "iMGMwQhtnaVwdrzev9uMspuNyQbYhCJEmU"
  }, 
    "identity":{
        "name":"YOUR_ID_NAME",
        "primaryaddresses":["R_ADDRESS_CHOSEN_WITH_NAME_COMMITMENT"],
        "minimumsignatures":1,
        "revocationauthority":["CHOOSE_I_ADDRESS"],
        "recoveryauthority":["CHOOSE_I_ADDRESS"]}
}'
```




### SubID name commitment
Commit a subID name by using the following command below (it is almost the same as doing a VerusID name commitment, except currency name is added.)

``` json
./verus -chain=VRSCTEST registernamecommitment "YOUR_ID_NAME" "YOUR_R_ADDRESS" "REFERRAL_ID[OPTIONAL]" "CURRENCY_NAME"
```

### SubID registration
The same as with VerusID registration.