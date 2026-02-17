
email = input("Enter your Email: ")

index = email.index("@")

user_name = email[:index]
domain_name = email[index + 1:]

print(f"Your user name is \"{user_name}\" and domain name is \"{domain_name}\"")