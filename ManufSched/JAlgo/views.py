from django.shortcuts import render
from django.http import HttpResponse
import random
def algo_op(request):
    PT=[random.sample(range(1,100),2) for x in range(0,10)]

    #PT=[ [5,2],[2,6],[1,2],[7,5], [6,6],[3,7],[7,2],[5,1] ]

    n=len(PT)
    jobs=dict((key+1, PT[key]) for key in range(0,n))

    first=[]
    last=[]

    print("\n\t\tJohnson's Rule.")

    for j in range(1, n+1):
        print(j, jobs[j])


    for j in range(1,n+1):
        if jobs[j][0] < jobs[j][1]:
            first.append(j)
        else:
            last.append(j)
    first1=first
    last1=last
    print("\nJobs that will go first:",first1)
    print("Jobs that will go last:",last1)

    for k in range(0, len(first)):
        for j in range(0,len(first)-1):
            if jobs[first[j]][0] >= jobs[first[j+1]][0]:
                temp=first[j]
                first[j]=first[j+1]
                first[j+1]=temp

    print("\nJobs going first arranged in ascending order:",first)

    for k in range(0,len(last)):
        for j in range(0,len(last)-1):
            if jobs[last[j]][1] <=  jobs[last[j+1]][1]:
                temp=last[j]
                last[j]=last[j+1]
                last[j+1]=temp

    #last = list( reversed(last)  )
    print("Jobs going last arranged in descneding order:",last)

    print("\nFinal sequence:",first+last)
    #return HttpResponse(job1+job2)
    return render(request, 'JAlgo/basic.html', {'content': ['The jobs: ',PT,'Jobs that will go first: ',first1,'Jobs that will go last: ',last1,'Jobs going first arranged in ascending order: ',first,'Jobs going last arranged in descending order: ',last,'Final Sequence: ',(first+last)]})

def index (request):
    return render(request, 'JAlgo/home.html')
