from django.shortcuts import render
from .models import Book, Author, Tag, Review, Profile
from django.db.models.functions import Length
from django.db.models import Count

def query_examples(request):
    # A - Busca por nome do autor
    nome_de_autores = Book.objects.filter(author__name='Pietro da Conceição')
    
    # B - Buscar livros por tag
    tag_de_livros = Book.objects.filter(tags__name='Tecnologia')
    
    # C - Buscar por termo em bio
    bio_de_perfil = Author.objects.filter(bio__icontains='Necessitatibus')
    
    # D - Buscar por livros com avaliações altas
    avaliacoes_altas = Review.objects.filter(rating__gte=4).order_by('-rating')
    
    # E - Buscar usuário por url específica 
    usuarios_por_website = Profile.objects.filter(website='https://cardoso.org/')
    
    # F - Buscar por livros sem avaliações
    livros_sem_avaliacoes = Review.objects.filter(rating__isnull=True)
    
    # G - Autores com maior número de livros
    maior_numero_livros = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')

    # H - Livros com resumos longos
    resumos_longos = Book.objects.filter(author__name='Pietro da Conceição')

    # I - Avaliações de um autor específico
    avaliacoes_de_autor = Review.objects.filter(book__author__name="Pietro da Conceição")
    
    # J - Livros com Múltiplas Tags:
    livros_multiplas_tags= Book.objects.filter(tags__in=[
        Tag.objects.get(name='Poesia'), 
        Tag.objects.get(name='Ciência')
        ]
    )

    # Envie todas as consultas para o template
    context = {
        'nome_de_autores': nome_de_autores,
        'tag_de_livros': tag_de_livros,
        'bio_de_perfil': bio_de_perfil,
        'avaliacoes_altas': avaliacoes_altas,
        'usuarios_por_website': usuarios_por_website,
        'livros_sem_avaliacoes': livros_sem_avaliacoes,
        'maior_numero_livros': maior_numero_livros,
        'resumos_longos': resumos_longos,
        'avaliacoes_de_autor': avaliacoes_de_autor,
        'livros_multiplas_tags': livros_multiplas_tags,
    }

    return render(request, 'core/teste1.html', context)
