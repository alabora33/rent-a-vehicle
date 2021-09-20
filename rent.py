import datetime # pc zamanından şu anki zamanı çekmemize yarar

class VehicleRent:
    "parent class"
    
    def __init__(self, stock):
        
        self.stock = stock
        self.now = 0
    def displayStock(self):
        "display stock"
        print("{} vehicle available to rent".format(self.stock))
        return self.stock
    
    def rentHourly(self, n):
        "rent hourly"
        #araç sayısı = n
        if n<=0:
            print("Number should be positive(yanlış bir sayı girdiniz)")
            return None
        elif n>self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n, self.now.hour))
            
            self.stock -= n         
            return self.now
        
    def rentDaily(self, n):
        "rent daily"
        #araç sayısı = n
        if n<=0:
            print("Number should be positive(yanlış bir sayı girdiniz)")
            return None
        elif n>self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours".format(n, self.now.hour))
            
            
            self.stock -= n       
            return self.now
        
        
    def returnVehicle(self, request, brand):
        "return a bill"
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bicy_h_price = 10
        bicy_d_price = bicy_h_price*7/10*24 #araçların saatlik ve günlük fiyatlandırması belirlendi
        
        rentalTime, rentalBasis, numOfVehicle = request #süre, saatlik mi günlük mü, kiralanan araç sayısı
        bill = 0 #ilk fatura 
        if brand == "car": #kiralanan araç araba ise
            if rentalTime and rentalBasis and numOfVehicle: #kiralama zamanı, günlük mü saatlik mi olduğu ve kaç araç olduğu belirli ise
            
                self.stock += numOfVehicle #stocktaki araç sayısı arttırılır
                now = datetime.datetime.now() #şu anki zaman alınır
                rentalPeriod = now- rentalTime #şu anki zamandan kiralanma zamanı çıkarılarak ne kadar saat kiraladığı bulunur
                
                if rentalBasis == 1: #hourly 
                     bill = rentalPeriod.second/3600 * car_h_price * numOfVehicle
                elif rentalBasis == 2: #daily
                     bill = rentalPeriod.second/(3600*24) * car_d_price * numOfVehicle
                     
                if (2 <= numOfVehicle):
                    print("you have extra %20 discount")
                    bill = bill * 0.8
                
                print("Thank you for returning your car")
                print("Price : $ {}".format(bill))
                return bill

        elif brand == "bike": #kiralanan araç bisiklet ise
            if rentalTime and rentalBasis and numOfVehicle: #kiralama zamanı, günlük mü saatlik mi olduğu ve kaç araç olduğu belirli ise
            
                self.stock += numOfVehicle #stocktaki araç sayısı arttırılır
                now = datetime.datetime.now() #şu anki zaman alınır
                rentalPeriod = now- rentalTime #şu anki zamandan kiralanma zamanı çıkarılarak ne kadar saat kiraladığı bulunur
                
                if rentalBasis == 1: #hourly 
                     bill = rentalPeriod.second/3600 * bicy_h_price * numOfVehicle
                elif rentalBasis == 2: #daily
                     bill = rentalPeriod.second/(3600*24) * bicy_d_price * numOfVehicle
                     
                if (4 <= numOfVehicle):
                    print("you have extra %20 discount")
                    bill = bill * 0.8 #indirim uygulandı ve tekrar fatura hesaplandı
                
                print("Thank you for returning your bike")
                print("Price : $ {}".format(bill))
                return bill                         
                
        else:
            print("You don't rent a vehicle")
            return None
    
class carRent(VehicleRent):
    "child class"
    
    def __init__():
        pass
    def discount():
        pass
    
    
class bicyRent(VehicleRent):
    "child class"
    
    def __init__():
        pass


class Customer:
    
    def __init__():
        pass
    def requestVehicle():
        "request vehicle"
        pass
    def returnVehicle():
        "return vehicle"
        pass
    
    





















































