# error while loading shared libraries: libgomp.so.1: No such file or directory
# error while loading shared libraries: libz.so: No such file or directory

When running `./verusd` on a Linux distro (eg Debian or Devuan), not all dependencies may be installed by default, resulting in the errormessage `error while loading shared libraries: libgomp.so.1: No such file or directory` or `error while loading shared libraries: libz.so: No such file or directory`.

To solve this you need to install the libgomp and zlib1g-dev libraries:
`sudo apt-get install libgomp1 zlib1g-dev`

Solution supplied by: Oink.vrsc@

Note: revision date 2021-12-01.
