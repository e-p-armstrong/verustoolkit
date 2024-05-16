# Set up Verus Vault in Verus Desktop (flags)
![image-vaulteasy](/images/lockfunds.png)
Verus Vault is not yet accessible with clickable interfaces. You can still set up Vault in Verus Desktop. Here's how.

What do you need:
- Latest version Verus Desktop
- VerusID (on the Verus mainchain, or when PBaaS is live on any other chain)

With Verus Vault you can lock funds in your VerusID. When your funds are locked in the Vault you can not spend them anymore, they cannot leave the VerusID. You can still always continue to stake and receive coins.

You can lock a VerusID in two different ways that cannot be circumvented by anyone, except the ``revocation and recovery authorities`` together. 

| Lock type | How it works | 
| - |:-----|:-----|
| TimeLock | Locks the funds and unlocks until a predetermined number of blocks have passed. | 
| DelayLock | Locks the funds and unlocks with a delay. Funds can not be spent until an unlock has been requested + a predetermined number of blocks have passed. | 

### Get Started
We need to access the commandline interface in Verus Desktop. Go to ``settings`` (the cogwheel top right corner), then select ``Coin Settings``. Here we can fill in the commands to set up your Vault.

## Vault with TimeLock
![image-timelock](/images/timeock.png)
Now let's put a Timelock on a VerusID. For a TimeLock you need to know the blockheight of the blockchain. Let's say the blockchain's blockheight is at ``1,000,000`` blocks. You want to lock your VerusID for 1 year. 1 year is ``508994`` blocks.

::: warning Long-Term Locking
**For long-term locking it's best to take an average block time of 62 seconds. Yet there are some variables that make it difficult to predict an exact time, leap years for example. Over long-term there are an average of 1394.5484 blocks per day.**
:::

- Under ``timelock`` you put ``1508994``
- Under ``name`` you put your VerusID name without ``@``
- Under ``primaryaddress`` you put the R-address which is the primary address of your VerusID (you can find this address in the 'VerusID'-tab, open your VerusID and click `ID Info')

So in our example your VerusID is locked for approximately for 1 year. After that period of time the funds can be spent again.

``` json
run updateidentity 
'{
    "name":"youridentityname",
    "minimumsignatures":1,
    "primaryaddresses":["primary-address-comes-here"],
    "flags":0,
    "timelock":1534360
}'
```

You can copy and paste this code snippet into the commandline interface of Verus Desktop and edit the necessary inputs for your needs. In the code snippet are the minimum requirements to update your VerusID with a lock.

:::tip Revoke & Recover
Remember: you can always revoke and recover a locked VerusID.
:::

## Vault with DelayLock
![image-delaylock](/images/delaylock.png)
Now let's put a DelayLock on a VerusID. This means that you lock the identity, and when you request the identity to be unlocked, a predetermined number of blocks have to pass before you can actually spend the funds again.


### Set the DelayLock
Let's say you want to put a Delaylock of 1 week. 1 week is ``10,080`` blocks (1440x7). This will lock the identity, and when you requested an unlock, it takes 1 week (or 10,080 blocks) before the funds can be spent again.

- Under ``timelock`` you put ``10080``
- Under ``name`` you put your VerusID name without ``@``
- Under ``primaryaddress`` you put the R-address which is the primary address of your VerusID (you can find this address in the 'VerusID'-tab, open your VerusID and click `ID Info')

``` json
run updateidentity 
'{  
    "name":"youridentityname",
    "minimumsignatures":1,
    "primaryaddresses":["primary-address-comes-here"],
    "flags":2,
    "timelock":10080
    }'
```

You can copy and paste this code snippet into the commandline interface of Verus Desktop and edit the necessary inputs for your needs. In the code snippet are the minimum requirements to update your VerusID with a lock.

:::tip Revoke & Recover
Remember: you can always revoke and recover a locked VerusID.
:::

### Request an unlock
Above you locked a VerusID with a DelayLock. Now let's request an unlock. When an unlock has been requested you have to wait the predetermined number of blocks before you can spend the funds again.

Fill in your VerusID ``name``, the ``primary address`` and set ``flags`` to 0. Now you only have to wait for your predetermined number of blocks (10,080 in our example) to run out so you can spend the funds again.

``` json
run updateidentity 
'{  
    "name":"youridentityname",
    "minimumsignatures":1,
    "primaryaddresses":["primary-address-comes-here"],
    "flags":0
    }'
```

You can copy and paste this code snippet into the commandline interface of Verus Desktop and edit the necessary inputs for your needs. In the code snippet are the minimum requirements to unlock your VerusID.