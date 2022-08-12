import imp


import matplotlib.pyplot as plt

# 构造数据
X_set = [1, 2, 3, 4, 5]  # X轴数值
Y_set = [128, 211, 136, 234, 150]  # Y轴数据
p1 = plt.bar(X_set, Y_set, width= 0.35, label='value')  # width表示柱子的宽度
plt.bar_label(p1, label_type='edge')   # label_type=‘edge’表示将数据值标签放在柱子顶端，label_type=‘center’表示将数据值标签放在柱子中间。
plt.title('The distribution of XXX')
plt.show()
