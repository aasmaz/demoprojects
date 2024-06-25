import datetime
from django.http import HttpResponse
from django.shortcuts import render
from.models import LogEntry

# Create your views here.

def mySquare(request,side):
    if side >0:
        area = side * side
        perimeter = 4 * side
        return HttpResponse(f"<h1>The area of the square is {area} and the perimeter is {perimeter}.</h1>")
    else:
        return HttpResponse("Invalid value")

    

def voteFromHome(request,age):
    if age >= 60:
        diff = age-60
        return HttpResponse(f"<h1>Eligible to vote from home. You are {diff} years old.</h1>")
    else:
        diff = 60-age
        return HttpResponse(f"<h1>Not eligible to vote from home. you need {diff} more years.</h1>")


# Show current date and time

def showCurrentDateTime(request):
    currdatetime = datetime.datetime.now()
    out = "<h2>Current date and time is %s</h2>"%(currdatetime)
    return HttpResponse(out)

def showDateSpecFormat(request):
    currdate = datetime.datetime.now().strftime("%d-%m-%Y")
    res = "<h2>Today's date is %s</h2>"%(currdate)
    return HttpResponse(res)

def showTimeNowAMPMor24HFormat(request):
    curr_time12 = datetime.datetime.now().strftime("%I:%m %p")
    curr_time24 = datetime.datetime.now().strftime("%H:%M")
    result = "<h2> Time now in 12 hr format is %s<br>Time now in 24 hr format is %s</h2>"%(curr_time12,curr_time24)
    return HttpResponse(result)

def showTimeAheadorBehind(request):
    curr_time24 = datetime.datetime.now()
    twohrsahead = curr_time24+datetime.timedelta(hours=2)
    tenminahead = curr_time24+datetime.timedelta(minutes=10)
    twohrsbehind = curr_time24+datetime.timedelta(hours=-2)
    result1 = "<h2>Time now in 24 hrs format %s<br>Time 2 Hrs ahead will be %s<br>Time 10 min ahead %s<br>Time 2 Hrs behind was%s</h2>"%(curr_time24,twohrsahead,tenminahead,twohrsbehind)
    return HttpResponse(result1)


def currentTime(request):
    curr_time24 = datetime.datetime.now()
    timeAhd = curr_time24+datetime.timedelta(hours=0.75)
    context = {'curr_time24': curr_time24,
               'timeAhd': timeAhd}
    return render(request,'timeAheadOutput.html', context)


def log_view(request):
    current_datetime = datetime.datetime.now()
    status_message = "Success!" if current_datetime.minute % 2 == 0 else "Failure!"
    log_entry = LogEntry(status_message=status_message)
    log_entry.save()
    return render(request, 'mytemplate.html', {'status_message': status_message})




