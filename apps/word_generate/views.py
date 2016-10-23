from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):

    request.session['mapping'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    request.session.setdefault('attempt', 0)
    return render(request, "word_generate/index.html")

def create_word(request):
    rs = request.session
    #rp = request.post

    if request.method == 'POST':
        word_length = 14
        random_word = ''
        i = 0
        while i < word_length:
            random_word += random.choice(rs['mapping'])
            i += 1
        rs['word'] = random_word
        rs['attempt'] += 1
        return redirect('/')

    else:
        return redirect('/')



    return redirect('/')
