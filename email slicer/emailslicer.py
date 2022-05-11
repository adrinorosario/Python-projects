user_email = input("Enter your email address here: ")
username = user_email[:user_email.index('@')]
domain = user_email[user_email.index('@')+1:user_email.index('.')]
new_st = user_email[user_email.index('@'):]
extension = new_st[new_st.index('.'):]

print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Extension: {extension}")
