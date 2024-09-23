from django.shortcuts import render, get_object_or_404
from .models import Blog, Category , Comment
from django.shortcuts import redirect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def index(request):
    post = Blog.objects.filter(status="1").order_by('-date')  # Filter published posts
    main_post = Blog.objects.filter(status="1", Main_post=True).order_by("-date")[:1]
    recent = Blog.objects.filter(section="Recent", status="1").order_by("-date")[:5]
    popular = Blog.objects.filter(section="Popular", status="1").order_by("-date")[:5]
    
    # Get trending posts for specific categories
    trending_technology = Blog.objects.filter(section="Trending", category__name="Technology", status="1").order_by("-date")[:3]
    trending_education = Blog.objects.filter(section="Trending", category__name="Education", status="1").order_by("-date")[:3]
    
    # Get Editor's Pick for Technology category (first post and other 4)
    editors_pick_technology = Blog.objects.filter(category__name="Technology", status="1").order_by("-date")[:5]
    first_tech_post = editors_pick_technology.first()
    other_tech_posts = editors_pick_technology[1:]
    
    # Get education posts
    education_posts = Blog.objects.filter(category__name="Education", status="1").order_by("-date")[:2]

    category = Category.objects.all()

    context = {
        "post": post,
        "main_post": main_post,
        "recent": recent,
        "category": category,
        "popular": popular,
        "trending_technology": trending_technology,
        "trending_education": trending_education,
        "first_tech_post": first_tech_post,
        "other_tech_posts": other_tech_posts,
        "education_posts": education_posts,
    }

    return render(request, "index.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(Blog, blog_slug=slug)
    categories = Category.objects.all()  
    comments = Comment.objects.filter(post=post).order_by('-date')  # Updated field name

    # Add popular posts to the context
    popular = Blog.objects.filter(section="Popular").order_by("-id")[:5]

    context = {
        "post": post,
        "categories": categories,
        "popular": popular,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)





def category(request, slug):
    categories = Category.objects.all()  # Fetch all categories
    blog_cat = Blog.objects.filter(category__slug=slug)  # Fetch blogs belonging to the category slug

    context = {
        "categories": categories,
        "active_category": slug,
        "blog_cat": blog_cat,
    }

    return render(request, "categories_page.html", context)




def add_comment(request, slug):
    if request.method == "POST":
        post = get_object_or_404(Blog, blog_slug=slug)
        comment_text = request.POST.get('InputComment')
        email = request.POST.get('InputEmail')
        website = request.POST.get('InputWeb')
        name = request.POST.get('InputName')
        parent_id = request.POST.get('parent_id')
        parent_comment = None  # Default to None

        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)

        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            website=website,
            comment_text=comment_text,  # Correct field name
            parent=parent_comment,
        )

        return redirect('blog_detail', slug=post.blog_slug)
    return redirect('blog_detail')



def categories_page(request):
    
    return render(request,'categories_page.html')






def search_view(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")  # Debug: Print the search query
    if query:
        posts = Blog.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query)
        )
        print(f"Posts found: {posts}")  # Debug: Print the filtered posts
    else:
        posts = Blog.objects.none()

    return render(request, 'search_results.html', {'posts': posts, 'query': query})


# Contact  view to send email to admmin


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        subject = request.POST.get('InputSubject')
        message = request.POST.get('InputMessage')

        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=email,
                recipient_list=['irfankhan.contact786@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return render(request, 'contact.html')  # Replace with your actual template