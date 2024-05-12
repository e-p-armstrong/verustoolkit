# How do I install the Verus CLI (command line interface) wallet on a brand new (hosted) Linux system?

Notice: Read it completely before use.

#### Important General Information

`wallet.dat` location on Linux: `~/.komodo/VRSC`

#### Necessary files:

Link 1: [Download latest Wallet](https://verus.io/wallet)
Link 2: [Download Verus Bootstrap](https://bootstrap.verus.io/)

## Procedure:

1. First make sure your system is up to date:  
  `sudo apt-get update && apt-get upgrade -y`  

2. I suggest not to use the root account. I you have not yet done, set up a new user
  `sudo adduser newusername`
  `sudo usermod -aG sudo newusername`
3. Switch to new username
  `su -  newusername`
4. Test the your new user actually has root (SuDo) access, e.g.:
  `sudo ls -la /root`
  You should get some lines like this:
  `drwx------  6 root root 4096 Jul  3 15:56`
5. Download & install the wallet binaries:
  `wget https://github.com/VerusCoin/VerusCoin/releases/download/v0.9.3/Verus-CLI-Linux-v0.9.3-amd64.tgz`
 The downloaded archive contains another archive and a signature text file, enabling the archive within to be verified (You'll need a running wallet to do that)
 Also: Verify the URL to the latest version from the [Download latest Wallet](https://verus.io/wallet) above.
  `tar -xvf Verus-CLI-Linux-v0.9.3-amd64.tgz`
 Now extract the wallet archive:
  `tar -xvf Verus-CLI-Linux-v0.9.3-amd64.tar.gz`
 Change directory to verus-cli
  `cd verus-cli`
 Fetch parameters, takes time, more on slow Internet connection
  `./fetch-params`
Creating the chaindata directory
  `cd ~`
  `mkdir -p .komodo/VRSC`
  `cd ~/.komodo/VRSC`
Download the block-chain bootstrap, this considerably speeds up synchronisation of the block-chain from days to minutes... (optional)
  `wget https://bootstrap.verus.io/VRSC-bootstrap.tar.gz`
  `tar -xvf VRSC-bootstrap.tar.gz`
 Install libraries for Verus
  `sudo apt-get install libcurl3 g++-multilib -y`
 Install Tmux a terminal multiplexer with which you can run threads in the background see https://en.wikipedia.org/wiki/Tmux
  `sudo apt-get install tmux -y`
 Start tmux:
  `tmux`
 Launch Verus Daemon with or without number of threads
 (usually number of threads equals number of cores or double of that if the processor support hyper threading well)
  `~/verus-cli/verusd -gen -genproclimit`
  `~/verus-cli/verusd -gen -genproclimit=24`
 Once mining is operational – again this may take some time –
 you’ll see: 256 mega hashes complete - working
 then detach tmux
`[ctrl]&b d`

Disable login with Root User
(make sure your newly created user login works and has sudo rights)
  `sudo nano /etc/ssh/sshd_config`
Find: PermitRootLogin yes
And set to
PermitRootLogin no
Apply new settings:
  `sudo systemctl restart sshd`

(submitted by @karero, corrected by @Glennp, edited by Oink.vrsc@)

Note: last revision date 2022-08-19.
