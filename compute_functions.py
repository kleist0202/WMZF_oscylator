import numpy as np

def Amplitudy(l, m, R, k, t_max):
    t = np.linspace(0, t_max, t_max*4)
    #t = np.linspace(0, 48 * np.pi, 600)
    A0 = 1
    w0 = np.sqrt(k/m)
    b = (6*np.pi*R*l)/(2*m)
    w = np.sqrt(w0**2 - b**2)
    x = A0*np.e**(-3*np.pi*R*l*t/m)*np.cos(w*t)
    print(x)

    return t, x

def Energie(l, m, R, k, t_max):

    t = np.linspace(0, t_max, t_max*4)
    A0 = 1
    E = 0.5*k*A0**2*np.e**(-6*np.pi*R*l*t/m)

    return t, E
   
    
