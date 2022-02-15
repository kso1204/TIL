import itertools
members = [['amy', 'frontend'], ['damian', 'frontend'], ['flynn', 'backend'], ['colin', 'backend'], ['belle', 'po']]


# 1.	멤버를 이름순으로 나열하세요 [a-z]

# 2.  po:1명, frontend:1~2명, backend:1~2명 으로 구성되어 있는 스쿼드(팀)을 만드려고 합니다. 가능한 경우의 수를 구하세요. 

# 3.  두 번째 문제에서 만들어진 팀 멤버의 팀목록을 No 와 같이 결과로 보여주세요.

me = []

for mem in members:
    me.append(mem[0])

print(sorted(me))


def makeTeam(members):
    
    list1 = []
    list2 = []
    for member in members:
        if member[1] == "frontend":
            list1.append(member[0])
        elif member[1] == "backend":
            list2.append(member[0])

    pep8
    

makeTeam(members)