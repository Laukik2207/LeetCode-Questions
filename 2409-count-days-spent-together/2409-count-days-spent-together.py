class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_days(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_per_month[:month]) + day
            
        arrive_a = to_days(arriveAlice)
        leave_a = to_days(leaveAlice)
        arrive_b = to_days(arriveBob)
        leave_b = to_days(leaveBob)
        
        start_overlap = max(arrive_a, arrive_b)
        end_overlap = min(leave_a, leave_b)
        
        return max(0, end_overlap - start_overlap + 1)