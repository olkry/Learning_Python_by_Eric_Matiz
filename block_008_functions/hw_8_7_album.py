def make_album(perform, title, track_num=None):
    album = {'performer': perform, 'name': title}
    if track_num:
        album['track'] = track_num
    return album


album_1 = make_album('Ария', 'Блок ада', 8)
album_2 = make_album('Эпидемия', 'Эльфийская песнь')
print(album_1)
print(album_2)
album_3 = make_album(track_num=12, perform='Казидор', title='Аббат')
print(album_3)