#Question 1
pi = 3.1415962
radius = 5
volume = (4/3) * pi * pow(radius,3)
print('The volume of a sphere with a radius of', radius, 'is', volume)

#Question 2
price = 24.95
shipping1 = 3
shipping2 = .75
n = 60
finalPrice = (price * n ) + shipping1 + (shipping2 * (n - 1))
print('The price of 60 books is', finalPrice, 'dollars')

#Question 3
start = 6 * 60 + 52
mile1 = 8 + (15/60)
mile3 = 3 * (7 + (12/60))
total_mile = 2*(mile1) + mile3
end = start + total_mile
print('She will be back at around', end/60)

#Question 4
average1 = 82
average2 = 89
avginc = ((average2 - average1)/average1)*100
print('The average increase is', '{:.2f}'.format(avginc), '%')

