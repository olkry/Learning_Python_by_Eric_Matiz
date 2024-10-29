favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

take_a_survey = ['Carl', 'Jen', 'Lily', 'Edward', 'Sten']

# for name in favorite_languages.keys():
#     if name.title() in take_a_survey:
#         print(f'{name.title()} благодарим за прохождение теста!')
#         take_a_survey.remove(name.title())
#
# for name in take_a_survey:
#     print(f'{name.title()} пожалуйста пройдите тест.')

for name in take_a_survey:
    if name.lower() in favorite_languages.keys():
        print(f'{name.title()} благодарим за прохождение теста!')
    else:
        print(f'{name.title()} пожалуйста пройдите тест.')