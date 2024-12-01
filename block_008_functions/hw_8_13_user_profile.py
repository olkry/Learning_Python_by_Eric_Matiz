def profile_designer(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile_oleg = profile_designer('Олег', "Крючихин", country='Россия', city="Москва", birth_date='08.04')

print(profile_oleg)