# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# >>> import better_bencode
# >>> dumped = better_bencode.dumps(['spam', 42])
# >>> better_bencode.loads(dumped)
# ['spam', 42]
import better_bencode as bencode
from settings import TORRENT_FILE_PATH

class ParsingTorrentFile:
    """
    simple class using better_bencode to parse torrent file

    using bencode.
    # >>> import better_bencode
    # >>> dumped = better_bencode.dumps(['spam', 42])
    # >>> better_bencode.loads(dumped)
    # ['spam', 42]
    """
    def __init__(self, file_path):
        self.name = 'torrent file parser'
        self.torrent_file = file_path
        self.name_of_file = None
        self.size_of_file = None
        self.url_of_tracker = None

    def __str__(self):
        return self.name

    def bencoding_decode(self):
        with open(self.torrent_file, 'rb') as f:
            meta_data = f.read()
            data = bencode.loads(meta_data) # data will be binary data
            for elm in data:
                if b'info' in elm:
                    self.size_of_file = data[elm][b'length']
                    name = data[elm][b'name']
                    self.name_of_file = name.decode('utf-8')



    def bencoding_encode(self, data):
        return bencode.dumps(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # FIRST PARSE TORRENT FILE WITH:
    # use ParsingTorrentFile to create an instance
    # of the class it accepts the path of the class
    # Then run the method bencoding_decoding()
    print("on")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
