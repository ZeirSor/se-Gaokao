def bubble_sort():
    # 获取用户输入
    n = int(input("请输入要排序的数字个数："))
    numbers = []
    for i in range(n):
        number = int(input("请输入第{}个数字：".format(i+1)))
        numbers.append(number)

    # 冒泡排序
    for i in range(n-1):
        for j in range(n-1-i):
            if numbers[j] > numbers[j+1]:
                
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # 输出排序结果
    print("排序结果：")
    for number in numbers:
        print(number, end=" ")
        
        
bubble_sort()
    