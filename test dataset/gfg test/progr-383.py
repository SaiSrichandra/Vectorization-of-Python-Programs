with open(r"myfile.txt", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)