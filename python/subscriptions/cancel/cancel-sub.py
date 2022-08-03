import chargebee
import sys
import time
import requests

if len(sys.argv) <= 2:
    print("\nEnsure to invoke like this example: ")
    sys.exit("python cancel-sub.py [keapint-test|keapnew-test|keapnew] chargebee-api-token\n")

chargebee_host_name = sys.argv[1]
chargebee_api_token = sys.argv[2]

chargebee.configure(chargebee_api_token, chargebee_host_name)
#
def main():
    with open('to-cancel.txt') as file, open('errors.txt', 'a') as error_apps, open('cancelled.txt', 'a') as cancelled_apps:
        items = file.readlines()
        for id in items:
            id = id.strip()

            print(f'Acting on {id}')

            try:
                # end_of_term: false, will cancel immediately
                result = chargebee.Subscription.cancel_for_items(id, {"end_of_term" : "false"})
                print('cancelling subId:', result.subscription.id)
                cancelled_apps.write(f'{id}\n')
                cancelled_apps.flush()
            except IOError as e:
                print(f'IOError {e}')
                error_apps.write(f'{id} errored\n')
                error_apps.flush()
            except chargebee.InvalidRequestError as e:
                print('Chargebee InvalidRequestError, ' + str(id))
                print(e)
                error_apps.write(f'{id}\n')
                error_apps.flush()
            except e:
                print(f'Generic exception occurred {e}')
                error_apps.write(f'{id}\n')
                error_apps.flush()

            time.sleep(2)

if __name__ == "__main__":
    main()
