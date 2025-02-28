import requests
import json
url = 'https://andrewbeatty1.pythonanywhere.com/books'

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbookbyid(id):
    geturl = url + '/' + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    #headers = {'Content-Type': 'application/json'}
    #response = requests.post(url, data=json.dumps(book), headers=headers)


    
    # Check if the response is empty or an error
    if response.status_code != 200 and response.status_code != 201:  
        print(f"Error: {response.status_code}, Response: {response.text}")
        return None

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: API returned a non-JSON response")
        print("Response Text:", response.text)
        return None

def updatebook(id, bookiff):
    updateurl = url + '/' + str(id)
    response = requests.put(updateurl, json=bookiff)
    return response.json()

def deletebook(id):
    deleteurl = url + '/' + str(id)
    response = requests.delete(deleteurl)
    return response

if __name__ == '__main__':
    book = {
        'Author':"test100",
        'Title':"test100 title",
        "Price": 1276
    }
    bookiff = {
        "Price": 123
    }
    #print(getallbooks())
    #print(getbookbyid(545))
    #print(deletebook(545))
    #print(createbook(book))
    print (updatebook(545, bookiff))
          