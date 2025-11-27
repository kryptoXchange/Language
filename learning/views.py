from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lesson(request, id):
    context = {
        "lesson_id": id,
        "title": f"Lesson {id}",
        "content": "This is the lesson content for WorkLingo!"
    }
    return render(request, 'lesson.html', context)
