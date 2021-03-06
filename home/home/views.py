from django.shortcuts import render,HttpResponse
from newsfetch.google import google_search
from newsfetch.google2 import google_search2
from newsfetch.google3 import google_search3
from newsfetch.google6 import google_search6
from newsfetch.news import newspaper
from home.home.models import Venue
from django.http import HttpResponse
from newsfetch.bing3 import Bing3
from newsfetch.bing import Bing
import csv
from templates import *
# from django.shortcuts import render
from newsfetch.forms import GeeksForm



def venue_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="venue_csv"'
    #create a csv writer
    writer=csv.writer(response)


    venues=Venue.objects.all()

    #Add column headings to the csv file
    writer.writerow(['links'])

    # lines=[]
    for venue in venues:
        writer.writerow([venue.link])
    return response


def home_view(request):
    data=request.POST.get('name')
    return render(request,'home.html',{'data':data})

def add(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    fname = request.GET.get("fname")
    date1 = request.GET.get("date1")
    date2 = request.GET.get("date2")

    if num1!=None and num2!=None:
        google=google_search(num1, num2,fname,date1,date2)
        non = 0
        for i in google.urls:
            non += 1
        result = "Your search on google by website finished successfully with {} links".format(non)
    else:
        pass
    return render(request,'result.html',{"result":result})


def tadd(request):
    tnum1 = request.GET.get("tnum1")
    tnum2 = request.GET.get("tnum2")
    tfname = request.GET.get("tfname")
    tdate1 = request.GET.get("tdate1")
    tdate2 = request.GET.get("tdate2")

    if tnum1!=None and tnum2!=None:
        googlet=google_search2(tnum1, tnum2,tfname,tdate1,tdate2)
        no=0
        for i in googlet.urls:
            no+=1
        tresult="Your search on google by topic finished successfully with {} links".format(no)
    else:
        pass
    return render(request,'result.html',{"tresult":tresult})

def hoew(request):
    context = {}
    context['form'] = GeeksForm()
    return render(request, "home.html", context)


def btadd(request):
    btnum1 = request.GET.get("btnum1")
    btnum2 = request.GET.get("btnum2")
    btfname = request.GET.get("btfname")
    btdate1 = request.GET.get("btdate1")
    btdate2 = request.GET.get("btdate2")

    if btnum1!=None and btnum2!=None:
        googletb=google_search6(btnum1, btnum2,btfname,btdate1,btdate2)
        # bingsearch3 = Bing3(btnum1, btnum2, btfname)
        # count=bingsearch3.crawl_all()
        # bresult = "Bing search completed successfully"
        noc=0
        for i in googletb.urls:
            noc+=1
        btresult="Your search on google by topic finished successfully with {} links".format(noc)
    else:
        pass
    return render(request,'result.html',{"btresult":btresult})





def bingadd(request):
    bnum1 = request.GET.get("bnum1")
    bnum2 = request.GET.get("bnum2")
    bfname = request.GET.get("bfname")
    # bdate1 = request.GET.get("bdate1")
    # bdate2 = request.GET.get("bdate2")
    bresult="None"

    if bnum1!=None and bnum2!=None:
        bingsearch=Bing(bnum1, bnum2,bfname)
        bingsearch.crawl_all()
        bresult="Bing search completed successfully"

    else:
        pass
    return render(request,'result.html',{"bresult":bresult})

def getcontent(request):
    fp1 = request.GET.get("fp1")
    fpc=str(fp1)
    filename2='{}content.csv'.format(fpc[:-4])
    # self.search_term = '"{}" site:{}'.format(self.keyword, self.newspaper_url)
    linecount=0
    contentim=""


    if fp1 != None :

        with open(fp1) as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            print("okundu")

            for row in reader:
                if linecount == 0:
                    with open(filename2, 'w', encoding='UTF8', newline='') as csvfile:
                        csvwriter2 = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        csvwriter2.writerow(["content"])

                else:
                    print("sdsss")
                    print(row)
                    nrow='\t'.join(row)
                    newscont=newspaper(nrow)
                    cc=newscont.article
                    # lines=[]

                    with open(filename2, 'a', encoding='UTF8', newline='') as csvfile:
                        csvwriter2 = csv.writer(csvfile, delimiter=' ')
                        # csvwriter2.writerow(["content"])
                        csvwriter2.writerow([cc])

                    # print("headddddddd")
                    # print(newspaper(row).article)
                    # news = newspaper(row)
                    # print(news.summary)
                    contentim = "i??erik ??ekildi"

                linecount += 1
    else:
        pass

    return render(request,'result.html',{"contentim": contentim})
