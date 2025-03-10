""""
 O
*|*
 |
* *
"""
class AdamAsmaca():
    def __init__ (self , s):
        self.s=s

    def game(self):
        point=6
        people=list()
        wordsizelist=list()
        wordd=list()
        numberPeople=int(input("oyuncu sayısını giriniz"))
        for i in range(1,numberPeople):
            peopleName=input(f"{i}.kişi ismini:")
            people.append(peopleName)
        

        follow=0
        while follow<numberPeople:
            who=people[follow+1]
            towho=people[follow]
            word=input(f"{who} , {towho} kişisi için bir kelime girsin!")
            wordsize=len(word)

            for i in range(0,wordsize):
                wordsizelist.append("_")
            print(wordsizelist)
            
            estimate=wordsize+(wordsize/3)
            while True:
                letter=input("Harf tahmininde bulununuz")
                estimate-=1
                for i in word:
                    if i==letter :
                        p=True
                        wordd.append(letter)
                        for j in word:
                            for z in wordd:
                                if z==j :
                                    print(end=z)
                                    
                                
                                elif oky==False:
                                    print(end=" _ ")
                                    oky=True
                            oky=False



                if(p==False):
                    point-=1  
                p= False
                print(".\n.\n.\n.\n")
                if(point==6):
                    print(" O\n/|\\\n |\n/ \\")   
                    print("Mükemmeliiizz Aşkım!")
                elif(point==5):
                    print(" O\n*|*\n |\n*")
                    print("Eyvah! Bir bacak koptu!")
                elif(point==4):
                    print(" O\n*|*\n |")
                    print("Eyvah eyvah! İkinci bacak da gitti!")
                elif(point==3):
                    print(" O\n*|\n |")
                    print("Neee yapıyorsuun! Bacaklarındn sonra kollarından birini de kaybettiiin!")
                elif(point==2):
                    print(" O\n | \n |")
                    print("Püü sana! Ne kolun ne bacağın kaldı")
                elif(point==1):
                    print("  \n | \n |\n")  
                    print("Kafasız kafanı da kaybettin! PPPÜÜÜ SANA!")
                    break
                if(point==1):
                    print(f"{who} için GAME OVER")
                elif(estimate==0):
                    print(f"{who} için GAME OVER")

                wl=len(wordd)
                if(wl==wordsize):
                    print(f"{who} KAZANDIN AŞKIMM!")


                                 

                                       
                print("""
                
                """)


oz=AdamAsmaca(26)
oz.game()
