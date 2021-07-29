def vowel_check():
    a = ['A', 'E', 'I', 'O', 'U', 'Y']
    n = input('Введите текст: ')
    count = 0
    for i in n:
        if i in a:
            count+=1
        return count
    print(count)


def pyramida():
    n = input('Введите символ пирамиды: ')
    m = int(input('Введите число этажей: '))

    print(m**2)
    for i in range(m):
        print(' '*(m-i-1) + f'{n}'*(2*i+1), '\n')


if __name__ == '__main__':
    vowel_check()
    pyramida()

