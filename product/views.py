from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


# Create your views here.(place you generate to be seen on screen)
#Index/ Home Page
def index(request: HttpRequest): #trov mean parameter name'HttpRequest'
    return render(
        request=request,
        template_name = "product/index.html"
        )  #return content text in web

#About Page
def about(request: HttpRequest):
    return render(
        request=request,
        template_name="product/about.html",
    )
    
def create(request: HttpRequest):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="read")  # Redirect after successful form submission
    return render(
        request=request,
        template_name="product/create.html",
        context={"form": form},  # Fixed key name
    )


def read(request: HttpRequest):
    count = Product.objects.count()
    products = Product.objects.all()  #yk all object from database
    return render(
        request=request,
        template_name="product/read.html",
        context = {
            "count": count,
            "products": products  # yk vea mk nis dermbei oy brer tv read bn
        },
    )

# Update
def update(request: HttpRequest, product_id: str):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(to="read")
    return render(
        request=request,
        template_name="product/update.html",
        context={"forms": form},
    )
# Delete
def delete(request: HttpRequest, product_id: str):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect(to="read")
    return render(
        request=request,
        template_name="product/delete.html",
        context={"product": product},
    )
