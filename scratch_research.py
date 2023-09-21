import numpy as np

M12 = '[[cos(2*phi) 0 0 0 0 0 -sqrt(2)*sin(2*phi)/2 sqrt(2)*sin(2*phi)/2 0 0],[0 cos(phi) 0 sin(phi) 0 0 0 0 0 0],[0 0 cos(phi) 0 sin(phi) 0 0 0 0 0],[0 -sin(phi) 0 cos(phi) 0 0 0 0 0 0],[0 0 -sin(phi) 0 cos(phi) 0 0 0 0 0],[0 0 0 0 0 1 0 0 0 0],[sqrt(2)*sin(2*phi)/2 0 0 0 0 0 cos(phi)**2 sin(phi)**2 0 0],[-sqrt(2)*sin(2*phi)/2 0 0 0 0 0 sin(phi)**2 cos(phi)**2 0 0],[0 0 0 0 0 0 0 0 1 0],[0 0 0 0 0 0 0 0 0 1]]'


def PythonToLatex(string):          # just for converting matrices to latex from numpy arrays
    ML = [j for j in string]
    for i in range(len(ML)):
        if ML[i] == '(':
            ML[i] = '{'
        if ML[i] == ')':
            ML[i] = '}'
        # phi, sin,cos
        if ML[i] == 'p' and ML[i+1] == 'h' and ML[i+2] == 'i':
            ML[i] = '\\p'
        if ML[i] == 's' and ML[i+1] == 'i' and ML[i+2] == 'n':
            ML[i] = '\\s'
        if ML[i] == 'c' and ML[i+1] == 'o' and ML[i+2] == 's':
            ML[i] = '\\c'
        if ML[i] == 's' and ML[i+1] == 'q' and ML[i+2] == 'r' and ML[i+3] == 't':
            ML[i] = '\\s'
    # comma replaced by next line, empty space by '&'
        if ML[i] == ',':
            ML[i] = '\\\\'
        if ML[i] == ' ':
            ML[i] = '&'
        if ML[i] == '*' and ML[i+1] == '*':
            ML[i] = '^' 
            ML[i+1] = ''
        if ML[i] == '[' or ML[i]==']' or ML[i] == '*':
            ML[i] = ''
    out = ' \\begin{equation} \\left( \\begin{array}{cccccccccc}'+''.join(ML)+'\\end{array} \\right) \\end{equation}'
    return out


print(PythonToLatex(M12))

'\begin{equation} \left( \begin{array}{cccc}\cos{2\Phi}&0&0&0&0&0&-\sqrt{2}\sin{2\Phi}/2&\sqrt{2}\sin{2\Phi}/2&0&0\\0&\cos{\Phi}&0&\sin{\Phi}&0&0&0&0&0&0\\0&0&\cos{\Phi}&0&\sin{\Phi}&0&0&0&0&0\\0&-\sin{\Phi}&0&\cos{\Phi}&0&0&0&0&0&0\\0&0&-\sin{\Phi}&0&\cos{\Phi}&0&0&0&0&0\\0&0&0&0&0&1&0&0&0&0\\\sqrt{2}\sin{2\Phi}/2&0&0&0&0&0&\cos{\Phi}2&\sin{\Phi}2&0&0\\-\sqrt{2}\sin{2\Phi}/2&0&0&0&0&0&\sin{\Phi}2&\cos{\Phi}2&0&0\\0&0&0&0&0&0&0&0&1&0\\0&0&0&0&0&0&0&0&0&1\end{array} \right) \end{equation}'


# print(np.arange(-4,15.1,.25))

for i in np.arange(-4,15.1,.25):
    print(f'\draw[thick] ({2*i},0) --({2*(i+.125)},.25);')

# \draw[->] (1,10) -- (2,11)












