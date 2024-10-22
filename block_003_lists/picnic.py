guests =['Herman', 'Cloud', 'Sephiroth']

print(f'{guests[0]}, вы приглашены на пикник!')
print(f'{guests[1]}, вы приглашены на пикник!')
print(f'{guests[2]}, вы приглашены на пикник!')
counte_guests = len(guests)
print(f'\n Приглашено {counte_guests} гостей')

print(f"Ой, а {guests[1]} прийти не сможет")
guests[1] = 'Tifa'

print('Новый список приглашений: ')
print(f'{guests[0]}, вы приглашены на пикник!')
print(f'{guests[1]}, вы приглашены на пикник!')
print(f'{guests[2]}, вы приглашены на пикник!')
counte_guests = len(guests)
print(f'\n Приглашено {counte_guests} гостей')
print('!!! Ура мы увеличили стол до 6 !!!')
guests.insert(0, "Gabriel")
guests.insert(2, "Alucard")
guests.append('Crouli')

print('\nНовый список приглашений: ')
print(f'{guests[0]}, вы приглашены на пикник!')
print(f'{guests[1]}, вы приглашены на пикник!')
print(f'{guests[2]}, вы приглашены на пикник!')
print(f'{guests[3]}, вы приглашены на пикник!')
print(f'{guests[4]}, вы приглашены на пикник!')
print(f'{guests[5]}, вы приглашены на пикник!')
counte_guests = len(guests)
print(f'\n Приглашено {counte_guests} гостей')

print("\nО нет! всё сломалось!")
quitting = guests.pop(2)
print(f'{quitting}, извини, в другой раз((')
quitting = guests.pop(2)
print(f'{quitting}, извини, в другой раз((')
quitting = guests.pop(2)
print(f'{quitting}, извини, в другой раз((')
quitting = guests.pop(2)
print(f'{quitting}, извини, в другой раз((')

print(f'\n{guests[0]}, приглашение в силе')
print(f'{guests[1]}, приглашение в силе')
counte_guests = len(guests)
print(f'\n Приглашено {counte_guests} гостей')
del guests[0]
del guests[0]
print(guests)
counte_guests = len(guests)
print(f'\n Приглашено {counte_guests} гостей')

