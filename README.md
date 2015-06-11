# crypto-vm

## What is crypto-vm

Crypto-vm is a simple interface to, and archive for, cryptography
related CTF challenges.

## How do I use crypto-vm?

Crypto-vm is designed to be easy to start and access problems on. You
will need the following:
* A Linux (ideally, possibly OS X) machine. Not a VM!
* Vagrant, Python, and VirtualBox installed.

After you've met the requirements, clone this repository and run
"runme.sh"!  This may take some time, but should automatically import,
configure, and run the VM containing all of the challenges.  After
this setup completes, you can visit the server at "localhost:8082".

For some problems it is likely you will want mathematical tools, such
as Mathmatica or similar. Python with Crypto-vm does not currently supply any
tools, you should do any work and scripting external to crypto-vm.

## Why crypto challenges specifically?

Crypto challenges are often competely platform independent, and very
easily re-hosted. Additionally, many newer CTF competitiors find
crypto problems unapproachable, and having a collection designed to
make them easy to practice on could help.

That said, building a similar project that includes all problem types,
or is built for another category would probably be a great idea! Fork
and build it!

# Adding to crypto-vm
Adding a new problem to crypto-vm is pretty straight forward.

If your problem serves only static content (ex: it is just a
description and some ciphertexts), setup is trivial. Run the
new_problem script and fill out the markdown files and setup.sh
configuration.

If your problem requires only a simple server (ex: server.py, or
similar self contained) again setup is simple. Running the new_problem
script will do most of the work for you. You can add server that are
either already properly server (they use sockets) or servers intended
to run under a service like xinetd. Currently crypto-vm will help you
setup either init.d or xinetd configurations.

Other more complex problem designs are possible, but may not be a good
fit for crypto-vm.

Please read the Readme in the problems directory for more details.

After completing the setup for you problem, testing it (from a clean
'vagrant up' please!), submit a pull request and we'll add it!

# Why crypto-vm?

New CTF participants often have trouble engaging with cryptographic
challenges, or finding ones they can practice with. Crypto-vm is
intended to be an easy to use and helpful resource for those new to
cryptographic CTF challenges to practice with them in a helpful
environment.
