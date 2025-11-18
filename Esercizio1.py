letture = []

def aggiungi(id, temp):
    letture.append({"id" : id, "temp": temp})
    
    
def media_temp():
    somma = 0
    conta = 0
    for l in letture:
        somma += l["temp"]
        conta += 1
    if not letture:
        return None
    return somma / conta
    

for id, temp in [(1, 31.1), (2, 29.8), (3, 30.5), (4, 32.0), (5, 28.9), (6, 30.2)]:
    aggiungi(id, temp)

print(media_temp())