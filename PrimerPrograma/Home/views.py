from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')

def productos(request):

    productos = [{'name': 'Capuccino', 'img': 'capuccino.jpg', 'valor': 3000 ,'descripcion': 'El capuccino es cafe compuesto por expreso de café y leche con espuma de leche'},
                {'name': 'Café Americano', 'img': 'cafe.webp', 'valor': 2500, 'descripcion': 'El Café americano consta de cafe más agua'},
                {'name': 'Latte', 'img': 'latte.jpg', 'valor': 2000, 'descripcion': 'El late es un hermano del capuccino pero mas vistoso, por su corte entre el cafe y la leche'},
                {'name': 'Moca', 'img': 'moca.jpg', 'valor': 3500, 'descripcion': 'El café moca es un capuccino con chocolate'},
                {'name': 'Expreso', 'img': 'expreso.webp', 'valor': 1500, 'descripcion': 'El Expreso es un corto de café concentrado'},
             ]

    return render(request, 'productos.html', {
        'productos': productos
    })