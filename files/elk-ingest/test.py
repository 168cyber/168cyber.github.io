###########
# IMPORTS #
###########
import json
import socket
#####################################################
# EMPTY PYTHON DICTIONARY FOR CREATING JSON MESSAGE #
#####################################################
json_data = {}
####################
# JSON INFORMATION #
####################
my_address = "123 Muffin Ln Johnston IA, 50131"
work_addres = "321 Hingle-McKringle Ave Des Moines IA, 50321"
times_mobilized = 2
things_i_do = ['Cyber', 'Be Awesome']
my_ip = "65.158.137.2"
city = "Johnston"
state = "Iowa"
country = "US"
loc = "41.6730,-93.6977"
org = "AS209 CenturyLink Communications, LLC"
#######################
# CREATE JSON MESSAGE #
#######################
json_data['my_address'] = my_address
json_data['work_address'] = work_addres
json_data['times_mobilized'] = times_mobilized
json_data['what_i_do'] = things_i_do
json_data['my_ip'] = my_ip
json_data['my_city'] = city
json_data['my_state'] = state
json_data['country'] = country
json_data['loc'] = loc
json_data['ip_org'] = org
##################################
# PRINT TEST MESSAGE TO TERMINAL #
##################################
print(json_data)
print(json.dumps(json_data))
# ################################################
# PIPE DATA INTO ELASTICSEARCH VIA LOGSTASH PORT #
##################################################
HOST = '127.0.0.1'
PORT = 31311
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as json_data:
    sys.stderr.write("[ERROR] %s\n" % json_data[1])
    sys.exit(1)
try:
    sock.connect((HOST, PORT))
except socket.error as json_data:
    sys.stderr.write("[ERROR] %s\n" % json_data[1])
    sys.exit(2)
sock.send(str(json.dumps(json_data)).encode('utf-8'))
