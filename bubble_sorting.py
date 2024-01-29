def bubble_sorting(numbers, flag=True):
    lst = numbers.split()
    lst_len = len(lst)
    while flag:
        flag = False
        for i in range(lst_len - 1):
            if int(lst[i]) > int(lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = True
        lst_len -= 1
    return ' '.join(lst)


if __name__ == '__main__':
    print(bubble_sorting('834 385 623 924 334 730 642 909 480 655 661 636 910 465 815 177 393 607 253 507 926 484 617 505 189 62 292 145 596 970 429 848 198 22 114 296 994 714 824 39 483 491 417 805 470 592 764 201 299 305 378 500 758 325 945 143 670 679 535 927'))
