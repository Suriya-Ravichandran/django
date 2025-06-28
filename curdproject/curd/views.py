from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookForm
from .models import Book 
# Create your views here.

def book_add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curd:booklist')
    return render(request,"add_book.html",{'form': form})

# READ (List)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('curd:booklist')
    return render(request, 'update_book.html', {'form': form})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('curd:booklist')
    return render(request, 'delete_book.html', {'book': book})