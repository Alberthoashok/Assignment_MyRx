Question 1:

def sorted_squares(arr):
    n = len(arr)
    left, right = 0, n - 1
    result = [0] * n 
    pos = n - 1 

    while left <= right:
        left_val, right_val = abs(arr[left]), abs(arr[right])
        if left_val > right_val:
            result[pos] = left_val ** 2
            left += 1
        else:
            result[pos] = right_val ** 2
            right -= 1
        pos -= 1 

    return sorted(result)


input_arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output_arr = sorted_squares(input_arr)

print("Output:", output_arr)


Question 2:

from dataclasses import dataclass, field
from typing import List
from datetime import date

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    postal_code: str

@dataclass(frozen=True)
class ImmutableEmployee:
    name: str
    id: str
    date_of_joining: date
    addresses: List[Address] = field(default_factory=list)


if __name__ == "__main__":
    address1 = Address("123 Main St", "Springfield", "IL", "62704")
    address2 = Address("456 Oak St", "Shelbyville", "IL", "62565")

    employee = ImmutableEmployee(
        name="John Doe",
        id="E12345",
        date_of_joining=date(2022, 5, 15),
        addresses=[address1, address2]
    )

    # Print the employee details
    print(employee)

    try:
        employee.name = "Jane Doe"  
    except AttributeError as e:
        print(f"Error: {e}")


Question 3:

def sort_rgb_balls(balls):
   
    low, mid, high = 0, 0, len(balls) - 1

    while mid <= high:
        if balls[mid] == "B":
            # Swap balls[mid] with balls[low] and increment both pointers
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1
        elif balls[mid] == "G":
            mid += 1
        else:  
            balls[mid], balls[high] = balls[high], balls[mid]
            high -= 1

    return balls

input_balls = ["R", "G", "B", "G", "G", "R", "B"]
sorted_balls = sort_rgb_balls(input_balls)

print("Sorted:", sorted_balls)


Question 4:

def find_min_platforms(arrivals, departures):
    arr = sorted([int(a.split(':')[0]) * 60 + int(a.split(':')[1]) for a in arrivals])
    dep = sorted([int(d.split(':')[0]) * 60 + int(d.split(':')[1]) for d in departures])

    n = len(arr)
    platforms = 0
    max_platforms = 0

    i, j = 0, 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms


arrivals = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departures = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

result = find_min_platforms(arrivals, departures)
print("Minimum platforms required:", result)


Question 5:

def sort_hashmap_by_value(input_map):
    sorted_map = dict(sorted(input_map.items(), key=lambda item: item[1]))
    return sorted_map


# Example input
input_map = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}

sorted_map = sort_hashmap_by_value(input_map)

print("Sorted Map:", sorted_map)
