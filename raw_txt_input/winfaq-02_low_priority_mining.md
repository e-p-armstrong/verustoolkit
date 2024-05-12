# Windows pool-mining on low priority.

## Links to VRSC miners:

[Miners download page](https://verus.io/getVRSC.html)

## Procedure:

In order to let your mining not interfere with other processes running on your PC, we'll need to deprioritize
the mining process. This will result in your miner throttling down whenever your PC needs processing power.
People have reported to be able to use CPU-heavy applications, like games, without the miner interfering, with
this method.

Because the Verus wallet (GUI and CLI) does a lot more than mining, it is not recommended to use this for a
solo-mining setup. This is tested on Verus NHEQminer and Verus CCMiner on Windows 10.

First thing you will need is pool-mining software. The link is supplied above this procedure. Download your
preferred miner, extract it to your prefered location and configure the batchfile with the pool of your choice
and your own mining address.

Now we'll need to adjust the batchfile to run on low priority:

##### NHEQMINER:

  - change to the folder you extracted the download
  - edit the `start.bat`
  - Scroll down to the line, that needs to be adjusted:
      `nheqminer.exe -v -l %PoolHost%:%Port% -u %PublicVerusCoinAddress%.%WorkerName% -t %Threads%  %1 %2 %3 %4 %5 %6 %7 %8 %9`
  - adjust the line so it looks like this:
      `%windir%\system32\cmd.exe /c start "NHEQminer VRSC" /Low "%THIS_DIR%\nheqminer.exe" -v -l %PoolHost%:%Port% -u %PublicVerusCoinAddress%.%WorkerName% -t %Threads%  %1 %2 %3 %4 %5 %6 %7 %8 %9`
  - save and exit the file
  - run `start.bat` to start mining

##### CCMINER:

  - Change to the folder you put the three files from the downloaded archive in (`run.verushhash.bat`, `libcrypto-1_1-x64.dll` & `ccminer.exe`)
  - edit the `run.verushhash.bat`
  - The line, that needs to be adjusted:
      `ccminer -a verus -o stratum+tcp://na.luckpool.net:3956 -u REoPcdGXthL5yeTCrJtrQv5xhYTknbFbec.Donator -p d=6 -t 8`
  - adjust the line, so it looks like:
      `C:\Windows\System32\cmd.exe /c start "ccminerCPUv3.5 VerusPool" /Low "c:\Miners\CCminer 2.0 CPU Release 3.5\ccminer.exe" -a verus -o stratum+tcp://pool.verus.io:9999 -u RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ.Donator -t 16`
  - make sure you replace the pool (`stratum+tcp://pool.verus.io:9999`) with your prefered pool and the address
    (`RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ`) with your own address. The address shown in this line is the veruscoin
    foundation donation address. If desired change the identifier (`Donator`) to a name that easily identifies the
    miner to you.
  - save and exit the file
  - run `run.verushhash.bat` to start mining.

Submitted by Oink.vrsc@
Note: last revision date 2020-11-11.
