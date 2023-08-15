from azure.storage.blob import BlobServiceClient
from storages.backends.azure_storage import AzureStorage
from .settings import AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY, AZURE_CONTAINER

class AzureMediaStorage(AzureStorage):
    account_name = AZURE_ACCOUNT_NAME
    account_key = AZURE_ACCOUNT_KEY
    azure_container = AZURE_CONTAINER
    expiration_secs = None