import sys

while True:
    expr = input('请输入计算表达式（如 3 + 4）或 "q" 退出：')
    if expr.lower() == 'q':
        print('计算器退出')
        sys.exit()
    try:
        num1, op, num2 = expr.split()
        num1 = float(num1)
        num2 = float(num2)
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print('错误：除数不能为零')
                continue
            result = num1 / num2
        else:
            print('错误：无效的运算符')
            continue
        print(f'结果：{result}')
    except ValueError:
        print('错误：请输入有效的数字和运算符')
    except ZeroDivisionError:
        print('错误：除数不能为零')
