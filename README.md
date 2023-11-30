# Online2CrackedMC_PlrData
## Purpose
When a server is started in online mode, player data is stored using each player's online UUID. When online mode is toggled off, player data is stored using offline UUIDs that are generated based off of player username. When the change happens and an existing player joins the server, their inventory and all other information stored in playerdata appears to be wiped. In reality, it's just stored in a different UUID.

The purpose of this project is to port minecraft multiplayer online playerdata files to cracked/offline playerdata.

## Instructions
Follow the steps below to use the script for yourself

1. Go to the latest release and download the .py file
2. Navigate to your server's playerdata directory (usually server/world/playerdata/) and place the file in it
3. Run the file and wait for the script to complete
4. Once it's done, the offline UUIDs should be in the same directory, along with two text files; one for valid UUIDs that were converted, and one for invalid UUIDs that were not. At this point you are ready to change online-mode to false in your server.properties file. Note that the original online UUIDs are not removed.
## Limitations
- The script uses Mojang's API to get username data from UUIDs. At the moment, Mojang's API has a rate limit of ~200 requests/minute for this endpoint. If you run the script with over 200 UUIDs, you will be rate limited.
- Currently, the method for looking for UUIDs is simply taking all file names in the directory and checking if their length is 40 characters. This means playerdata.dat_old files are skipped over, and any other 40 character long file name will be sent to Mojang's API.
- Plugins are NOT accounted for! If any plugins you have don't convert online UUIDs to offline UUIDs automatically, your data may not be migrated.
