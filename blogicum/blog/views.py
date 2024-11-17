from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.published_objects.order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.published_objects,
        id=id,
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.published_objects.filter(
        category=category,
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template, context)
