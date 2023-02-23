import json

with open ('sample') as file: 
    data = json.load(file)
    print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
i=1
for x in data['imdata']:
    l1=x["l1PhysIf"]
    att=l1["attributes"]
    
    while i<4:
        print(att["dn"], "                            ", att["speed"], " ", att["mtu"])
        i+=1


