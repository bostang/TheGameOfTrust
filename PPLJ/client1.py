import requests
import json

def http_client():
    target_ip = "10.8.102.108"
    user_input = input("Enter data to send to the HTTP server: ")
    data_list =user_input.split(',')
    json_data = json.dumps(data_list)
    url = f'http://{target_ip}:8080?data={json_data}'
    response = requests.get(url)
    print('HTTP Server Response:', response.text)

if __name__ == '__main__':
    while(1):
        http_client()