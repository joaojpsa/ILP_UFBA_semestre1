st = input()
st = st.upper()
st = st.replace(" ", "")
i = st[::-1]

if st == i:
    print("Palindromo")
else:
    print("!Palindromo")


