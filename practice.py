def demo1():
   """
   1,2,3,4可以组成几个不同的三位数
   :return:
   """
   count=0
   for i in range(1,5):
       for j in range(1,5):
          for k in range(1,5):
              if (i!=k) & (i!=j) & (j!=k):
                 print(i,j,k)
                 count=count+1
   print(count)
   return None
def demo2():
    """
    企业发放的奖金根据利润提成。
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，
    高于100万元时，超过100万元的部分按1%提成.
    从键盘输入当月利润I，求应发放奖金总数？
    :return:
    """
    while True:
       i=int(input('利润为:'))
       month_profit=[1000000,600000,400000,200000,100000,0]
       rate=[0.01,0.015,0.03,0.05,0.075,0.1]
       profit=0
       for index in range(0,6):
           if i >month_profit[index]:
              profit+=(i-month_profit[index])*rate[index]
              print((i-month_profit[index])*rate[index])
              i=month_profit[index]
       print(profit)
       choice=eval(input('请输入您的选择1 (yes) or 0 (no) :'))
       if choice==1:
           continue
       else:
           break
    return None
def demo2_2():
    i = int(input('利润为:'))
    month_profit = [1000000, 600000, 400000, 200000, 100000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    profit = 0
    for index in range(0, 6):
        if i > month_profit[index]:
            profit += (i - month_profit[index]) * rate[index]
            print((i - month_profit[index]) * rate[index])
            i = month_profit[index]
    print(profit)
    return None
def demo3():
    """
    一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    (m+n)(m-n)=168,m+n=i,m-n=j,i*j=168，m=(i+j)/2,n=(i-j)/2,j>=2,1<i<168/2+1
    :return:
    """
    for i in range(1,85):
        if 168%i==0:
            j=168/i
            if i>j and (i+j)%2==0 and (i-j)%2==0:
                m=(i+j)/2
                n=(i-j)/2
                x=n*n-100
                print(i)
                print(x)
    return None
def demo4():
    """
    输入某年某月某日，判断这一天是这一年的第几天？
    :return:
    """
    #首先判断年份
    year=eval(input('请输入要判断的年份:'))
    month=eval(input('请输入对应的月份:'))
    day=eval(input('请输入对应的日期:'))
    if year%400==0 and (year%4==0 and year%100!=0):
        print('这一年是闰年！')
        months=[0,31,60,91,121,152,182,213,244,274,305,335]
        if month in range(1,13):
            day_num=months[month-1]+day
            print('这一天是第',day_num,'天！')
        else:
            print('data error')
    else:
        print('这一年是平年！')
        months=[0,31,59,90,120,151,181,212,243,273,304,334]
        if month in range(1,13):
           day_num=months[month-1]+day
           print('这一天是第',day_num,'天！')
        else:
            print('data error')
    return None
def demo5():
 """
 #输入三个整数x,y,z，请把这三个数由小到大输出。
 :return:
 """
 while True:
    x=int(input('输入第一个整数:'))
    y=int(input('输入第二个整数:'))
    z=int(input('输入第三个整数:'))
    if x<y:
        if y<z:
            print(x,y,z)
        else:#y>z
            if x<z:
                print(x,z,y)
            if x>z:
                print(z,x,y)
    if x>y:
        if z>x:
            print(y,z,x)
        if z<x:
            if z<y:
                print(z,y,x)
            else:
                print(y,z,x)
    choice=eval(input('是否选择继续 1(yes) or 0(no) :'))
    if choice==1:
        continue
    if choice==0:
        break
 return None
def demo5_2():
  while True:
    # 输入三个整数x,y,z，请把这三个数由小到大输出。
    List=[]
    for i in range(3):
        x=eval(input('请输入整数:'))
        List.append(x)
    List.sort()
    print(List)
    choice=eval(input('请选择接下来的操作 1(yes) or 0(no) :'))
    if choice==1:
         continue
    else:
         break
  return None
def demo6():
    """
    斐波那契数列的某一项。
    :return:
    """
    #方法一
    def fib(n):
        a,b=1,1
        for i in range(1,n-1):
            a,b=b,a+b
        return a
    n=eval(input('请输入要输出的第几项:'))
    print(fib(n))
    return None
def demo6_2():
    #斐波那契数列的某一项
    #方法二:使用递归的方法解决
    def fib(n):
        if n==1:
            return 0
        if n==2 or n==3:
            return 1
        return fib(n-2)+fib(n-1)
    n=eval(input('请输入需要找的项数:'))
    print(fib(n))
    return None
def demo6_3():
    """
    输出斐波那契数列
    :return:
    """
    def fib(n):
        if n==1:
            return [0]
        if n==2:
            return [0,1]
        if n==3:
            return [0,1,1]
        fibs=[0,1,1]
        for i in range(1,n-2):
            fibs.append(fibs[-1]+fibs[-2])
        return fibs
    n=eval(input('请输入需要求的项数:'))
    print(fib(n))
    return None
def demo7():
    """
    将一个列表的数据复制到另一个列表中。
    :return:
    """
    a=[1,2,3,4]
    b=a[:]
    print(b)
    return None
def demo8():
    """
    输出 9*9 乘法口诀表。
    :return:
    """
    for i in range(1,10):
        print()
        for j in range(1,i+1):
            print('%d*%d=%d' % (i,j,i*j),end='\t')
    return None
def demo8_2():
    #方法二输出九九乘法表
    for i in range(1,10):
        print()#换行
        for j in range(1,i+1):
            print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    return None
def demo9():
    """
    暂停一段时间输出
    使用time模块的sleep()函数
    :return:
    """
    import time
    my_dict={1:'a',2:'b',3:'c'}
    for key,value in dict.items(my_dict):
        print(key,value)
        time.sleep(5)#暂停5秒
    l=[1,2,3,4]
    for i in range(len(l)):
        print(l[i])
        time.sleep(2)
    return None
def demo10():
    """
    暂停120秒输出，并格式化当前时间。
    :return:
    """
    import time
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(120)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return None
def demo11():
    """
    有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    :return:
    """
    #兔子的数量规律为1，1，2，3，5，8
    f1=1
    f2=1
    for i in range(1,13):
        print('%12ld %12ld' % (f1,f2),end='\t')#"%12ld %12ld" 输出两个12位的长整数
        if i%3==0:
            print('')
        f1=f1+f2
        f2=f1+f2
    return None
def demo12():
    """
    判断101-200之间有多少个素数，并输出所有素数。
    判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
    :return:
    """
    from math import sqrt
    counts=0
    flag=1
    for i in range(101,201):
        k=int(sqrt(i+1))
        for j in range(2,k+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i)
            counts+=1
        flag=1
    print('素数的个数为:',counts)
    return None
def demo12_2():
    #求解素数的标准答案
    h = 0
    leap = 1
    from math import sqrt
    for m in range(101, 201):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % m)
            h += 1
            if h % 10 == 0:
                print('')
        leap = 1
    print('The total is %d' % h)
