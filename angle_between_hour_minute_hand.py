hr = 3
minute = 30

if hr>=12 :
    hr = hr%12

m_d = minute*6

h_d = hr*30 + minute*0.5

diff = abs(m_d-h_d)
print(diff)