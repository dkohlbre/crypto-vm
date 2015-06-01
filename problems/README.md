# Structure
Each problem should get its own directory!

Name directory as ctfnameandyear-problem

# Setups

Each problem dir should contain:

* setup.sh
  * Setup problem, register any services or whatever
  * copy any needed files to /var/www/html/files/
* description.md
  * Similar to CTF description, err on the side of more detail than normal.
  * Links to files should point to "/files/$file"
* hint.md
  * Strong pointers in direction of challenge
  * Recommended readings!
* solution.md
  * Links to writeups, or full writeups
* flag.txt
  * one line of ONLY THE EXACT FLAG TO BE MATCHED. Flag may not contain newlines, all other characters will be treated as part of the flag.
* config.txt
  * key-value pairs
  * port
  * category
* other files as needed for problem
  * service.py
  * foo.txt


# Notes
* Please include a windows-style file extension to all filenames
* Strip any hashes included in the names
* Make names as descriptive as possible
* Preface all files with problem name, including ctf

# Config syntax
PORT: number-or-NONE

CATEGORY: no-spaces-string

Thats it for now
