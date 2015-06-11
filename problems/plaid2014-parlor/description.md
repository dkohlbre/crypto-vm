A simple betting game.

User connects and the server and a "session" starts. The server generates a
nonce for the session, and asks the user to input their own nonce. The server
requests the odds the user wants and then the user's guess. If
`md5(server_nonce+user_nonce)%odds == user_guess`, they win.

To verify the server isn't cheating, the user can request for the server\_nonce
to be displayed, which will also reset the server\_nonce to something else.

Get a copy of the server (with the flag removed!) [here](plaid2014-parlor_redacted-server.py).

The server is running on port 4321. Get the server to give you a flag!
