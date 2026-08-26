from datetime import datetime

employee_data = {'a':{'password':'a','role':'admin'},'r':{'password':'r','role':'receptionist'},'p':{'password':'p','role':'pharmacist'},'l':{'password':'l', 'role':'lab technician'} , 'admin':{'password':'admin@123','role':'admin'}, 'receptionist':{'password':'receptionist@123','role':'receptionist'}, 'pharmacist': {'password':'pharmacist@123','role':'pharmacist'}, 'technician': {'password':'technician@123','role':'lab technician'}}


patients_data = {100001:{'name':'Sumesh Kumar', 'dob': '12-12-2020', 'blood group': 'O+','gender':'M', 'phone': 9656244560, 'address': 'Trivandrum','created on':datetime.today().date().strftime("%d-%m-%Y"), 'is_active': True}}

staff_data = {1001:{'name':'Ramesh Kumar', 'dob': '12-12-2020', 'phone': 9656244560, 'address': 'Trivandrum','doj': datetime.today().date().strftime("%d-%m-%Y"), 'salary':25000, 'is_active': True}}

medicine_data = {101:{'medicine name':'paracetamol', 'company name': 'Para ceta Pharma', 'generic name': 'Paracetamol', 'quantity':5000, 'price':50000, 'is_active': True}}

test_data = {101:{'test name':'BP test','low range':'80', 'high range': '120', 'unit':'mmHg', 'price':750, 'is_active': True}}