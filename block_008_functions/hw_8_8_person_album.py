def make_album(perform, title, track_num=None):
    album = {'performer': perform, 'name': title}
    if track_num:
        album['track'] = track_num
    return album


all_albums ={}
count = 1

while True:
    print(
        'Добовление нового альбома!\nНажмите q для выхода в любое время.\n'
    )
    autor_name = input('Введите имя исполнителя: ')
    if autor_name == 'q':
        break
    album_name = input('Введите название альбома: ')
    if autor_name == 'q':
        break
    number_track = input('Введите количество треков, или просто пропустите: ')
    if number_track == 'q':
        break
    new_album = make_album(autor_name, album_name, number_track)
    all_albums[f'альбом_{count}'] = new_album
    count += 1
    print(f'Вы успешно добавили альбом {album_name} от {autor_name}')
    print()

print(all_albums)