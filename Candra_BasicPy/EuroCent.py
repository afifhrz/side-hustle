euro_cent = int(input())

euro_2 = 200
euro_1 = 100
euro_50c = 50
euro_20c = 20
euro_10c = 10
euro_5c = 5
euro_2c = 2
euro_1c = 1

# floor division
# 500 // 200 = 2

result_2 = euro_cent // euro_2

# euro_cent = 589
# euro_cent = 589 - (2 * 200)
# euro_cent = 189
euro_cent = euro_cent - (result_2 * euro_2)
# print(euro_cent)

# untuk mencari berapa keping 1 euro
result_1 = euro_cent // euro_1
euro_cent = euro_cent - (result_1 * euro_1)

# untuk mencari berapa keping 50 eurocent
result_50c = euro_cent // euro_50c
euro_cent = euro_cent - (result_50c * euro_50c)

# untuk mencari berapa keping 20 eurocent
result_20c = euro_cent // euro_20c
euro_cent = euro_cent - (result_20c * euro_20c)

# untuk mencari berapa keping 10 eurocent
result_10c = euro_cent // euro_10c
euro_cent = euro_cent - (result_10c * euro_10c)

# untuk mencari berapa keping 5 eurocent
result_5c = euro_cent // euro_5c
euro_cent = euro_cent - (result_5c * euro_5c)

# untuk mencari berapa keping 2 eurocent
result_2c = euro_cent // euro_2c
euro_cent = euro_cent - (result_2c * euro_2c)

# untuk mencari berapa keping 1 eurocent
result_1c = euro_cent // euro_1c
euro_cent = euro_cent - (result_1c * euro_1c)

print("2-euros:",result_2)
print("1-euros:",result_1)
print("50c-euros:",result_50c)
print("20c-euros:",result_20c)
print("10c-euros:",result_10c)
print("5c-euros:",result_5c)
print("2c-euros:",result_2c)
print("1c-euros:",result_1c)