import random
print("============================")
print("====WELCOME TO WAW STORE====")
print("============================")
money = random.randint(250,5000)
print(f'\n====Your budget is :{money}====\n')
buyedLaptop = []
class Laptop :
    def __init__(self,id,merk,name,ram,storage,cpu,screen,price,special):
        self.id = id
        self.merk = merk
        self.name = name
        self.ram = f'{ram} GB'
        self.storage = f'{storage} GB'
        self.cpu = cpu
        self.screen = screen
        self.price = price
        self.special = special
    
    
    def details(self) : 
        return(f'You have selected Laptop no. {self.id}\n\n|{self.merk} {self.name} |\n|CPU | {self.cpu} |\n|RAM | {self.ram} |\n|Stogare | {self.storage} |\n|Screen | {self.screen} |\n|For only ${self.price},00 |\n|Whats special about this laptop is {self.special}|\n')
        

laptop0 = Laptop(0,'Axioo',"MyBook Z6",8,"NVME 256","Intel i3 1215U","FHD IPS",299,"Very suitable for office task")
laptop1 = Laptop(1,'Axioo',"Hype 5 Gen 12",16,"NVME 512","Intel i5 1235U","FHD IPS",349,"High core for multitasking")
laptop2 = Laptop(2,'Advan',"Workmate",8,"NVME 256","Ryzen 5 3500U","FHD IPS",249,"Affordable laptop for student")
laptop3 = Laptop(3,'Advan',"AI GEN",16,"NVME 512","Ryzen 7 8845HS","FHD IPS",599,"HIghly integrated A.I")
laptop4 = Laptop(4,'Asus','Vivobook',16,"NVME 512","Intel i5 13420H","FHD LED",549,"Clear and Bright LED screen")
laptop5 = Laptop(5,'Asus','ROG',64,"NVME 4096","Intel Ultra 9 275HX","2.5K MIni-LED",4999,"RTX 5090")
laptop6 = Laptop(6,'Acer','Swift',32,"NVME 512","Intel Ultra 5 125H","2.5K OLED",759,"OLED Screen and Intel ARC GPU")
laptop7 = Laptop(7,'Acer','Aspire',16,"NVME 512","Intel i5 12450H","FHD IPS",569,"RTX 3050 and 144Hz screen")
laptop8 = Laptop(8,'Zyrex','L-BOOK',8,"EMMC 256","Intel Celeron N4020","HD TN/VA",149,"Very affordable laptop")
laptop9 = Laptop(9,'Zyrex','D-TECH PRO',16,"NVME 512","Ryzen 5 6600H","FHD IPS",149,"Clean looking affordable but fast laptop")


laptops = [
    laptop0,
    laptop1,
    laptop2,
    laptop3,
    laptop4,
    laptop5,
    laptop6,
    laptop7,
    laptop8,
    laptop9,
]

print("Welcome to the store,Come check our products \n")
for i in laptops : 
    print(f'{i.id}.{i.merk} {i.name}')
while(True):
    q = int(input("Choose between product 1 to 4 , example (1) \nselect product : "))
    isFound = False
    for i in laptops :
        if(i.id==q):
            print(i.details())
            isFound = True
            b=input(f'Do you wanna buy this laptop for ${i.price},00? Current Balance ${money},00\n (Y / N) : ')
            if(b=='Y' or b == 'y'):
                if(money >= i.price) :
                    money = money- i.price
                    print(f'Succesfully buying {i.merk} {i.name},\nNow your balance is {money}')
                    buyedLaptop.insert(0,f'{i.merk} {i.name} , {i.price}')
                    break
                else :
                    print("Sorry,insuffisence balance")
            break
    if(isFound==False):
        print("There is no laptop with that id")
    
    print("\n \nThis the list is your laptop/s\n")
    for i in buyedLaptop :
        print(f'-{i}')
    print(f'\nYour current balance is {money}')