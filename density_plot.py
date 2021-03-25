import matplotlib.pyplot as plt
import sys
def main(argv):
    pos=[]
    neg=[]
    cov_name=sys.argv[1].split()[-1]
    neg_cov_name=sys.argv[2].split()[-1]
    with open(cov_name) as f:
        pos = f.readlines()
    with open(neg_cov_name) as f2:
        neg = f2.readlines()
    total_fq = int(sys.argv[3])
    path = sys.argv[4]
    if sys.argv[1] == 'max_circle.cov':
        exit()
    sign = 0
    if pos[0].split()[0][-1] == '-':
        sign = 'negative'
    pos_y = []
    neg_y = []
    neg_y_final = []
    pos_y_final = []
    name = sys.argv[1].split('.')[0]
    x_max_num = int(pos[-1].split()[-2])
    x_min_num = int(pos[0].split()[-2])

    for i in range(len(pos)):
        pos_unnorm_i = int(pos[i].split()[-1])
        pos_y.append(pos_unnorm_i / (total_fq / 4 / 1000000))

    for i in range(len(neg)):
        neg_unnorm_i = -int(neg[i].split()[-1])
        neg_y.append(neg_unnorm_i / (total_fq / 4 / 1000000))

        # reverse horizontally and vertically
    if sign == 'negative':
        for ele in reversed(pos_y):
            neg_y_final.append(-ele)
        for ele2 in reversed(neg_y):
            pos_y_final.append(-ele2)
    else:
        neg_y_final = neg_y
        pos_y_final = pos_y

    # change x axis
    if pos[0].split()[0][-1] == '+' or sign == 'negative':
        x_max_num = x_max_num - x_min_num + 1
        x_min_num = 1

    x_axis = [x for x in range(1, x_max_num + 1)]
    plt.figure(figsize=(8, 6))
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x_axis, pos_y_final,
                 color='red',
                 label='positve',
                 alpha=0.6,
                 linewidth=1)

    plt.plot(x_axis, neg_y_final,
                 color='blue',
                 label='negative',
                 alpha=0.6,
                 linewidth=1)
   
    plt.ylabel('coverage')
    plt.xlabel('base number')
    title = name + ': ' + str(x_min_num) + '-' + str(x_max_num)
    plt.title(title)
    plt.legend(['positive strand', "negative strand"])
    plt.savefig(path + '/' + name + '.png')


if __name__ == "__main__":
    main(sys.argv)









