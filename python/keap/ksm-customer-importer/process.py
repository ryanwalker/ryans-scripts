import sys
import time
import requests
import csv

if len(sys.argv) <= 2:
    print("\nEnsure to invoke like this example: ")
    sys.exit("python process.py http://localhost:8080 api-token\n")

KSM_BASE_URL = sys.argv[1]
API_KEY = sys.argv[2]

HEADERS = {
    'Content-Type': "application/json",
    'X-SM-ADMIN': API_KEY
}

FIVE_SECONDS = 5


def main():
    with open('customers.csv') as customers_csv:
        csv_reader = csv.reader(customers_csv, delimiter=',')

        line_number = 0

        for row in csv_reader:
            if line_number == 0:
                line_number += 1
            else:
                customer = {
                  'id': row[0],
                  'exclude_from_usage_gathering': row[1],
                  'exclude_from_usage_gathering_invoice_creation': row[2]
                }

                post_customer_to_ksm(customer)
                time.sleep(2)


def post_customer_to_ksm(customer):
    url = f'{KSM_BASE_URL}/admin/customers'

    response = requests.post(url=url, headers=HEADERS, timeout=FIVE_SECONDS,
                             json=customer)

    with open('success.txt', 'a') as success_txt,\
            open('failures.txt', 'a') as failures_txt:

        if response.status_code == 200:
            print(f'SUCCESS {customer["id"]}')
            success_txt.write(f'{customer["id"]}\n')
            success_txt.flush()
        else:
            print(f'FAIL {customer["id"]} - {response.text}')
            failures_txt.write(f'{customer["id"]} - {response.text}\n')
            failures_txt.flush()


if __name__ == "__main__":
    main()

