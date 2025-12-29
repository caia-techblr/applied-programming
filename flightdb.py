"""
flightservicedb = [
    [ "Indigo", "6E205", "Bengaluru", "Delhi", "1000"],
    [ "AirXPress", "AI405", "Chennai", "Hyderabad", "500"]
]
"""
flightservicedb = []

def add_service(operator, fno, origin, destination, distance):
    service = [operator,fno,origin,destination,distance]
    flightservicedb.append(service)

def list_all_services():
    for service in flightservicedb:
        print(service)
        #print(service[0],service[1],service[2],service[3],service[4])

def list_services_by_origin(origin):
    # results = {}
    for service in flightservicedb:
        if service[2] == origin:
            print(service)  # results.add(service)
    # return results

def list_services_by_destination(destination):
    pass

def list_services_by_operator(operator):
    pass

def find_service_with_max_fare():
    pass

def find_service_with_min_fare():
    pass

def find_service_with_long_duration():
    pass

def find_service_with_short_duration():
    pass



