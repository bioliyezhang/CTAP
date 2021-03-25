import sys
def main(argv):
    with open(sys.argv[1]) as trans:
        lines1=trans.readlines()
    with open(sys.argv[2]) as trans2:
        lines2=trans2.readlines()
    with open(sys.argv[3])as gff:
        annotation=gff.readlines()
    path=sys.argv[4]
    f2 = open(path + '/' + 'max_circle_gene.bed', 'w')
    name='.cov'

    name2='.negcov'
    def split_file(name,lines):
        for each in annotation:
            number = annotation.index(each)
            start = int(each.split()[3])
            end = int(each.split()[4])
            name_list=[]
            name_list.append(each.split()[-1])
            name_list.append(str(start-1))
            name_list.append(str(end-1))
            name_list.append('myregion')
            name_list.append('0')
            name_list.append(each.split()[-4])
            f = open(path + '/' + each.split()[-1] + name, 'w')
            for x in lines[start - 1:end]:
                x_list = x.split()
                x_list[0] = each.split()[-1] + each.split()[-4]
                f.write('\t'.join(x_list) + '\n')
            f2.write('\t'.join(name_list) + '\n')
    split_file(name,lines1)
    split_file(name2,lines2)
if __name__ == "__main__":
    main(sys.argv)