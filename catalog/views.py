from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from catalog.models import Category, Product, Blog, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product = Product.objects.all()

        for prod in product:
            active_version = Version.objects.filter(product=prod, version_sign=True).first()
            prod.active_version = active_version.version_name if active_version else 'Нет активной версии'
            prod.version_numbers = active_version.version_number if active_version else ''
            prod.version_signs = active_version.version_sign if active_version else False

        context_data['product'] = product
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('list_blog')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image')
    # success_url = reverse_lazy('list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_blog', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_number += 1
        self.object.save()

        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list_blog')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.public_sign:
        blog_item.public_sign = False
    else:
        blog_item.public_sign = True

    blog_item.save()
    return redirect(reverse('list_blog'))
