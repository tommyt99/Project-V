from userinformation import UserInfo

# Usage
user1 = UserInfo(first_name="John", last_name="Doe", email="johndoe@example.com", age=28)

#Initialize V Rank
user1.v_rank = 1

# Update email 
user1.update_email("newemail@example.com")
print(user1)

