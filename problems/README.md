# Structure
Each problem should get its own directory!

Name directory as ctfnameandyear-problem

# Setup script
You can use new_problem.py to setup basic problems
(mostly) completely. It will create all the relevant markdown files
and most of the setup script you need. Make sure to read the rest of this and fill out anything the script tells you to!

# Setups

Each problem dir should contain:

* setup.sh
  * Setup problem, register any services or whatever
  * copy any needed PUBLIC files to /var/www/html/$PROBLEM/ (There is a skeleton for doing this in the default setup.sh)
* description.md
  * Similar to CTF description, err on the side of more detail than normal.
  * Links to files should point to "/$PROBLEM/$PROBLEM_$file"
* hint.md
  * Strong pointers in direction of challenge
  * Recommended readings! (Make sure to fill this out!)
* solution.md
  * Links to writeups, or full writeups.
  * If linking, include a PDF version of the writeup. (Print the page to pdf, and store)
* flag.txt
  * one line of ONLY THE EXACT FLAG TO BE MATCHED. Flag may not contain newlines, all other characters will be treated as part of the flag.
* config.txt
  * key-value pairs("KEY: VALUE")
  * CATEGORY
  * ENABLED
  * Others may be added later
* other files as needed for problem
  * service.py
  * foo.txt
  * init or xinetd configuration

# Ports and Servers
Add any ports you need accessible to the 'ports' file. Don't use a port already on that list!
The new_problem script will update the file automatically, but will NOT check for conflicts.

For an example of an xinetd server based problem, see hitcon2014-rsaha.

For an example of an init server config, see plaid2014-parlor.

# Notes
* Please include a windows-style file extension to all filenames publicly available
  * This is intended to help newer users, who may not be used to files without extensions.
* Strip any hashes included in the names
  * Keep naming clean
* Make names as descriptive as possible
* Preface all files with problem name, including ctf
  * The skeleton setup script will do this automatically

# Config syntax
CATEGORY: no-spaces-string

ENABLED: TRUE or FALSE

Thats it for now
