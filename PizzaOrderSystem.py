import csv 
import datetime 
import time
#menuyu bir txt dosyasına yazıdmak
with open("Menu.txt", "w") as f:
    f.write("Lütfen bir Pizza Tercihinizi Yapınız:\n")
    f.write("1: Klasik\n")
    f.write("2: Margarita\n")
    f.write("3: TurkPizza\n")
    f.write("4: DominosPizza\n")
    f.write("\n")
    f.write("ve Sos seçimleriniz:\n")
    f.write("11: Zeytin\n")
    f.write("12: Mantar\n")
    f.write("13: KeçiPeyniri\n")
    f.write("14: Et\n")
    f.write("15: Soğan\n")
    f.write("16: Mısır\n")
    f.write("\n")
    f.write("Teşekkür Ederiz!")
#Burayda Pizza sınıfı oluşturuyoruz
#init metodu ile parametreleri tanımlıyoruz
class Pizza: 
    def __init__(self, description='Pizza', cost=0):
        self.description = description 
        self.cost = cost 
    
    def get_description(self): 
        return self.description 

    def get_cost(self): 
        return self.cost
#Pizza alt sınıfları oluşturuyoruz ve fiyat tanımlamalarını yapıyoruz
class KlasikPizza(Pizza): 
    def __init__(self):
        super().__init__('Klasik Pizza', 45) 

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 75)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Turk Pizza', 90)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__('Dominos Pizza', 55)

#dekarator super sınıflarını oluşturduk.
class Decorator(Pizza): 
    def __init__(self, component, description, cost): 
        self.component = component
        self.description = description
        self.cost = cost 
    
    def get_cost(self): 
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self): 
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Tüm dekarator alt sınıflarının fiyatlarını tanımlıyotuz
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Zeytin, ', 11)

class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mantar, ', 15)

class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Keci Peyniri, ', 18)

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Et, ', 30)

class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Soğan, ', 8)

class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mısır, ', 12)

# database de tutmak üzere csv kütüphanesinden faydalanıyoruz
       
def write_to_csv(isim, tc, kk, son_hesap, odeme_tarih, kart_psw):
    try:
        with open("Orders_Database.csv") as csv_f:
            pass
        with open("Orders_Database.csv", "a") as csv_file:
            fieldnames = ['isim', 'tc', 'kk', "son_hesap", "odeme_tarih", "kart_psw"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {"isim": isim, "tc": tc, "kk": kk, "son_hesap": son_hesap, "odeme_tarih": odeme_tarih,
                 "kart_psw": kart_psw})
    except:
        with open("Orders_Database.csv", "w") as csv_file:
            fieldnames = ['isim', 'tc', 'kk', "son_hesap", "odeme_tarih", "kart_psw"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {"isim": isim, "tc": tc, "kk": kk, "son_hesap": son_hesap, "kart_psw": kart_psw, 
                 "odeme_tarih": odeme_tarih})

