# ;arr = [10,20,30,20,10,50,60,40,80,50,40]


# ; 1 Verilən listdəki ədədlərin kvadratlarını hesablayaraq ayrı bir listin içərisində toplayın


# ; 2 Verilən listin içərisəndə təkrarlanan dəyərləri silərək geri qalan deyerlerin olduğu list yaradın


# ; 3 Verilən listdə cüt yerdə duran ədədlərlə tək yerdə duran ədədlərin yerini dəyişdirin  


# ;Aşağıdakı şərtləri yerinə yetirən proqram yazın


#  input metodu vasitəsi ilə istifadəçidən username və password yazmasını tələb edin


# ; 4 daxil edilən username və password admin,123456 dəyərlərinə bərabərdirsə ekranda "Sistemə daxil oldunuz təşəkkür edirik" mesajı göstərilsin


# ; 5 daxil olunan username və password-dan hər hansı boş buraxılıbsa ekranda "Dəyərlər boş buraxıla bilməz" mesajı göstərilsin


# ; 6 daxil edilən dəyərlərdən hər hansı biri səhvdirsə hansı dəyərin səhv olduğunu göstərən mesaj göstərilsin


# ; Şans oyunu yazın.Tələblər aşağıdakı kimidir


# ;7 İstifadəçi ekrandan 1-20 arasında sıra ilə 3 ədəd daxil edir. (məsələn 3,14,18)


# ; 8 Sistem 1-20 arasında təsadüfi 3 ədəd seçir


# ; 9 İstifadəçinin daxil etdiyi dəyərlər ilə sistem tərəfindən seçilən dəyərlər üst üstə düşürsə ekrana təbrik edirik mesajı yazılsin.


# ; 10 İstifadəçiyə bu əməlyatı təkrarlamaq üçün 3 şans verilsin


# ; 11 3 haqqını istifadə etdikdən sonra "Siz oyunu uduzdunuz " mesajı verilsin


#### ----------1 Verilən listdəki ədədlərin kvadratlarını hesablayaraq ayrı bir listin içərisində toplayın--- helll oldu----------
# arr = [10,20,30,20,10,50,60,40,80,50,40]
# x = list(map(lambda x: x ** 2, arr))
# def ededlerinkvadrati():
#     return arr
# print("listdəki ədədlərin kvadratlarını:")
# print(arr)

# arr = [10,20,30,20,10,50,60,40,80,50,40]
# arr = list(set(arr))
# print(arr)

####------------2 Verilən listin içərisəndə təkrarlanan dəyərləri silərək geri qalan deyerlerin olduğu list yaradın--- hell oldu------

# arr = [10,20,30,20,10,50,60,40,80,50,40]
# arr2 = []
# for a in arr:
#  if a not in arr2:
#     arr2.append(a)
# print(arr2)

####------------3 Verilən listdə cüt yerdə duran ədədlərlə tək yerdə duran ədədlərin yerini dəyişdirin------tam basa dusmedim
# arr = [10,20,30,20,10,50,60,40,80,50,40]
# arr.reverse()
# print(arr)


####-------4 daxil edilən username və password admin,123456 dəyərlərinə bərabərdirsə ekranda---- hell edildi "Sistemə daxil oldunuz təşəkkür edirik" mesajı göstərilsin            
# x=0
# while x<1:
#     username=input('username?')
#     password=input('password?')
#     if username=='admin'and password=='123456':
#        print('Sistemə daxil oldunuz təşəkkür edirik!')
#     else:
#         x+=1
#         print('Sistemə daxil ola bilmediz!')
        
        
#### ---------  5daxil olunan username və password-dan hər hansı boş buraxılıbsa ekranda "Dəyərlər boş buraxıla bilməz" mesajı- hell olundu
# username = "admin"
# password = "123456"

# istifadeci_adi = input("Adınızi Girin: ")
# sifre = input("Şifreyi Girin: ")

# if (istifadeci_adi == username) and (sifre != password):
#     print("Şifre yanlış..")
# elif (istifadeci_adi != username) and (sifre == password):
#     print("Dəyərlər boş buraxıla bilməz")
# elif (istifadeci_adi != username) and (sifre != password):
#     print("Dəyərlər boş buraxıla bilməz")
# else:
#     print("Giriş yapıldı!")

####-----------6 daxil edilən dəyərlərdən hər hansı biri səhvdirsə hansı dəyərin səhv olduğunu göstərən mesaj göstərilsin--- helll edildi
# username = "admin"
# password = "123456"

# istifadeci_adi = input("Adınızi Girin: ")
# sifre = input("Şifreyi Girin: ")
# if (istifadeci_adi == username) and (sifre != password):
#     print("dəyərde səhvlik var.")
# elif (istifadeci_adi != username) and (sifre == password):
#     print("dəyərde səhvlik var  ")
# elif (istifadeci_adi != username) and (sifre != password):
#     print("dəyərde səhvlik var ")
# else:
#     print("Giriş yapıldı!")



