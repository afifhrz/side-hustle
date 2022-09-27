euro_cent = int(input())

euro_data = [200,100,50,20,10,5,2,1]
euro_string = ["2","1","50c","20c","10c","5c","2c","1c"]

for index, data in enumerate(euro_data):
    result = euro_cent // data
    print(euro_string[index]+"-euros:",result)
    euro_cent = euro_cent - (result * data)