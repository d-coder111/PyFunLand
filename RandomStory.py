import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 2th Oct']
who = ['a tiger', 'an elephant', 'a ghost', 'a man','a cat']
name = ['Chris', 'Miriam','daniel', 'Harry', 'Starwalker']
residence = ['Russia','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'park']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))