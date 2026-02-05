import requests

n8n_url = "http://localhost:5678/webhook/7b7fe729-2e7e-43fe-a1ac-6aeb01ab4a5a"

prompt = "who is Casillas? explain about 30 words"

payload = {"message": prompt}
response = requests.post(n8n_url, json=payload).json()
print(response)