def demo13():
    """
    打印出所有的"水仙花数".
    所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
    利用for循环控制100-999个数，每个数分解出个位，十位，百位。
    :return:
    """
    num=0
    for i in range(100,1000):
        a=i//100#求出百位数
        b=i//10%10#求出十位数字
        c=i%10#求出各位数字
        if i==a**3+b**3+c**3:
            print(i)
            num+=1
    print('水仙花树的数量为:',num)
    return None
def demo14():
    """
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
    (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
    (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
    (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
    :return:
    """
def demo15():
    """
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
    :return:
    """
    while True:
        student_score=eval(input('请输入学生的分数:'))
        if student_score>100 or student_score<0:
            print('成绩输入错误！')
            break
        elif student_score>=90:
            grade_class='A'
        elif student_score>=60 and student_score<=89:
            grade_class='B'
        elif student_score<60:
            grade_class='C'
        print('%d 分属于 %s 等级' % (student_score,grade_class))
        choice=eval(input('是否选择继续 1(yes) or 0(no) :'))
        if choice==1:
            continue
        else:
            break
    return None
def demo16():
    """
    输出指定格式的日期。
    使用 datetime 模块。
    :return:
    """
    import time
    import datetime
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d'))
    # 创建日期对象
    my_birthday=datetime.date(2000,6,10)
    print(my_birthday.strftime('%Y-%m-%d'))
    # 日期算术运算
    my_sister_birthday=my_birthday-datetime.timedelta(days=9)
    print(my_sister_birthday.strftime('%Y-%m-%d'))
    # 日期替换
    my_father_birthday=my_birthday.replace(year=my_birthday.year-30,month=my_birthday.month-4,day=my_birthday.day)
    print(my_father_birthday.strftime('%Y-%m-%d'))
    return None
