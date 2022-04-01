# arr=[1,34,23,90,230,1400,600,300,240] bu listi nəzərə alaraq aşağıdakı problemləri həlledin
# (2) Ən böyük 3 ədədi ekrana çap edin
# (3) Ədədlərin ortalamasından böyük olan ədədləri ekrana çap edin
# (4) 2 rəqəmli ədədləri ekrana çap edin.
# (5) Bu listin içərisində olan ədədlərin rəqəmlərinin cəmini ekrana çap edin (nüm: 34->3+4=7)
# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
# (7) Bütün ölkələrin hərf sayını tapın Link
# (8)  Ən uzun ölkə adını tapın
# (9)  Daxilində A hərfi olan ölkələri tapın


 # Ən böyük 3 ədədi ekrana çap edin: 2-ci tapsiriq hell oldu
# arr= [1,34,23,90,230,1400,600,300,240] 
# arr.sort() 

# print("1. Boyük Sayı:", arr[-1])
# print("2. Boyük Sayı:", arr[-2])
# print("3. Boyük Sayı:", arr[-3])

# Ədədlərin ortalamasından böyük olan ədədləri ekrana çap edin : 3cu tapsiriq hell oldu
# arr=[1,34,23,90,230,1400,600,300,240]
# print (sum(arr))
# print(2918//9)

#####2 rəqəmli ədədləri ekrana çap edin :4cu hell olundu
# arr= [1,34,23,90,230,1400,600,300,240] 
# def ikiliededleritap():
#     for eded in arr:
#         if eded>10 and eded<100:
#             print(eded)
# ikiliededleritap()
        
    


# #Bu listin içərisində olan ədədlərin rəqəmlərinin cəmini ekrana çap edin :5ci tapsiriq hell oldu

# arr=[1,34,23,90,230,1400,600,300,240]
# def ededlerinreqemlerinceminitap():
#     for eded in arr:
#         cem=0
#         for reqem in str (eded):
#             cem=cem+int(reqem)
#             print(cem)
            
# ededlerinreqemlerinceminitap()


##### Bütün ölkələrin hərf sayını tapın:7 ci tapsiriq hell olundu
# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
# def herfsayitap():
#     for country in countries:
#         print(country, len(country))      
# herfsayitap()


# Ən uzun ölkə adını tapın: 8ci tapsiriq hell oldundu
# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
# print(max(countries, key=len))


#  Daxilində A hərfi olan ölkələri tapın :9ci  tapsiriq  hell oldu
# countries= ("Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan")
# x = countries.count("a")
# for x in countries:
#     z = countries.count("a")
#     x = countries.count("A")
# print(x)  
# print(z) 


