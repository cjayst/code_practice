# 使用遞迴實作九九乘法表
# Implement multiplication table using recurcive function 

def loop(i, j):
    print(f'{i}x{j}={i*j}', end='\t')
    if i == 9:
        return i

    return loop(i+1, j)

if __name__ == '__main__':
    for i in range(1, 10):
        loop(1, i)
        print('')