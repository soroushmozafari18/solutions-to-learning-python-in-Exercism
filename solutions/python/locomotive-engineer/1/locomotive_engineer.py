"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a,b,c,*rest=each_wagons_id
    thelist=[c,*missing_wagons,*rest,a,b]
    return thelist

    
def add_missing_stops(mydict,**kwargs):
    return {**mydict,'stops':list(kwargs.values())}


def extend_route_information(route, more_route_information):
    return {**route,**more_route_information}

def fix_wagon_depot(wagons_rows):
    A,B,C=wagons_rows
    thelist=list(zip(A,B,C))
    a,b,c=thelist
    return [list(a),
            list(b),
            list(c)]

