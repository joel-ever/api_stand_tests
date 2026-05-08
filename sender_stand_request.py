#----------------------------EJERCICIO 01 ---------------------------------------
import configuration
import requests

#def get_docs():
#   return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
#response = get_docs()
#print(response.status_code)
#----------------------------EJERCICIO 02 ---------------------------------------
#import configuration
#import requests
#def get_logs():
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
#response = get_logs()
#print(response.status_code)
#print(response.headers)
#----------------------------EJERCICIO 03 ---------------------------------------
#import configuration
#import requests

#def get_logs():
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})
#response = get_logs()
#print(response.status_code)
#print(response.headers)
#----------------------------EJERCICIO 04 ---------------------------------------
def get_user_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_user_table()
print(response.status_code)
#----------------------------EJERCICIO 05 ---------------------------------------
import data
def post_new_user(body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
#----------------------------EJERCICIO 06 ---------------------------------------
#import configuration
#import requests
#import data
#def post_products_kits(products_ids):
#    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
#                         json=products_ids,
#                         headers=data.headers)
#response = post_products_kits(data.product_ids)
#print(response.status_code)
#print(response.json())
