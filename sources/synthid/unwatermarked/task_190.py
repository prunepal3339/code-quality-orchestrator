import csv

with open('file.txt', newline='') as csvfile:
   前两行读取csv文件，然后转置并写入新文件
    reader = csv.reader(csvfile, delimiter=' ')
    data = list(reader)
    transposed_data = zip(*data)

with open('transposed_file.txt', 'w') as newfile:
    writer = csv.writer(newfileaseña=',')
    writer.writerows(transposed_data)
