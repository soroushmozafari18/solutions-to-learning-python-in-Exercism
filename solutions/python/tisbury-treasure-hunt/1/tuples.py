"""Functions to help Azara and Rui locate pirate treasure."""


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
    report=[]
    for eachtuple in combined_record_group:
        newtuple=((eachtuple[0],eachtuple[2],eachtuple[3],eachtuple[4]))
        report.append(str(newtuple)+'\n')
    return ''.join(map(str,report))
        
