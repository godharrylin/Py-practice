x= 1.234
a=str(x).split('.',1)

if int(a[1][2]) >= 5:
    x= x+0.01
    b= str(x).split('.',1)
    b[1]=b[1][:2]
    c = '.'
    b=c.join(b)
else:
    b= str(x).split('.',1)
    b[1]=b[1][:2]
    c = '.'
    b=c.join(b)
    
print('b =',b)
print('\n')
print('=============')

def myRound(x,y):
    a=str(x).split('.',1)

    if int(a[1][y]) >= 5:
        x= x+ 1/ (10)**y
        b= str(x).split('.',1)
        b[1]=b[1][:y]
        c = '.'
        b=c.join(b)
    else:
        b= str(x).split('.',1)
        b[1]=b[1][:y]
        c = '.'
        b=c.join(b)
    return float(b)

c = [600.0241732163647, 598.8315731526682, 595.0149397556576, 593.2956404829945, 593.0258007829849, 593.8859285668199, 597.2383148205278, 597.6073115551479, 596.621437673132, 593.0519343354626]

d= [myRound(i,2) for i in c]
print(d)
g = myRound(3.15,1)
print('g = {}'.format(g))

h=round(3.15,1)
print('h = {}'.format(h))


