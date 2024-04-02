# JotaShell
Server software for accessing the shell remotely via a website

## How to deploy
Assuming you have a hosting machine powered by Linux.
1. Make sure you have Python installed. Version 3.10 is recommended, but it works fine with 3.7.x and above
2. Run ```python3 -m pip install flask``` to install the Flask module (required)
3. Run ```python3 main.py``` to start.
4. For accessing the web-shell from a device in a different network, you must configure port forwarding on your server.

You can optionally use the streaming version, but consider that it is in a very early stage and may not work properly.

## Known errors
- In main.py: Programs that require inputs wont return any output to the web-shell
- In main.py: Sudo doesn't work
- In index.html: The command input is not centered
- In index.html: When fetching HTML from internet it renders instead of showing plain text
- In index.html: The command input overlays the console output

Don't report errors about `streaming_test.py` as it is a test version and may not work properly.
