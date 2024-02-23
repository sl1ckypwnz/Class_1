class cash_cassa:
    def __init__(self, money):
        self.money = money
        
    
    def top_up(self, x):
        self.money += x
        return f"В кассе - {x}"
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if x <= self.money:
            self.money -= x
        else:
            return ("Недостаточно денег в кассе")
        
s = cash_cassa (50000) # Касса с начальным балансом 
print(s.top_up(50000)) # Пополнение кассы
print(s.count_1000()) # Вывод количества целых тысяч в кассе 
print(s.take_away(150000)) # Попытка снять из кассы  

