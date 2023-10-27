from django.shortcuts import render,HttpResponse
def myworks(request):
    mw = [
        {'category': 'Absract Painting',
         'doc': '30-08-2023',
         'price': '1000 USD',
         'rating': '5',
         'inspiration': 'From Nature',
         },

        {'category': 'Digital',
         'doc': '15-07-2023',
         'price': '500 USD',
         'rating': '4',
         'inspiration': 'Technology',
         }

    ]
    return render(request, 'report/myworks.html', {'mw': mw})
def profile(request):
    return HttpResponse(request ,'report/profile.html')
def history(request):
    works = [
        {"noc": "mm", "pdate": "01-09-2023", "mop": "cash", "amount": "10000usd", "artcategory": "abstarct painting"},
        {"noc": "tarun", "pdate": "04-09-2023", "mop": "net banking", "amount": "1000usd", "artcategory": "digital"}
    ]
    return HttpResponse(request, 'report/history.html', {'works': works})

0# Create your views here.
