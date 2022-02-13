"""Given mean temperatures on days, find out longest sequence of days with
min and max mean temperature difference within 5 degrees. Example:

Input:

temperatures = [7, 12, 5, 3, 11, 6, 10, 2, 9]
days = [0, 1, 2, 3, 4, 5, 6, 7, 8]

Output:

The sequence of days 4 to 6 has difference between maximum and minimum mean 
temperatures within 5 degrees with length of sequence 2, which is longest. 
"""

class Temperature:
    def __init__(self):
        """Longest sequence initial and final days set to zero"""
        self.long_seq_in_day = 0
        self.long_seq_fin_day = 0
        
    def solution(self, num_of_days, temp_by_day):
        max_len_seq = 0
        for i in range(num_of_days):
            len_seq = 0
            min_temp = temp_by_day[i]
            max_temp = temp_by_day[i]
            for j in range(i+1, num_of_days):
                if temp_by_day[j] > max_temp:
                    max_temp = temp_by_day[j]
                if temp_by_day[j] < min_temp:
                    min_temp = temp_by_day[j]
                if max_temp - min_temp <= 5:
                    len_seq = j - i
                    if len_seq > max_len_seq:
                        max_len_seq = len_seq
                        self.long_seq_in_day = i
                        self.long_seq_fin_day = j
                else:
                    break      
        return
        
    def longest_seq_in_day(self):
        return self.long_seq_in_day
        
    def longest_seq_fin_day(self):
        return self.long_seq_fin_day                 
        
if __name__ == '__main__':
    temp_on_day = list(map(int, input("Enter temperatures on days "\
        + "seperated by space (e.g. '7 12 5 3'): ").strip().split(" ")))
    num_of_days = len(temp_on_day)
    temp_by_day = dict(zip([i for i in range(num_of_days)], temp_on_day))
    obj = Temperature()
    obj.solution(num_of_days, temp_by_day)
    print(f"Longest sequence with min and max mean temperature difference"\
        + f" within 5 has initial day {obj.longest_seq_in_day()}, and"\
        + f" final day {obj.longest_seq_fin_day()}!")
