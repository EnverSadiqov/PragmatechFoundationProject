# quote="""Programming isn't about what you know; it's about what you can figure out."""
# 1  quote daxilində necə xarakter olduğunu tapın 
# 2  quote daxilində necə boşluq olduğunu tapın 
# 3  quote ifadəsini sözlərini ayrı ayrı ekrana çap edin 
# 4  quote daxilində olan ' işarəsini silərək yeni əldə edilən ifadəni ekrana çap edin
# 5  quote daxilində necə hərf olduğunu tapın 
# 6  quote daxilində necə ədəd o hərfi olduğunu tapın
# nums=[23,56,78,100,14,70,300,236]
# 7  list-i tərs çevirərək ekrana çap edin 
# 8  sadəcə iki reqemli ededlerin cemini tapin


      ####1 quote daxilində necə xarakter olduğunu tapın- hell oldu###
# quote="""Programming isn't about what you know; it's about what you can figure out."""
# print(len(quote))

      ####2quote daxilində necə boşluq olduğunu tapın- hell oldu#### 
quote="""Programming isn't about what you know; it's about what you can figure out."""
def bosluqlaritap(quote):
    cem = 0
    for i in quote:
        if i == " ":
            cem += 1   
    return cem
print("bosluklarin sayisi-",bosluqlaritap(quote))


      #### 4 quote daxilində olan ' işarəsini silərək yeni əldə edilən ifadəni ekrana çap edin-hell oldu###
# quote = "Programming isn't about what you know; it's about what you can figure out."
# a = quote.replace("'", " ")
# print(a)

      #### 5 quote daxilində necə hərf olduğunu tapın
# quote = "Programming isn't about what you know; it's about what you can figure out."
# print(len(quote))


      #### 6 quote daxilində necə ədəd o hərfi olduğunu tapın- HELL OLUNDU
# quote="""Programming isn't about what you know; it's about what you can figure out."""      
# print(quote.count("o"))
# print(quote.count("O"))    
  
      #### 7 list-i tərs çevirərək ekrana çap edin- hell oldu###
# nums = [23,56,78,100,14,70,300,236] 
# def Ters(nums): 
#     nums.reverse() 
#     return nums 
# print(Ters(nums))

     ####  8  sadəcə iki reqemli ededlerin cemini tapin-hell oldu
# nums= [23,56,78,100,14,70,300,236] 
# def ikiliededleritap():
#     for eded in nums:
#         if eded>10 and eded<100:
#             print(eded)
# ikiliededleritap()