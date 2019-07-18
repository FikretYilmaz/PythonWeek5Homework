"""
*ODEV 1: ADAM ASMACA*
  -Onceden belirlenmis bir kelime degiskene atanacak ve kullanicidan bu kelimeyi harf tahminleriyle bilmesi istenecek.
  -Kullanicinin 6 hamle sansi olacak ve her bir yanlis hamlesinde kalan hamle sayisini gosterin. Ayrica yine her bir
  yanlis hamle sonucunda adam asmaca oyunu oynarken cizdigimiz yanlis hamle sonucundaki cizimleri sizde ekranda
  karakterleri kullanarak gosterin.
  -Kullanici harf disinda bir karakter girdiginde gerekli uyariyi yapin ve bunu da yanlis hamle olarak saymayin. Oyun devam etsin.
  -Bir yanlis ve bir dogru hamle yapilmis ornek kod ciktisi:
                           ____
                          |       |
                          |      O           5 HAKKINIZ KALDI!!!
                          |
                          |
                         ---
           - a -  -  -  - a -
          harf:
"""
pics = [ """
       +---+
       |   |
       |   O 
       |
       |
       |
=========""", """
       +---+
       |   |
       |   O
       |   |
       |
       |
=========""", """
       +---+
       |   |
       |   O
       |  /|
       |
       |
=========""", """
       +---+
       |   |
       |   O
       |  /|\\
       |
       |
=========""", """
       +---+
       |   |
       |   O
       |  /|\\
       |  /
       |
=========""", """
       +---+
       |   |
       |   O
       |  /|\\ 
       |  / \\
       |
========="""]

answer= ("fikret")
counter = 0
#guess=[]
key= len(answer)*[" - "]
while counter < 6:
    print(*key)
    guess=input("Please Enter A Letter: ")
    guess= guess.lower()
    #print(pics[counter], 'This is Your {}.Rihgt'.format(counter+1))
    answer2= list(answer)
    index=0
    if len(guess) !=1 or guess.isalpha()== False:
        print("You Can Only Enter One Character and It Must Be Letter")

    else:
        if not guess in answer2:
            counter += 1
            print("Wrong Letter")
        else:
            for i in answer2:
                if guess == i:
                    key[index] = guess
                    print(*key)
                index += 1
    if key == answer2:
        print("You won!")
    if counter == 6:
        print('You lost! The word was', answer)
    else:
        print(pics[counter], 'This is Your {}.Rihgt'.format(counter))