def demo17():
    """
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    :return:
    """
    import string
    s=input('请输入一个字符串:\n')
    """
    input() 和 raw_input() 这两个函数均能接收 字符串 
    但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
    而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
    """
    letters = 0
    space=0
    digit=0
    others=0
    for c in s:
        if c.isalpha():
            letters+=1
        elif c.isspace():#用elif，否则others的数量太多
            space+=1
        elif c.isdigit():
            digit+=1
        else:
            others+=1
    print('char= %d ,space= %d ,digit= %d ,others= %d '%(letters,space,digit,others))
    return None
def demo18():
    """
    求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
    例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
    :return:
    """
    Tn=0
    Sn=0
    n=int(input('数列的项数为n=:'))
    a=int(input('输入首项为a=:'))
    for count in range(n):
        Tn=Tn+a
        a=a*10
        Sn+=Tn
        print(Tn)
    print('数列的和为:',Sn)
    return None
def demo19():
    """
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。
    例如6=1＋2＋3.编程找出1000以内的所有完数。
    :return:
    """
    return None
def demo20():
    """
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
    :return:
    """
    total_height=[]
    height=[]
    hei=100#初始高度
    times=10#次数
    for i in range(1,11):
        #从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i==1:
            total_height.append(hei)
        else:
            total_height.append(2*hei)
        hei/=2
        height.append(hei)
    print('总高度为:',sum(total_height))
    print('第10次的高度为:',height[-1])
    return None
def demo21():
    """
    猴子吃桃问题：
    猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
    第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
    以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
    :return:
    """
    y=1
    for day in range(9,0,-1):  #表示从9开始，取到0，不包含0；其中step默认是1，-1表示逆序
        x=(y+1)*2  #采取逆向思维的方法，从后往前推断。
        y=x
    print(x)
    return None
def demo22():
    """
    题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
    有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
    :return:
    """
    for a in ['x','y','z']:
        for b in ['x','y','z']:
            for c in ['x','y','z']:
                if (a!=b) and (a!=c) and (b!=c) and (a!='x') and (c!='x') and (c!='z'):
                    print('a和%s比赛,b和%s比赛,c和%s比赛'%(a,b,c))
    return None
def demo23():
    """
    打印出如下图案（菱形）:
        *
       ***
      *****
     *******
      *****
       ***
        *
    :return:
    """
    row=eval(input('请输入菱形的行数:'))
    #上半部分
    top_row=(row+1)//2
    for i in range(1,top_row+1):
        for j in range(1,top_row+1-i):
            print(' ',end='')
    #1,3,5,7的三角形,range(1,2),range(1,4),range(1,6)
        for k in range(1,2*i): #(1,1).(2,3),(3,5)
            print('*',end='')
        print()
    #下半部分
    bottom_row=row//2
    for i in range(1,bottom_row+1):
        for j in range(1,i+1):
            print(' ',end='')
        for k in range(1,2*(bottom_row-(i-1))):
            print('*',end='')
        print()
    return None
def demo24():
    """
    有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
    :return:
    """
    a=2
    b=1
    sum=0
    for i in range(1,21):
        sum+=a/b
        a,b=a+b,a
    print(sum)
    return None
def demo24_2():
    #使用列表的形式解决问题:
    a=2
    b=1
    l=[]
    for i in range(1,21):
        l.append(a/b)
        a,b=a+b,a
    print(sum(l))
    return None
def demo24_3():
    #参考答案
    a = 2
    b = 1
    lst = []
    for i in range(20):
        lst.append(str(a) + '/' + str(b))
        a, b = a + b, a
    print('{0} = {1}'.format(eval('+'.join(lst)), '+'.join(lst))) #设置对应的参数问题
    return None
def demo25():
    """
    求1+2!+3!+...+20!的和。
    :return:
    """
    s=1
    l=[]
    for i in range(1,21):
        s=s*i
        l.append(s)
    print('1!+2!+3!+...+20!=%d '%(sum(l)))
    return None
def demo26():
    """
    利用递归方法求5!
    程序分析：递归公式：fn=fn_1*4!
    :return:
    """
    def f(n):
        fn=0
        if n==0:
            return 1
        else:
            fn= n*f(n-1)
        return fn
    print('5!=%d'%(f(5)))
    return None
