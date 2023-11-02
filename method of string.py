#1. capitalize(): convert first letter of string into upper case

st = "hello pYtHon"
out = st.capitalize()
print(out)


#2. title():

st = "hello pythOn programing"
out = st.title()
print(out)


#3. lower()/casefold(): convert all letter into lowercase

st='hello 5G world'

out=st.lower()
print(out)

#4. upper():
st='hello world 123'
out= st.upper()
print(out)

#5 center() : return centered string with filled character
st='hello'
out=st.center(30,'*')
print(out)

#6 rjust()

st='hello'
out= st.rjust(20,'*')
print(out)

#7

n=10
for i in range(n+1):
    x=bin(i)[2:]
    print(x)
#8 how to access the element in string
#1. indexing: get the element at position

st='hello'
out= st[-6]
print(out)    


#9. slicing range(): get elements with range (substring)
# str[start : stop : step = 1]
st = "hello world"
out = st[1:10:2]
print(out)
