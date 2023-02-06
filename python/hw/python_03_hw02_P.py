s_triangle = list(map(int, input().split()))
s_triangle.sort()

if s_triangle[0] == s_triangle[1] == s_triangle[2]:
    print('정삼각형')
elif s_triangle[0] ** 2 + s_triangle[1] ** 2 == s_triangle[2] ** 2:
    print('직각삼각형')
elif s_triangle[0] == s_triangle[1] or s_triangle[1] == s_triangle[2] or s_triangle[0] == s_triangle[2]:
    print('이등변삼각형')
elif s_triangle[0] + s_triangle[1] > s_triangle[2]:
    print('삼각형')
else:
    print('삼각형 아님')