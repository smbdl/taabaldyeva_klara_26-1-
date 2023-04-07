from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from products.forms import ProductCreateForm, ReviewCreateForm
from products.models import Product, Review
from products.constants import PAGINATION_LIMIT
from django.views.generic import ListView, CreateView, DetailView, DeleteView


# Create your views here.


class MainPageCPV(ListView):
    model = Product


class PostCPV(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, **kwargs):
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        """ starts_with, ends_with, icontains """

        """ and | or """

        if search:
            products = \
                products.filter(title__icontains=search) | products.filter(description__icontains=search)

        max_page = products.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        """ posts splice """
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }

        return render(request, self.template_name, context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': ReviewCreateForm,
            'user': request.user

        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=id
            )

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': ReviewCreateForm

        }

        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                image=form.cleaned_data.get('image'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


class ProductCreateCPV(ListView, CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            self.model.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                image=form.cleaned_data.get('image'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')

        return render(request, self.template_name,
                      context=self.get_context_data(form=form))
