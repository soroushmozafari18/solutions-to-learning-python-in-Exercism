def transform(legacy_data):
    new_data={}
    for a,b in legacy_data.items():
        for letter in b:
            new_data.update({letter.lower():a})
    return new_data