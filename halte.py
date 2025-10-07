print("Welcome to Halte Information System")
halte1 = [
    "Kemayoran",
    "Lapangan Banteng",
    "Pasar Baru",
    "Juanda"
]
halte2 = [
    "Matraman",
    "Senen Sentral",
    "Sunter",
    "Utan Kayu Rawamangun"
]

for i in halte1 :
    print(f'Halte Berangkat : {i}')
for i in halte2 :
    print(f'Halte Tujuan : {i}')
    
class Halte :
    def __init__(self,nama,koridor,landmark):
        self.nama = nama
        self.koridor = koridor 
        self.landmark = landmark
    
    def goToMonas(self):
        for i in halte1 : 
            if(self.nama==i) : 
                if(i=='Kemayoran'):
                    print(f'Naik 14 ke arah Senen lalu transit di Senen Toyota Rangga untuk naik 2 dan turun di halte balai kota')
                elif(i=='Lapangan Banten'):
                    print(f"Naik 5 ke arah Ancol lalu transit di Pasar Baru Timur untuk naik 10 / 14A dan turun di halte Janda")
                else :
                    print(f'Naik 2 lalu turun di halte Monumen Nasional')
                return
            else :
                print(f'Gagal mengambil data halte {self.nama}')
                
                
halteB1 = Halte("Kemayoran","14","Patung Ondel Ondel")
halteB2 = Halte(halte1[1],"5/5C/6H/12B","SMA dan SMK Negeri 1")
halteB3 = Halte(halte1[2],"5/7U/10H/12B/14A","Kali")
halteB4 = Halte(halte1[3],"1A/2/2A/5C/7F/10H/12B/14A","Kali")

halteB1.goToMonas()
halteB1.goToMonas()
halteB1.goToMonas()
halteB1.goToMonas()

