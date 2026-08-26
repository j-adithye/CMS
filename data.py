from datetime import datetime

employee_data = {'a':{'password':'a','role':'staff'},'b':{'password':'b','role':'admin'},'p':{'password':'p','role':'pharmacist'},'arun':{'password':'Arun@123','role':'staff'}, 'roshin':{'password':'Roshin@123','role':'staff'}, 'albin': {'password':'albin@123','role':'staff'}}


patients_data = {100001:{'name':'Sumesh Kumar', 'dob': '12-12-2020', 'blood group': 'O+','gender':'M', 'phone': 9656244560, 'address': 'Trivandrum','created on':datetime.today().date().strftime("%d-%m-%Y"), 'is_active': True}}

staff_data = {1001:{'name':'Ramesh Kumar', 'dob': '12-12-2020', 'phone': 9656244560, 'address': 'Trivandrum','doj': datetime.today().date().strftime("%d-%m-%Y"), 'salary':25000, 'is_active': True}}

medicine_data = {101:{'medicine name':'paracetamol', 'company name': 'Para ceta Pharma', 'generic name': 'Paracetamol', 'quantity':5000, 'price':50000, 'is_active': True}}

test_data = {101:{'test name':'BP test','low range':'80', 'high range': '120', 'unit':'mmHg', 'price':750}}