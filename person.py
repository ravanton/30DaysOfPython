person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    # 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'skills': [ 'React', 'MongoDB', 'Node'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'JavaScript'  in person['skills'] and 'Python' in person['skills']:
    print("He is front-end developer")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is back-end develop")
elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is fullstack developer')
else:
    print('not a developer')