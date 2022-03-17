def make_albums(singer_name, album_name, num = ''):
    make_album = {'singer': singer_name, 'album' : album_name}
    if num:
        make_album['num'] = num
    return make_album

while True:
    print("\nPlease enter the singer name:")
    print("(enter 'q' at any time to quit)")
    
    singer = input("Singer name: ")
    if singer == 'q':
        break
        
    album = input("Album name: ")
    if album == 'q':
        break
    
    number = input("Include number: ")
    if number == 'q':
        break
    
    make_album = make_albums(singer, album, number)
    if number:        
        print("Singer: " + make_album['singer'].title() + ", Album: " + make_album['album'].title() + ", Songs number: " + str(make_album['num']))
    else:
        print("Singer: " + make_album['singer'].title() + ", Album: " + make_album['album'].title())
        
