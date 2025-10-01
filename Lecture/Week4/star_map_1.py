import pandas as pd 
import py5

df = pd.read_csv("", encodings = "latin-1")

dist = df['Distance'][1]
display_name = df['Display Name'][1]

col = df['HabHyg']

print(col)
print(dist)
print(display_name)

print(df.shape)

print(df.shape[0]) #row count
print(df.shape[1]) #column count

for i, row in df.iterrows():
    print(i)
    display_name = row['Display Name']
    print(display_name)

s = "I love Python"
l = s[2:6]
print(l) 

rainfall = [300, 400, 800, 400, 200, 100, 50, 25, 100, 200, 300, 400]

print(len(rainfall))

def setup():
    py5.size(500,500)

def draw():
    py5.background(0)

    w = py5.width

    for i in range(len(rainfall)):
        x = py5.remap(i, 0, len(rainfall), 0, py5.width)
    py5.rect(x, py5.height, w, - rainfall)

py5.run_sketch()


