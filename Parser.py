# import time
# import datetime
# now = datetime.datetime.now()
#
# time1 = now + datetime.timedelta(hours = 2, minutes = 32)
# print (now.strftime('%d.%m.%Y,%H.%M'))
# print (time1)
#
# time2 = now + datetime.timedelta(days = 5)
# print (time2)
# new_year = datetime.datetime(2021,1,1)
#
# print(new_year - now)
# a = int('056')
# print(a)

with open(r'C:\1.txt.log', 'r') as work_file:
    words_list = work_file.read().splitlines()
    words_counter = {}
    for i in words_list:
        if i not in words_counter.keys():
            words_counter.update()
        else:
            words_counter.values( +1 )
print (len(words_list))
print (words_counter)
with open(r'c:\2.txt', 'w') as out_file:
    for key,val in words_counter.items():
        out_file.write('{}:{}\n'.format(key,val))