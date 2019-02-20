def triangles(total):
    tri_list, count = [1], 0
    while count < total:
        # yield关键字将此函数变成了一个生成器（generate），程序每次运行到yield完就返回，
        # 等下次调用时再从yield处继续运行,一般使用for循环来重复调用
        yield tri_list
        # 杨辉三角每行列表首尾都为1，从第三行开始，中间的第i个数等于上一行的第（i-1)个加上第i个数
        tri_list = [1] + [tri_list[i] + tri_list[i+1]
                          for i in range(len(tri_list) - 1)] + [1]
        count += 1


total = int(input("请输入要显示杨辉三角的总行数:"))
for x in triangles(total):
    print(x)
