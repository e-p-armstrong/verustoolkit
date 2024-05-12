# Compile Monkins Verus enhanced CCMiner for various hardware

Read it completely before using.

## Important General Information

This guide is aimed towards Debian based Linux distributions. If you are using a different kind of distribution
(eg RPM-based, like CentOS) you will need to install the dependancies using a procedure that fits your
specific distribution.

There are 3 active branches in ccminer github repo:
  `ARM`             (for 64bit ARM chips with AES intrinsic)
  `Verus2.2`        (standard x86-64 pc's)
  `Verus2.2gpu`     (GPUs)

Note: Replace `ARM` in the `git clone` line below with the branchname above you want to use.

## Procedure:

Install dependencies (specific for Debian-based distributions):
```bash
sudo apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git
```
For GPU-miner compilation additional sources are required (Not needed for CPU or ARM):
```bash
wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run
sudo sh cuda_10.2.89_440.33.01_linux.run
```
Download the source and compile:
```bash
git clone --single-branch -b ARM https://github.com/monkins1010/ccminer.git
cd ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh
```
And finally starting the miner (Change pool, address & workername to your own liking):
```bash
./ccminer -a verus -o stratum+tcp://pool.verus.io:9999 -u RVjvbZuqSGLGDm1B9BFkbHWySPKEx4tfjQ.donator -p x
```

Info from @Chris - Monkins1010 LOUD Mining.

Note: last revision date 2021-04-20.
