# import pandas
# # data = pandas.read_csv('100DaysOfCode_Python/Day_25/weather_data.csv')
# # print(data)

# # data_dict = data.to_dict()
# # print(data_dict)

# # Converting the data at temp to a list
# # temp_list = data['temp'].to_list()
# # print(temp_list)

# # # mean temperature
# # mean_ = data['temp'].mean()
# # print(mean_)

# # # Getting the maximum number in a list
# # maximum = data['temp'].max()
# # print(maximum)

# # # Getting dat in column
# # print(data.condition)
# # print(data['day'])

# # Getting the data in the row
# # print(data[data.day == 'Monday'])

# # highest_temperature = data['temp'].max()
# # print(data[data.temp == data['temp'].max()])

# # monday_temp = data[data.day == 'Monday'].temp[0]
# # c_to_f = monday_temp * 9/5 + 32
# # print(c_to_f)

# # creating a datframe from scratch
# data_dict = {
#     'students': ['Amy', 'Jack', 'Lily'],
#     'scores': [95, 85, 92]
#     }
# data = pandas.DataFrame(data_dict)
# data.to_csv('100DaysOfCode_Python/Day_25/Random_data_csv.csv')


import pandas

squirrel_data = pandas.read_csv('100DaysOfCode_Python/Day_25/2018_Squirrel_Data.csv')
Fur_list = squirrel_data['Primary Fur Color'].to_list()

gray_count = Fur_list.count('Gray')
black_count = Fur_list.count('Black')
Cinnamon_count = Fur_list.count('Cinnamon')

new_data = {
    'Fur Color': ['Gray' , 'Red', 'Black'],
    'Count': [gray_count, Cinnamon_count, black_count]
}
squirrel_fur_count = pandas.DataFrame(new_data)
squirrel_fur_count.to_csv('100DaysOfCode_Python/Day_25/squirrel_count.csv')
print(squirrel_fur_count)

# print(squirrel_data['Primary Fur Color'].value_counts().to_csv())
# print(squirrel_data['Primary Fur Color'].unique()[1:])

