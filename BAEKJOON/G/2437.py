N = int(input())
l = list(map(int, input().split()))
l.sort()

result = 1

for i in l:
    if i > result:
        break
    result += i
print(result)

'''
https://www.acmicpc.net/board/view/143410
smallest_missing을 짧게 sm이라고 줄여서 부르겠습니다.

11번 줄의 for문이 끝날 때까지, 0부터 sm-1까지의 모든 무게를 잴 수 있음을 귀납법으로 증명합니다.

for문을 시작하기 전에는 추를 하나도 보지 않았으므로 sm = 1 초기화가 말이 됩니다.

i번째로 가벼운 추를 보고 있을 때, 이 추의 무게(wi)가 sm보다 크면 sm만큼의 무게를 만들 방법이 없는 게 확정되고
sm-1까지는 모두 가능하다고 가정했으니 sm이 정답입니다.

아니라면, (i-1)번째까지의 추들만을 사용해서 0부터 sm-1까지 만드는 법을 모두 알고 있으니
거기에 i번째 추만 추가하여 wi부터 wi+sm-1까지 만드는 방법도 알 수 있고, 이 두 범위가 겹치기 때문에 (wi <= sm) 빈틈이 생기지 않습니다.

따라서 결과적으로 sm이 wi만큼 증가하는 꼴이 되고, for문을 계속 진행합니다.

0              sm-1
+---------------+
            +---------------+
            wi           wi+sm-1
'''