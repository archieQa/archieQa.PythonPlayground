def make_album(artist_name, album_title):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album


while True:
    print("\nPlease enter the album details:")
    print("(Type 'quit' at any time to stop)")

    artist = input('Please enter artist name: ')
    if artist.lower() == 'quit':
        break

    title = input('Please enter the title:')
    if title.lower() == 'quit':
        break

    album = make_album(artist, title)
    print(album)
