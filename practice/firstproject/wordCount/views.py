from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def result(request):
    # textarea의 값 가져오기
    sentence = request.GET['sentence']

    wordList = sentence.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    
    # result.html로 보내주기 : dictionary 형태로 넘겨주기
    # .items 메서드 : dictionary의 key, value값이 한꺼번에 넘겨짐.
    return render(request, 'result.html', {'fulltext':sentence,'count':len(wordList), 'wordDict':wordDict.items})
