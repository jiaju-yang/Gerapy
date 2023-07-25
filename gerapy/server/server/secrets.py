from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


def get_secret(key_vault_name):
    key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=key_vault_uri, credential=credential)
    return lambda secret_name: client.get_secret(secret_name).value
