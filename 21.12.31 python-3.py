#랜덤함수(난수함수)
#무작위로 수를 뽑는것
#이떄 라이브러리 사용!
#from random import *
#라이브러리는 아직 배우지 않았지만 내가 본 봐로는
#from ~ import * 라고 적는 것 같다. 
#또한 이 명령문은 ~를 어디선가(?)에서 수입, 즉 가져와~ 라는 명령문으로 보임
#randrange
#randint

from random import *

print(random()) 

#0.0부터 1.0까지의 임의의 값 생성

print( random() * 10) 

#10씩 곱해서 범위를 늘려줬음 난수함수에 *를 사용하면 범위가 늘어난다.

print(int(random()) * 10) 

#랜덤함수에 속한 ()에 수를 넣으면 안된다. 오류난다.
#물론 예외는 존재하지 않는다.

print(randint(1, 5)) 

#정수만를 무작위로 뽑고 싶으면 randint?
#그렇게 해도 정수만 나오고 random()에 int를 붙여도 나온다.
#print(int(random())) 이런 식으로 
#근데 이렇게 되면 0부터 출력이 되니까 시작 범위를 정하고 싶으면
# + 연산자를 사용해서 특정 수를 더해주면 된다

print( int( random() * 10 ) + 1 ) 

# 이렇게!
#주의 *를 사용해서 범위를 늘려주는 것을 잊으면 안됨.
#안그러면 + 1만 입력되서 계속 1이 나옴.

#ex
print( int ( random() ) + 1 ) # => 1

#randint()에서 ()사이에 있는 수를 모두 포함 즉, 1부터 5까지 중 난수 생성
# randrange함수도 정수 형태로 나온다 단 주의 할 것이 있다
# randrange( a , b )중 b전까지의 정수만 나온다.

print(randrange(1, 3)) 

# ( a , b )중 b전까지의 정수만 나온다.
#25행처럼 하기 싫으면 18행처럼하면 된다. why? 범위가 a부터 b까지 나오기 떄문이다.

#내가 만들어 보고 싶은 것 
# 1에서 100까지 수 중에 소숨점수 포함하는 것 하나 않하는 것 하나
# 않하는 것은 다시 randrange, randint 두 가지를 사용해서 만들어봐.

# 1. 소수점를 포함하는 난수 함수

print( (random() * 100) )
# 0.~ ~ 100까지 생성

# 2. 소수점을 포함하지 않는 난수 함수 - range버전

print( randrange(1, 101) ) 
# 0부터 9까지 생성 

# 3. 소수점을 포함하지 않는 난수 함수 - rangeint편

print( randint(1, 100) ) #0~10까지 난수 생성
