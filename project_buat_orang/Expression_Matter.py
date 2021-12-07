#2. Program Expression Matter

def expression_matter(a,b,c):
    maxx = []
    maxx.append(a*(b+c))
    maxx.append(a*b*c)
    maxx.append(a+b*c)
    maxx.append((a+b)*c)
    maxx.append(a+b+c)
    return max(maxx)

x = expression_matter(1,2,3)
y = expression_matter(1,1,1)
z = expression_matter(9,1,1)

print("Expression terbesar dari 1,2,3 adalah",x)
print("Expression terbesar dari 1,1,1 adalah",y)
print("Expression terbesar dari 9,1,1 adalah",z)

txt = open("express.txt","a")

txt.write(f"""
Bilangan expression terbesar dari 1,2,3 adalah {x}
Bilangan expression terbesar dari 1,1,1 adalah {y}
Bilangan expression terbesar dari 9,1,1 adalah {z}
""")
txt.close()
