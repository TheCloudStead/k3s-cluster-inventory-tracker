import requests
from requests.auth import HTTPBasicAuth

from bs4 import BeautifulSoup

NC_HOST = ""
NC_USERNAME = ""
NC_PASSWORD = ""
CONVERSATION_ID = ""

def check_status():
    #url = "https://<in_stock_url>"
    url = "<actual_url>"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    item_stock_status = soup.find_all("script")
    for script in item_stock_status:
        if 'item_stock_status' in script.text:
            if '"item_stock_status":"In stock"' in script.text:
                print("In Stock")
                return True
            elif '"item_stock_status":"Out of stock"' in script.text:
                print("Out of Stock")
                return False

def send_message():
    MESSAGE = "@<user_id> Light is available!"
    API_URL = f"{NC_HOST}/ocs/v2.php/apps/spreed/api/v1/chat/{CONVERSATION_ID}"
    HEADERS = {'OCS-APIRequest': 'true','Accept': 'application/json',}
    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            auth=HTTPBasicAuth(NC_USERNAME, NC_PASSWORD),
            data={'message': MESSAGE},
        )

        if response.status_code == 201:
            print(f"Message sent successfully to conversation {CONVERSATION_ID}! 🚀")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    light_status = check_status()
    if light_status == True:
        send_message()