def demo27():
    """
    利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
    :return:
    """
    def f(s):
        if (len(s)>0):
            print(s[-1])
            f(s[0:-1])
    s=input('输入一段字符:')
    print(f(s))
    return None
def demo27_2():
    #参考答案
    def output(s, l):
        if l == 0:
            return
        print(s[l - 1])
        output(s, l - 1)
    s = input('Input a string:')
    l = len(s)
    output(s, l)
    return None
def demo28():
    """
    题目：有5个人坐在一起，问第五个人多少岁？
    他说比第4个人大2岁。
    问第4个人岁数，他说比第3个人大2岁。
    问第三个人，又说比第2人大两岁。
    问第2个人，说比第一个人大两岁。
    最后问第一个人，他说是10岁。请问第五个人多大？
    程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。
    :return:
    """
    def age(n):
        if n==1:
            a=10
        else:
            a=age(n-1)+2
        return a
    print('第五人的年龄为%d岁'%(age(5)))
    return None
def demo29():
    """
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
    :return:
    """
    while True:
        num=eval(input('请输入一个不多于五位的正整数:'))
        a=num//10000
        b=num%10000//1000
        c=num%1000//100
        d=num%100//10
        e=num%10
        if a!=0:
             print('五位数！倒序为%d %d %d %d %d'%(e,d,c,b,a))
        elif b!=0:
             print('四位数！倒序为%d %d %d %d'%(e,d,c,b))
        elif c!=0:
             print('三位数！倒序为%d %d %d'%(e,d,c))
        elif d!=0:
             print('两位数！倒序为%d %d'%(e,d))
        else:
             print('个位数！倒序为%d'%(e))
        choice=eval(input('情选择是否继续 1(yes) or 0(no) ？'))
        if choice==1:
            continue
        else:
            break
    return None
def demo30():
    """
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
    :return:
    """
    while True:
        num=eval(input('请输入一个5位数:'))
        #万位数字
        a=num//10000
        b=num%10000//1000
        c=num%1000//100
        d=num%100//10
        e=num%10
        if e==a and d==b:
            print('%d 是回文数！'%(num))
        else:
            print('%d 不是回文数！'%(num))
        choice=eval(input('请选择是否继续 1(yes) or else(no) :'))
        if choice==1:
            continue
        else:
            break
    return None
def demo31():
    """
    请输入星期几的第一个字母来判断一下是星期几?
    如果第一个字母一样，则继续判断第二个字母。
    星期一：Monday 星期二：Tuesday 星期三：Wednesday 星期四：Thursday 星期五：Friday 星期六：Saturday 星期天：Sunday
    :return:
    """
    word1=input('请输入第一个字母:')
    if word1=='M' or word1=='m':
        print('是周一！')
    if word1=='W' or word1=='w':
        print('是周三！')
    if word1=='F' or word1=='f':
        print('是周五！')
    if word1=='T' or word1=='t' or word1=='S' or word1=='s':
        print('无法确定！需要进一步检验！')
        word2=input('请输入第二个字母:')
        if word1=='T' or word1=='t':
            if word2=='u':
                print('是周二！')
            if word2=='h':
                print('是周四！')
            else:
                print('日期错误！')
        if word1=='S' or word1=='s':
            if word2=='a':
                print('是周六！')
            if word2=='u':
                print('是周日！')
            else:
                print('日期错误！')
    else:
        print('日期输入错误！')
    return None
def demo32():
    """
    按相反的顺序输出列表的值。
    :return:
    """
    a=[1,2,3,4,5]
    for i in a[::-1]:
        print(i)
    return None
def demo33():
    """
    按逗号分隔列表。
    :return:
    """
    a=[1,2,3,4,5]
    a1=','.join(str(n) for n in a)
    a2='*'.join(str(n) for n in a)
    print(a1)
    print(a2)
    return None
def demo33_2():
    a=[1,2,3,4,5]
    for i in range(0,5):
        if i!=(len(a)-1):
            print(a[i],end=',')
        else:
            print(a[i])
    return None
def demo34():
    """
    求100之内的素数。
    :return:
    """
    from math import sqrt
    counts=0
    flag=1
    for i in range(2,101):
        k=int(sqrt(i+1))
        for j in range(2,k+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i)
            counts+=1
        flag=1
    print('素数的个数为%d'%(counts))
    return None
if __name__=='__main__':
    demo34()
