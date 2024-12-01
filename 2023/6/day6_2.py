time, distance = 45977295, 305106211101695
t1, t2 = (time/2 + ((time**2)/4 - distance)**0.5), (time/2 - ((time**2)/4 - distance)**0.5)
print(int(t1) - int(t2) - (int(t1) == t1)) #(int(t1) == t1) will subtract 1 if integer. Pretty cool. int() instead of floor since we have postives only. 
