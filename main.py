import requests

def getApiResponse():
    try:
        res = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10&offset=200")

        if res.status_code == 200:
            print(res.json())

        else:
            raise Exception
            
    except:
        print("Error!")



#testing 2
getApiResponse()