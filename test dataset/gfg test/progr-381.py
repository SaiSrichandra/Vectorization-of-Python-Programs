with open(r"myfile.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Number of lines:', count + 1)