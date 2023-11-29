# Online2CrackedMC_PlrData
## Purpose
The purpose of this project is to port minecraft multiplayer online playerdata files (usually stored in /world/playerdata with the .dat suffix) to cracked/offline playerdata, as there doesn't seem to be any standard way to do this at the moment.
## Instructions
Follow the steps below to use the script for yourself

1. Go to the latest release and download the .py file
2. Navigate to your server's playerdata directory (usually server/world/playerdata/) and place the file in it
3. Run the file and wait for the script to complete
4. Once it's done, the offline UUIDs should be in the same directory, along with two text files; one for validUUIDs that were converted, and one for invalid UUIDs that were not. Note that the original online UUIDs are not removed.
## Limitations
- The script uses Mojang's API to get username data from UUIDs. At the moment, Mojang's API has a rate limit of ~200 requests/minute for this endpoint. If you run the script with over 200 UUIDs, you will be rate limited.
- Currently, the method for looking for UUIDs is simply taking all file names in the directory and checking if their length is 40 characters. This means playerdata.dat_old files are skipped over, and any other 40 character long file name will be sent to Mojang's API.
