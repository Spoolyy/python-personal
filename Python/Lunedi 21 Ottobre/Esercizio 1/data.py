class Analyzer:
    
    def total(self, list):
        total_sales = 0
        for number in list:
            total_sales += number
        print('The total_sales of the sales is: $', total_sales)
        return total_sales

    def average(self, list):
        total_sales = self.total(list)
        average = total_sales / len(list)
        print('The average of your sales is: $', average)
        return average
        
    def maximum(self, list):
        average = self.average(list)
        
        highestnumber = 0
        most_profitable_day = 0
        
        for day, number in enumerate(list):
            if number > average:
                highestnumber = number
                most_profitable_day = day
                print(f'Day: {day}. During this day, your income (${highestnumber}) was higher than your average income.')

        if highestnumber > 0:
            print(f'You profited the most on day {most_profitable_day}, with an income of ${highestnumber}')
        else:
            print('No day had a profit higher than the average.')
            