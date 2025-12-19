def get_coordinate(record):
    return record[1]
def convert_coordinate(coordinate):
    return tuple(coordinate)
def compare_records(azara_record, rui_record):
    return azara_record[1]==''.join(rui_record[1])  
def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record) is True:
        return azara_record+ rui_record
    else:
        return 'not a match'
def clean_up(combined_record_group):
    return '\n'.join(list(map(lambda x: f'{x[0],x[2],x[3],x[4]}',combined_record_group)))+'\n'  