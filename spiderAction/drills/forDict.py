quotes = [
    {
        'text': 'a',
        'name': 'jane',
        'age': 20
     },
    {
        'text': 'b',
        'name': 'jack',
        'age': 21
     },
    {
        'text': 'c',
        'name': 'lucy',
        'age': 22
     },

]

for quote in quotes:
    text = quote['text']
    age = quote['age']
    name = quote['name']
    print(dict(text=text, name=name, age=age))
