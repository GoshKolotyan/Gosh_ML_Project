from django.shortcuts import render
from pickle import load
from json import loads

# Create your views here.
def main(request):
    model = load(open('/Users/gosh/PycharmProjects/pythonProject5/ML/logic/someobject.pickle', 'rb'))
    converter = load(open('/Users/gosh/PycharmProjects/pythonProject5/ML/logic/someobject1.pickle', 'rb'))
    print(request.GET.get('data'))
    output = ''
    if request.GET.get('data'):
        data = converter.transform(loads(request.GET.get('data')))
        output = model.predict(data)

    return render(request, 'index.html', {'output': output})