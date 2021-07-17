from os import system
from time import sleep
def clear():
    system('cls')
print("Enter Your Date In The Format DD/MM/YYYY\nEnter your Birthday:6\nEnter your Birthmonth:12\nEnter your Birthyear:2000\nRange of year is(1980-2003)")
input("Press Enter To Continue...")
clear()
while(1):
    print("1.Play\n2.Exit")
    choice=int(input("Enter Your Choice:"))
    clear()
    if(choice==1):
        day = int(input("Enter your Birthday:"))
        if(day<=0 or day>21):
            print("wrong Input")
            day = int(input("Enter your Birthday:"))
        month = int(input("Enter your Birthmonth:"))
        if(month<=0 or month>12):
            print("wrong Input")
            month = int(input("Enter your Birthmonth:"))
        year = int(input("Enter your Birthyear:"))
        if(year<=1979 or year>2003):
            print("wrong Input")
            year = int(input("Enter your Birthyear:"))
        daylist = ["Someone", "a Donkey", "Monkey", "Sunny Leone", "Elephant", "Shah Rukh Khan", "Your Boyfriend", "Doremon", "Your Girlfriend", "Joker", "The Hulk", "Bin Laden", "Superman", "Macho man", "My crush", "Spiderman","Frog", "Elon Musk", "a Pepsi can", "A fisherman", "A gorrila", "An old man", "an old lady", "Dinosaur", "Tom Cruise", "Crocodile", "Pikachu", "My Best Friend", "Hippopotamus", "Your best friend", "Captian Americe"]
        monthlist = ["I need", "I killed", "I love", "I hugged", "I Slapped", "I forgot",
                    "I played with", "I jumped on", "I Drunk with", "I slept with", "I eat", "I kissed"]
        yearlist = ["in a theatre", "in a village", "in a forest", "in a swimming pool", "in a villa", "in a room", "in a bus", "in a park", "in a beach", "in a toilet", "in a zoo", "in a office","in a garden", "in a airport", "in a stadium", "in a hospital", "in a hotel", "in a balcony", "in a taxi", "in a bed", "in a river", "in a hostel", "in a play ground", "in a canteen"]
        if(month == 1):
            monthsentence=monthlist[0]
        elif(month == 2):
            monthsentence=monthlist[1]
        elif(month == 3):
            monthsentence=monthlist[2]
        elif(month == 4):
            monthsentence=monthlist[3]
        elif(month == 5):
            monthsentence=monthlist[4]
        elif(month == 6):
            monthsentence=monthlist[5]
        elif(month == 7):
            monthsentence=monthlist[6]
        elif(month == 8):
            monthsentence=monthlist[7]
        elif(month == 9):
            monthsentence=monthlist[8]
        elif(month == 10):
            monthsentence=monthlist[9]
        elif(month == 11):
            monthsentence=monthlist[10]
        elif(month == 12):
            monthsentence=monthlist[11]
        if(day==1):
            daysentence=daylist[0]
        elif(day==2):
            daysentence=daylist[1]
        elif(day==3):
            daysentence=daylist[2]
        elif(day==4):
            daysentence=daylist[3]
        elif(day==5):
            daysentence=daylist[4]
        elif(day==6):
            daysentence=daylist[5]
        elif(day==7):
            daysentence=daylist[6]
        elif(day==8):
            daysentence=daylist[7]
        elif(day==9):
            daysentence=daylist[8]
        elif(day==10):
            daysentence=daylist[9]
        elif(day==11):
            daysentence=daylist[10]
        elif(day==12):
            daysentence=daylist[11]
        elif(day==13):
            daysentence=daylist[12]
        elif(day==14):
            daysentence=daylist[13]
        elif(day==15):
            daysentence=daylist[14]
        elif(day==16):
            daysentence=daylist[15]
        elif(day==17):
            daysentence=daylist[16]
        elif(day==18):
            daysentence=daylist[17]
        elif(day==19):
            daysentence=daylist[18]
        elif(day==20):
            daysentence=daylist[19]
        elif(day==21):
            daysentence=daylist[20]
        elif(day==22):
            daysentence=daylist[21]
        elif(day==23):
            daysentence=daylist[22]
        elif(day==24):
            daysentence=daylist[23]
        elif(day==25):
            daysentence=daylist[24]
        elif(day==26):
            daysentence=daylist[25]
        elif(day==27):
            daysentence=daylist[26]
        elif(day==28):
            daysentence=daylist[27]
        elif(day==29):
            daysentence=daylist[28]
        elif(day==30):
            daysentence=daylist[29]
        elif(day==31):
            daysentence=daylist[30]
        if(year==1980):
            yearsentence=yearlist[0]
        elif(year==1981):
            yearsentence=yearlist[1]
        elif(year==1982):
            yearsentence=yearlist[2]
        elif(year==1983):
            yearsentence=yearlist[3]
        elif(year==1984):
            yearsentence=yearlist[4]
        elif(year==1985):
            yearsentence=yearlist[5]
        elif(year==1986):
            yearsentence=yearlist[6]
        elif(year==1987):
            yearsentence=yearlist[7]
        elif(year==1988):
            yearsentence=yearlist[8]
        elif(year==1989):
            yearsentence=yearlist[9]
        elif(year==1990):
            yearsentence=yearlist[10]
        elif(year==1991):
            yearsentence=yearlist[11]
        elif(year==1992):
            yearsentence=yearlist[12]
        elif(year==1993):
            yearsentence=yearlist[13]
        elif(year==1994):
            yearsentence=yearlist[14]
        elif(year==1995):
            yearsentence=yearlist[15]
        elif(year==1996):
            yearsentence=yearlist[16]
        elif(year==1997):
            yearsentence=yearlist[17]
        elif(year==1998):
            yearsentence=yearlist[18]
        elif(year==1999):
            yearsentence=yearlist[19]
        elif(year==2000):
            yearsentence=yearlist[20]
        elif(year==2001):
            yearsentence=yearlist[21]
        elif(year==2002):
            yearsentence=yearlist[22]
        elif(year==2003):
            yearsentence=yearlist[23]
        print(monthsentence , daysentence,yearsentence)
        time=5
        for i in range(0,5):
            print(f"Restarting Program In {time} Seconds...")
            time=time-1
            sleep(1)
        clear()
    else:
        exit(0)
