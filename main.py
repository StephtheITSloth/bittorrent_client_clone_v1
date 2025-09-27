"""
implementation source: https://github.com/eliasson/pieces/tree/master/pieces

we need to get a list of peers to connect with.
This is where the tracker comes in.
A tracker is a central server keeping track of available peers for a given torrent.
A tracker does NOT contain any of the torrent data, only which peers that can be connected to and their statistics

peer_id
The peer_id is exactly 20 bytes (characters) long.
There are mainly two conventions how to encode client and client version information into the peer_id,
Azureus-style and Shadow's-style.

Azureus-style uses the following encoding:
'-', two characters for client id,
four ascii digits for version number,
'-', followed by random numbers.
For example: '-AZ2060-'

url params:
info_hash	The SHA1 hash of the info dict found in the .torrent
peer_id	A unique ID generated for this client
uploaded	The total number of bytes uploaded
downloaded	The total number of bytes downloaded
left	The number of bytes left to download for this client
port	The TCP port this client listens on
compact	Whether or not the client accepts a compacted list of peers or not


From the tracker response, there is two properties of interest:

interval - The interval in seconds until the client should make a new announce call to the tracker.
peers - The list of peers is a binary string with a length of multiple of 6 bytes.
Where each peer consist of a 4 byte IP address and a 2 byte port number (since we are using the compact format).

"""
from random import randint
import requests


class Tracker:
    #for dev a dummy torrent

    torrent = {}
    def __init__(self, torrent):
        self.name = "Tracker class"
        self.torrent = torrent
        self.peer_id = self.generate_peer_id()
        self.left = None

    def generate_peer_id(self):
        #attach -PC0001- to a string made of 12 random numbers (# Azureus - style)
        return '-PC0001-' + ''.join([str(randint(0,9)) for _ in range(12)])

    def create_request_params(self, uploaded=0, downloaded=0):
        params ={
            'info_hash': torrent.info_hash, #should be the SHA1 hash of torrent info
            'peer_id': self.peer_id,
            'uploaded': uploaded,
            'downloaded': downloaded,
            'left': self.torrent.size - downloaded,
            'port': 6969,# using 6969 as an example
            'compact': 1
        }


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("on")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
