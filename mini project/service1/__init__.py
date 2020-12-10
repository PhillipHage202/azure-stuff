import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey, exceptions



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letterstring = requests.get('https://genletters.azurewebsites.net/api/service2?code=0PIZjZ5krmmlkIeoW1vwD40ezvlnUUWgIQYe3kLneP/BAoAkTa0TDA==').text
    numstring = requests.get('https://gennum.azurewebsites.net/api/service3?code=Dpsg85A2oaWewTtawMoAS9q6vObDsbF/1WvHBaasrr7Si9QJEFBPGQ==').text
    
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += numstring[i]
    
   
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)

    return username

