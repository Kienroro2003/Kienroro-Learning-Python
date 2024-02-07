text = '''Not exactly. Cohesion focuses on
how you’ve constructed each individual
class, object, and package of your software.
If each class does just a few things that are
all grouped together, then it’s probably a
highly cohesive piece of software. But if you
have one class doing all sorts of things that
aren’t that closely related, you’ve probably
got low cohesion.'''

print(' '.join(text.split('\n')))