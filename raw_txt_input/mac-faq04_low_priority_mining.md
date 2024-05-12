# MacOS pool-mining on low priority.

Attention: Read it completely before use.

### Useful links for VRSC mining:

[Miners download page](https://verus.io/get-vrsc)
[Miner configuration guide](#!faq-macos\mac-faq03-mining_guide.md)

## Procedure:

In order to let your mining not interfere with other processes running on your PC, we'll need to deprioritize the mining process. This will result in your miner throttling down whenever your PC needs processing power.
People have reported to be able to use CPU-heavy applications, like games, without the miner interfering, with this method.

Because the Verus wallet (GUI and CLI) does a lot more than mining, it is not recommended to use this for a solo-mining setup.

First thing you will need is pool-mining software. The link is supplied above this procedure. Download your preferred miner, extract it to your prefered location and configure the batchfile with the pool of your choice and your own mining address.

Now we'll need to adjust the batchfile to run on low priority:

#### NHEQMINER:

  - Run your miner as you normally would, with `nice -n 19 ` placed in front of the command you normally use,
    for example:
      `nice -n 19 ./nheqminer -v -l pool.verus.io:9999 -u RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ.Donator -p x -t 6`
  - make sure you replace the pool (`pool.verus.io:9999`) with your prefered pool and the address
    (`RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ`) with your own address. The address shown in this line is the veruscoin
    foundation donation address. If desired change the identifier (`Donator`) to a name that easily identifies the
    miner to you.

Created by Oink.vrsc@.

Note: last revision date 2020-11-11.
