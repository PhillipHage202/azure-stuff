import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey, exceptions


endpoint = "https://peehage202.documents.azure.com:443/"
key = "kILpCMZAwpelpDZMAxawxHM7pgETsCi4kiWY1qB9XZMP3CaHfCw74LUEZeWMwsLtEEmd6Vfmi6iMcJuvEyghIg=="
client = CosmosClient(endpoint, key)

database_name = "user"
database=client.create_database_if_not_exists(id=database_name)

container_name = "User"
container = database.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path="/username"), offer_throughput=400)




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

