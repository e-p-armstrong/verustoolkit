# ERROR: Cannot Get a lock on data directory /root/.komodo/VRSC.

Komodo is probably already running.

## Procedure:

It just means you can't start it when it's already running. If it isn't running we can take a look at it.
Check to see if it is running by running:

  `./verus getinfo`

If it's running you'll get info back, if it isn't you'll get an error.
If that throws an error, it's worth checking using this command:

  `ps fax |  grep verus`

and seeing if any processes are listed besides the process you're using to search.
You would see verusd with a child process of komodo and all its cli arguments.


(submitted by @keda666, solution written by englal.vrsc@)

Note: last revision date 2020-02-26.
