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
Dear {0} {1}
Thank you for your letter. We are sorry that our {2} {3} in your {4}. 
Please note that it should never be used in a {4}, especially near any {5}.

Send us your receipt and {6} for shipping and handling. We will send you
another {2} that, in our tests, is {9}% less likely to have {3}.

Thank you for your support.
Sincerely,
{7}
{8}
""".format(salutaion,name, product, verbed, room, animals, amount, spokesman, job_title, percent)

print(letter)