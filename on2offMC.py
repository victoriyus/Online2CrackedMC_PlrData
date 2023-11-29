import requests
import hashlib
import sys
import shutil
import os

def getCrackedUUIDFromOnlineUUID(uuid):

	r = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
	if (r.status_code != 200):
		return [False]
	username = "OfflinePlayer:" + r.json()["name"]
	hash = hashlib.md5(username.encode('utf-8')).digest()
	byte_array = [byte for byte in hash]
	byte_array[6] = hash[6] & 0x0f | 0x30
	byte_array[8] = hash[8] & 0x3f | 0x80
	hash_modified = bytes(byte_array)
	result = hash_modified.hex()
	offline_uuid = result[:8] + "-" + result[8:12] + "-" + result[12:16] + "-" + result[16:20] + "-" + result[20:]
	return [True, offline_uuid]

def main():
	onlineUUIDs = [element for element in os.listdir() if len(element) == 40]
	f = open("ValidUUIDs_Converted.txt", "w")
	g = open("InvalidUUIDs_NotConverted.txt", "w")
	for i in range(len(onlineUUIDs)):
		onlineUUIDnoFileExtension = onlineUUIDs[i][:36]
		offlineUUID = getCrackedUUIDFromOnlineUUID(onlineUUIDnoFileExtension)
		if offlineUUID[0]:
			shutil.copy(onlineUUIDs[i], offlineUUID + ".dat")
			f.write(onlineUUIDs[i] + "\n")
		else:
			g.write(onlineUUIDs[i] + "\n")

	f.close()
	g.close()

main()