def main():
    while True:
        print('Pizzacımıza Hosgeldiniz!\n\nMenum:\n')
        print(open('Menu.txt', 'r').read())
                    
         # Pizza seçimi için kontrol sağlayan döngü
        while True:
            try:
                pizza_sec = int(input("Lütfen bir pizza seçiniz (1-4): "))
                if pizza_sec < 1 or pizza_sec > 4:
                    print("Lütfen geçerli bir seçim yapınız.")
                else:
                    break
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")

        # Sos seçimi için boş liste açıyoruz
        sos_list=[]
        while True:
            try:
                sos_sec = int(input("Lütfen bir sos seçiniz (11-16)\n(Ödemeye geçmek için '0' basınız.):"))
                if sos_sec==0:
                    break
                elif sos_sec < 11 or sos_sec > 16:
                    print("Lütfen geçerli bir seçim yapınız.")
                else:
                    sos_list.append(sos_sec)
                    continue
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")
        print(sos_list)
        while sos_sec==0:
        # Seçilen pizza ve sosların fiyatlarını hesaplama
            if pizza_sec == 1:
                pizza = KlasikPizza()
                break
            elif pizza_sec == 2:
                pizza = MargaritaPizza()
                break
            elif pizza_sec == 3:
                pizza = TurkPizza()
                break
            else:
                pizza = SadePizza()
                break

        pizza_base=pizza.get_cost()
        sos_cost=0
        sos_description=""
        for element in sos_list:
                if element == 11:
                    sos_cost += Zeytin(pizza).cost
                    sos_description+=" "+Zeytin(pizza).description
                elif element == 12:
                    sos_cost += Mantar(pizza).cost
                    sos_description+=" "+Mantar(pizza).description
                    
                elif element == 13:
                    sos_cost += KeciPeyniri(pizza).cost
                    sos_description+=" "+KeciPeyniri(pizza).description

                elif element == 14:
                    sos_cost += Et(pizza).cost
                    sos_description+=" "+Et(pizza).description

                elif element == 15:
                    sos_cost += Sogan(pizza).cost
                    sos_description+=" "+Sogan(pizza).description

                else:
                    sos_description+=" "+Misir(pizza).description
                    sos_cost +=Misir(pizza).cost

        total_cost = pizza_base+sos_cost
        description = pizza.get_description()+sos_description
        
        print('\nSiparisiz Ozetiniz: \nPizza seçiminiz: {}\nSos seçiminiz: {}\nTutar: {} TL '.format(pizza.get_description(), sos_description, total_cost))

        isim = input("Lütfen adınızı giriniz: ")
        # isim alanının harflerden oluşması onun dışında girilen karekterlerde hata vermesi için
        while not isim.isalpha():
            print('Gecersiz giris yaptiniz Lutfen sadece harfler kullanin.')  
            isim = (input('\nLutfen adınızı girin: '))  
        # girilen verilerin gerçekci olması için sayı basamaklarına sınırlama getirdik istenilen kadar girilmeli  
        tc_num = False
        kk_num = False
        kkps_num = False
        
        while not tc_num:  
            try:
                tc = input("Lütfen TC numaranızı giriniz: ")
                assert len(str(tc)) == 11
                tc_num = True
            except AssertionError:
                print("TC numaranızı 11 haneli olmak zorunda.")
            except ValueError:
                print("TC numaranız sadece rakamlardan oluşmak zorunda. Tekrar deneyiniz.")
        while not kk_num:  
            try:
                kk = int(input("16 haneli Kredi Kartı numaraınızı giriniz: "))
                assert len(str(kk)) == 16
                kk_num = True
            except AssertionError:
                print("Kart Numaranızı 16 haneli olarak tekrar giriniz.")
            except ValueError:
                print("Kart numaranız sadece rakamlardan oluşmalı. Tekrar Deneyiniz.")
        
        while not kkps_num:  
            try:
                kart_psw = input("Kredi kartı şifrenizi giriniz: ")
                assert len(str(kart_psw)) == 4
                kkps_num = True
            except AssertionError:
                print("Kart numaranız 4 haneli olmak zorunda.")
            except ValueError:
                print("Kart numaranız sadece rakamlardan oluşmak zorunda. Tekrar deneyiniz.")
        print("\nÖdemeniz Başarılı!")
        #ödeme tarihinin kaydedilmesi
        odeme_tarih = datetime.datetime.now()
        
        write_to_csv(isim, tc, str(kk), total_cost, odeme_tarih, str(kart_psw))

    #sparişin tekrarlanıp tekrarlanmaması için sorulması
        yeni_sparis = input("Yeni spariş oluşturmak istiyor musunuz? Evet/Hayır?: ")
        if yeni_sparis.lower() == "evet":
            continue
        elif yeni_sparis.lower() == "hayır":
                
            break

   # Yazdığımız csv_yaz fonksiyonunun çağrılarak verilen bilgilerin database'e işlenmesi
    now = datetime.datetime.now()
    formatted_time = now.strftime('%Y-%m-%d %H:%M') 
    print("Tebrikler siparisiniz basari ile olusturuldu.", formatted_time)

if __name__ == "__main__":
        main()
        print("İyi Günler Dileriz!") 

# sparişin hazır olması için kalan süre ve geri sayım
        finish_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        while True:
                    remaining_time = (finish_time - datetime.datetime.now()).total_seconds()
                    if remaining_time <= 0:
                        print("Siparişiniz hazır!")
                        break
                    print("Siparişinizin hazır olması için {} dakika kaldı.".format(int(remaining_time/60)))
                    time.sleep(60)
                    break
        print("Afiyet Olsun...")