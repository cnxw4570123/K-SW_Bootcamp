salutaion = "diligent"
name = 'Sherlock'
product = 'laptop'
verbed = 'didn\'t arrived'
room = '109'
animals = 'cat'
amount = '$100'
spokesman = 'edward'
job_title = 'manager'
percent = '48'

letter = """
Dear {0} {name}
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. 
Please note that iy should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""

print(letter)