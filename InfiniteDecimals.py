SoinsuList=[]
def SoinsuExtractor(n):
  for i in range(2, n):
    if n%i==0:
      SoinsuList.append(i)
      while True:
        k=2
        try:
          SoinsuList.remove(SoinsuList.index(k*i))
          k=k+1
        except ValueError:
          break

def NumRemover(n):
  for i in SoinsuList:
    while True:
      if n%i==0:
        n=n/i
      else:
        break
    print(str(i)+'의 거듭제곱 제거 후 결과: '+str(int(n)))


n=int(input('무한소수의 분모: '))
SoinsuExtractor(10)
NumRemover(n)
Token=1
while True:
  if n==1:
    print('0')
  elif (10**Token-1)%n==0:
    break
  else:
    Token=Token+1
    
print('순환마디의 길이는 '+str(Token)+'입니다.')
