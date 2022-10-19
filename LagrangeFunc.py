import numpy as np
import matplotlib.pyplot as plt
xn = [-5, -3, -1, 1, 4, 7]
n = len(xn)
x0 = -5
yn = [-4, -1, 5, -4, 2, 0]
def Lag(x):
  s = 0
  for i in range(0, len(yn)):
    p1 = 1
    for j in range(0, len(xn)):
      if j==i:
        True
      else:
        p1 = p1*(x-xn[j])/(xn[i]-xn[j])
    s = s + yn[i]*p1
  return s
print('Значение полинома Лагранжа в x0=', x0, 'L(x0)=', Lag(x0))
xnew = np.linspace(np.min(xn), np.max(xn), 100)
ynew = [Lag(i) for i in xnew]
plt.plot(xn, yn,'o', xnew, ynew)
plt.grid(True)
plt.show()
