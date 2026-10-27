from typing import List

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    """
    Calculates the maximum attainable profit for the fractional knapsack problem.
    """
    # Create a list of tuples containing (value/weight ratio, weight, value)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    
    # Sort items in descending order based on the value-to-weight ratio
    items.sort(key=lambda x: x[0], reverse=True)
    
    max_profit = 0.0
    current_capacity = capacity
    
    for ratio, weight, value in items:
        if current_capacity >= weight:
            # If the whole item fits, take it entirely
            max_profit += value
            current_capacity -= weight
        else:
            # If only a fraction fits, take the remaining capacity's worth
            max_profit += ratio * current_capacity
            break # Knapsack is full
            
    return max_profit


class Job:
    """Class to represent a job with an ID, deadline, and profit."""
    def __init__(self, job_id: int, deadline: int, profit: int):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs: List[Job]) -> List[int]:
    """
    Calculates the optimal job sequence to maximize profit where each job takes 1 unit of time.
    """
    # Sort jobs in descending order of profit to greedily pick the most profitable first
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Find the maximum deadline to create a time slot array
    max_deadline = max(job.deadline for job in jobs) if jobs else 0
    
    # Array to keep track of free time slots (False means free)
    # Size is max_deadline + 1 to use 1-based indexing for days
    time_slots = [False] * (max_deadline + 1)
    
    scheduled_sequence = []
    
    for job in jobs:
        # Try to schedule the job as late as possible before its deadline
        for j in range(job.deadline, 0, -1):
            if not time_slots[j]:
                # Found a free slot, schedule the job
                time_slots[j] = True
                scheduled_sequence.append(job.job_id)
                break
                
    return scheduled_sequence

# Example Usage:
if __name__ == "__main__":
    # Fractional Knapsack Example
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print(f"Max Profit (Knapsack): {fractional_knapsack(weights, values, capacity)}")

    # Job Scheduling Example
    job_list = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30)
    ]
    print(f"Optimal Job Sequence: {job_scheduling(job_list)}")