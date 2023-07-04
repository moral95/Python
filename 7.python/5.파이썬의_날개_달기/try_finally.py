try:
    f = open('foo.txt', 'w')
    
    # 무언가를 수행한다.
    (... 생략 ...)

finally:
    f.close()