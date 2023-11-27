import requests

def local_test():
    response = requests.post('http://localhost:5000/create-intents')
    print(response.json())

if __name__ == '__main__':
    local_test()
