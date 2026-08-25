from datetime import datetime

staff_data = {'a':{'password':'a','role':'staff'},'arun':{'password':'Arun@123','role':'staff'}, 'roshin':{'password':'Roshin@123','role':'staff'}, 'albin': {'password':'albin@123','role':'staff'}}


patients_data = {1001:{'name':'Sumesh Kumar', 'dob': '12-12-2020', 'blood group': 'O+','gender':'M', 'phone': 9656244560, 'address': 'Trivandrum','created on':datetime.today().date().strftime("%d-%m-%Y"), 'is_active': True}}