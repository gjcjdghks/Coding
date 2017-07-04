m, d = map(int,raw_input().split())
t = 0
md=[31,28,31,30,31,30,31,31,30,31,30,31]
y=['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in range(m-1):
	t = t+md[i]
t = t + d
print y[t%7]
