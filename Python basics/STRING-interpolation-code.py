name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)


name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')
print(greeting)

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"
print(greeting)
