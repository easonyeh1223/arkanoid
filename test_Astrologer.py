class constellation:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def get_constellation(self) -> str:
        constellation = ['Capricron','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius']
        constellation_date = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
        # 執行順序
        # lambda 會把 x這個變數代入x<(self.month,self.day)這個判斷式
        # x從哪裡代呢? 透過filter
        # filter 會將 constellation_date 這個清單
        your_constellation = constellation[len(list(filter(lambda x:x<(self.month,self.day),constellation_date)))%12]
        return your_constellation
    def get_each_number(self,number: int) -> []:
        """
        輸入一個正整數，然後將每一位數分開。
        ex get_each_number(1920)
        return [1,9,2,0]
        """
        result = [int(i) for i in str(number)]
        return result

    def get_life_number(self) :
        """
        會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
        ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
        這樣生命靈數就是4
        """
        a = str(sum(self.get_each_number(self.year) + self.get_each_number(self.month) + self.get_each_number(self.day)))
        result = sum([int(i) for i in a])

        return result


a  =  constellation(1999,9,15)
print(a.get_each_number(1920))
print(a.get_life_number())

