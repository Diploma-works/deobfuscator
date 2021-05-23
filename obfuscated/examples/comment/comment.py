# коммент
a = 2

easy = 2 + 2
if easy == 4:  # А вдруг нет?
    print('Квадрат    с обрезанными углами:')
    # коммент
    print('/-\\')
    print('|#|')  # c кучей 'коммент\'ариев'
    print('\\_/')
for i in range(1, 20):  # 'цик'л
    print(i)  # c кучей 'коммент\'ариев'
    print('  #  ')
    if True:
        print('  \',   \'  ')
print('\t')  # это, кстати, символ табуляции
print('\\')

class Car(object):
    """
    The Car class
    """
    def brake(self):
        """
        Stop the Car
        """
        return "The car class is breaking slowly!"
