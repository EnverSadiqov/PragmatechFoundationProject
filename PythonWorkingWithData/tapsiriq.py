
# version 01
# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# telebeler=[adlar,soyadlar]


# i=0
# while i<len(adlar):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i=i+1
    
# for i in range (len(adlar,)):  
#    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")

# version 02
# telebeler=[
#     ['Ehmed','Memmed','Sabir'],
#     ['Ehmedov','Salehov','Quliyev']
# ]
# print(telebeler[1][2])    

# i=0
# while i<len(telebeler [0]):
#     print(f"ad:{telebeler[0][i]} soyad:{telebeler[1][i]}")
#     i=i+1
    
# for i in range(len(telebeler[0])):
#    print(f"ad:{telebeler[0][i]} soyad:{telebeler[1][i]}")

# version 03

# telebe01={
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
# }

# telebe02={
#     "ad":"Memmed",
#     "soyad":"Salehov"
# }

# telebe03={
#     "ad":"Sabir",
#     "soyad":"Quliyev"
# }
# telebeler=[telebe01,telebe02,telebe03]
# i =0

# while i<3:
#     print(telebeler[i])
#     i=i+1

# for x in range(len(telebeler)):
#  print(telebeler[x])

#version 04

# telebeler=[
# {
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
# },
# {
#     "ad":"Memmed",
#     "soyad":"Salehov"
# },
# {
#     "ad":"Sabir",
#     "soyad":"Quliyev"
# }
# ]
# print(telebeler[1]["ad"])


# #version 05

telebeler={
    "adlar":['Ehmed','Memmed','Sabir'],
    "soyadlar":['Ehmedov','Salehov','Quliyev']
}

print(telebeler["adlar"][0])

i=0
while i<len(telebeler["adlar"]):
    print(telebeler["adlar"][i],telebeler["soyadlar"][i])
    i+=1
    
for i in range(len(telebeler["adlar"])):
    print(telebeler["adlar"][i],telebeler["soyadlar"][i])
