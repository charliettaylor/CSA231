from terminusdb_client.woqlquery.woql_query import WOQLQuery as WQ
from terminusdb_client.woqlclient.woqlClient import WOQLClient

server_url = "https://127.0.0.1:6363"
user = "admin"
account = "admin"
key = "root"
dbid = "playlistgroup3"
repository = "local"
label = "Playlist"
description = "A playlist"

client = WOQLClient(server_url)
client.connect(user=user,account=account,key=key,db=dbid)


def insert(artist, length, album, title, count):
    docName = "song" + str(count)
    WQ().woql_and(
        WQ().insert("doc:" + docName, "scm:song")
            .property("scm:artist", artist)
            .property("scm:length", int(length))
            .property("scm:album", album)
            .property("scm:title", title)
    ).execute(client, "Add song")

def count_objects():
    song_query = WQ().triple("v:X", "scm:title", "v:Y").execute(client)
    return len(song_query["bindings"])


def main():
    print("Follow the prompts to add entries to the playlist database!")
    count = count_objects()
    while input("Continue? [y/n]") != "n":
        artist = input("enter the artist")
        length = input("enter the length")
        album = input("enter the album")
        title = input("enter the title")
        insert(artist, length, album, title, count)
        count = count_objects()

main()