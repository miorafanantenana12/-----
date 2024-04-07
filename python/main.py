import requests

def get_response(question):
    api_key = "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"
    endpoint = "https://azeu-api-beta.onrender.com/GlobalGPT"
    params = {"question": question, "apiKey": api_key}

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch response."}

question = input("Entrez votre question : ")
response = get_response(question)
print(response)
