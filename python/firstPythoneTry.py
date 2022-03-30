def EdediYaz(sayi):
    if sayi >0:
        EdediYaz(sayi - 1)
        print(sayi)
 
 
EdediYaz(30)