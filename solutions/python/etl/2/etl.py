def transform(legacy_data):
    new_data={}
    for value in list(legacy_data.values()):
        if isinstance(value,list):
            for letter in value:
                new_data[letter.lower()]=list(legacy_data.keys())[(list(legacy_data.values()).index(value))]
        else:
            new_data[value.lower()]=list(legacy_data.keys())[list((legacy_data.values()).index(value))]
    return new_data
