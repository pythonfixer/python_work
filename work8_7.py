def make_albums(singer_name, album_name, num = ''):
    make_album = {'singer': singer_name, 'album' : album_name}
    if num:
        make_album['num'] = num
    return make_album

make_album = make_albums('michael jackson', 'thriller')
print(make_album['singer'].title() + ", " + make_album['album'].title())

make_album = make_albums('leslie cheung', 'monica')
print(make_album['singer'].title() + ", " + make_album['album'].title())

make_album = make_albums('celine dion', 'unison', 20)
print(make_album['singer'].title() + ", " + make_album['album'].title() + ", " + str(make_album['num']))
