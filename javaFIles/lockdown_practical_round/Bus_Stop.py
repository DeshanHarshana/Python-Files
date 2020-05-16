number_of_stop_points=int(input())

list_of_stop_point=list(map(int, input().split()))
if(len(list_of_stop_point)!=number_of_stop_points):
    exit()
list_of_spend_time_and_speed=list(map(int, input().split()))


print(number_of_stop_points)
print(list_of_stop_point)