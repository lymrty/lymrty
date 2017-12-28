import numpy as np
import matplotlib.pyplot as plt

def main():
    #这里我们取值一共1000个点，分为十份
    num_all = 1000 # 一共的点数
    num_copies = 10 # 一共分为10份
    num_points = num_all / num_copies # 每份的点数

    num_rows_copies = [3, 2, 3, 2]

    # 一共进行四次循环分别得到10个数组，这样可以将对应的结果得到
    x = []
    y = []
    # 四行数据，表示每次需要添加的范围，为在行上添加的变换
    row_copies = [1,2,3,4]
    # 三份数据是添加的元素, 表示次需要添加的范围， 为在列上添加的变换
    col_copies_2 = [2, 4]
    col_copies_3 = [1, 3, 5]
    row_num = 0 # 用来表示所在的行号
    col_num = 0
    for i in num_rows_copies:
        for ele_j in range(i):
            # np.random生成的值在[0.0, 1.0]之间
            if i==2:
                y_temp = np.random.random(int(num_points)) + row_copies[row_num]
                y.append(y_temp)
                x_temp = np.random.random(int(num_points)) + col_copies_2[ele_j]
                x.append(x_temp)
            else:
                y_temp = np.random.random(int(num_points)) + row_copies[row_num]
                y.append(y_temp)
                x_temp = np.random.random(int(num_points)) + col_copies_3[ele_j]
                x.append(x_temp)
        row_num += 1

    print(len(x), len(y))
    return x, y

# 该函数要画出x和y的图
def figure(x, y):
    len_x = len(x)
    len_y = len(y)
    print(len_x, len_y)
    plt.figure()
    for i in range(len_x):
        plt.scatter(x[i], y[i], c="k")

    # 给figure加入坐标
    # plt.xlabel("x")
    # plt.ylabel("y")
    # 关闭坐标轴
    plt.axis('off')
    plt.title("balabala")
    plt.show()


if __name__ == '__main__':
    x, y = main()
    figure(x, y)