from django.shortcuts import render
from django.urls import reverse_lazy
from catalog.models import Category, Product, Blog
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:list', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
