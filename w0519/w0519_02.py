import pandas as pd

data = {
   '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
   '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
   '키' : [197, 184, 168, 187, 188, 202, 188, 190],
   '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
   '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
   '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
   '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
   '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
   'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data)

print(df.describe())
print(df.info())
print(df['키'].mean())
print(df['키'].sum())
print(df.values)
print(df.index)
print(df.columns)

df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name = '지원번호'

print(df)

print(df.reset_index(drop=True))
print(df)

# temp = pd.Series([-20,-10,0,10,20],index=['1월','2월','3월','4월','5월'])
# print(temp['1월'])