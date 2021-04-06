# 깃 

# 깃헙으로 협업하는 법

https://brunch.co.kr/@anonymdevoo/9

# 브랜치, 머지

pull request를 해야 하는 경우?

다른 브랜치로 머지하기 위해

# 부모 브랜치 찾기

git show-branch | grep '*' | grep -v "$(git rev-parse --abbrev-ref HEAD)" | head -n1 | sed 's/.*\[\(.*\)\].*/\1/' | sed 's/[\^~].*//'
