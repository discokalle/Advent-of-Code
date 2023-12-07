times = [45, 97, 72, 95]
distance = [305, 1062, 1110, 1695]
number_of_ways = []
for i, t_race in enumerate(times): #check math.txt
    t1 = (t_race/2 + ((t_race**2)/4 - distance[i])**0.5) #root 1
    t2 = (t_race/2 - ((t_race**2)/4 - distance[i])**0.5) #root 2
    number_of_ways.append(int(t1) - int(t2) - (int(t1) == t1)) #(int(t1) == t1) will subtract 1 if integer. Pretty cool. int() instead of floor since we have postives only. 
prod = 1
for n in number_of_ways:
    prod *= n
print(prod)
