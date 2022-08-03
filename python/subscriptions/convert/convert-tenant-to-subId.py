import chargebee
import sys
import time
import requests

if len(sys.argv) <= 2:
    print("\nEnsure to invoke like this example: ")
    sys.exit("python convert-tenant-to-subId.py [intg|stge|prod] ksm-api-token\n")

env = sys.argv[1]
api_key = sys.argv[2]

def main():
    with open('convert.txt') as file, open('errors.txt', 'a') as errors, open('converted.txt', 'a') as converted:
        items = file.readlines()
        for tenant in items:
            tenant = tenant.strip()
            try:
                subId = convertTenantToSubId(tenant)
                print(f'Converted tenant {tenant} to subId {subId}')
                converted.write(f'{subId}\n')
                converted.flush()
            except Exception as e:
                print(f'Error converting tenant {tenant}, see errors.txt')
                errors.write(f'{tenant}: {e}\n')
                errors.flush()


def convertTenantToSubId(tenant):
    global env
    global api_key

    headers = {
        'Content-Type': 'application/json',
        'X-SM-TENANTS-APIKEY': api_key
    }
    environment = env
    if environment == "prod":
        environment = ""
    else:
        environment = f'{environment}.' # add a '.'

    url = f'https://subscription-management-service.{environment}keapapis.com/v1/subscriptions?filter=tenant_id="{tenant}"'

    r = requests.get(url, headers=headers)
    return r.json()['subscriptions'][0]['subscription_id']

if __name__ == "__main__":
    main()
