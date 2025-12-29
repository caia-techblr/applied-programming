#from flightdb_ops import *
from flightdb_ops import add_service
from flightdb_ops import list_all_services

if __name__ == "__main__":
    add_service("Indigo", "6E205", "Bengaluru", "Delhi", "1000")
    add_service("AirXPress", "AI405", "Chennai", "Hyderabad", "500")
    list_all_services()
