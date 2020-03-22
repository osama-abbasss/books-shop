from django.shortcuts import render, get_object_or_404
from .models import Section, Comment
from .form import CommentForm

def sections_view(request):
    sections = Section.objects.all()
    template_name = 'resume/resume.html'
    context = {"sections":sections}

    return render(request, template_name, context)


def section_details_view(request, slug):
    section = get_object_or_404(Section, slug=slug)
    comments = Comment.objects.filter(post=section)

    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            print("yes")
            comment= request.POST.get("comment")
            name= request.POST.get("name")
            email= request.POST.get("email")

            new_comment = Comment(
            post = section,
            comment =comment,
            name =name,
            email =email,
            )

            new_comment.save()
        else:
            print (error)

    template_name = 'resume/resume_details.html'
    context = {"section":section,
                'comments':comments}

    return render(request, template_name, context)
