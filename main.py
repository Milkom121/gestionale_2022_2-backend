from customer_dao import CustomerDao
from reservation_dao import ReservationDao
import json

newCustomer = {
    "phoneNumber": "12345678990",
    "idToken": "123654789",
    "name": "mario",
    "surname": "mario",
    "email": "mario@mario.mario",
  }

#customerJson = json.dumps(newCustomer)

def testInsertCustomer(map):
    customerDao = CustomerDao()
    customerDao.insertCustomer(map)

def testUpdateCustomer(map):
    customerDao = CustomerDao()
    customerDao.editCustomer(map['idToken'], {'name' : 'michele'})




testInsertCustomer(newCustomer)

testUpdateCustomer(newCustomer)





# newCustomer = {
#     "phoneNumber": "",
#     "idToken": "",
#     "name": "",
#     "surname": "",
#     "email": "",
#   }
#
# customerJson = json.dump(newCustomer)
#
#
#
# def testInsertReservation(reservationJson):
#     reservationDao = ReservationDao()
#     reservationDao.insertReservation(reservationJson)
