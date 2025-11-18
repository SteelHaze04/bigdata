letture = []

def aggiungi(id, temp):
    letture.append({"id" : id, "temp": temp})
    
    
def media_temp():
    if not letture:
        return None
    return sum(x["temp"] for x in letture) / len(letture)
    

for _id, _temp in [(1, 31.1), (2, 29.8), (3, 30.5), (4, 32.0), (5, 28.9), (6, 30.2)]:
    aggiungi(_id, _temp)

print(media_temp())