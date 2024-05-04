from django.shortcuts import render
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        
        # 파일 처리 로직 추가
        # 예를 들어, 파일을 저장하거나 다른 조작 수행
        
        return HttpResponse('파일이 성공적으로 업로드되었습니다.')
    return render(request, 'upload_form.html')
