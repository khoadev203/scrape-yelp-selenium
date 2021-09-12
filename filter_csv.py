def main():
    #check duplicate
    print(u'check duplicate from {0} and filter & write in {1}'.format('data.csv','filterd_data.csv'))
    with open('data.csv', 'r') as in_file, open('filterd_data.csv', 'w') as out_file:
        seen = set()  # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen:
                continue  # skip duplicate

            seen.add(line)
            out_file.write(line)

# main entry
if __name__ == '__main__':
    main()