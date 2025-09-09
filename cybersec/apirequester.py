import requests

def main():
    endpoint = input('Please enter the API endpoint to request: ')
    response = requests.get(endpoint)
    if response.status_code == 200:
        print('Data received')
        data = response.json()
    else:
        print('No data found')
    saveData(data)

def saveData(data):
    with open("jsonoutput.txt", 'a') as file:
        for line in data:
            file.write(str(line) + '\n')

main()