from django.http import FileResponse
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Todo, Document
from .forms import TodoForm, DocumentForm
from django.contrib import messages
from django.conf import settings
import os


def index(request):
    task = Todo.objects.all()
    task_form = TodoForm()
    document_form = DocumentForm()

    if request.method == 'POST':
        if 'title' in request.POST:  # Check if task form is submitted
            task_form = TodoForm(request.POST)
            if task_form.is_valid():
                task_form.save()
                messages.success(request, "Task added successfully!")
                return redirect('todo')

        elif 'file' in request.FILES:  # Check if document form is submitted
            document_form = DocumentForm(request.POST, request.FILES)
            if document_form.is_valid():
                document_form.save()
                messages.success(request, "Document uploaded successfully!")
                return redirect('todo')

    return render(request, 'todo/index.html', {
        'list': task,
        'forms': task_form,
        'document_form': document_form
    })

def delete_task(request, item_id):
    task = Todo.objects.get(id=item_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('todo')

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'todo/document_list.html', {'documents': documents})

def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')  # Redirect to document list
    else:
        form = DocumentForm()

    return render(request, 'upload_document.html', {'document_form': form})

def delete_file(request, file_id):
    document = get_object_or_404(Document, id=file_id)

    # Delete the file from storage
    if document.file:  # Ensure there is a file
        file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))
        if os.path.exists(file_path):
            os.remove(file_path)  # Remove the file from storage

    # Delete the record from the database
    document.delete()
    
    return redirect("document_list")  # Redirect after deleting

def download_file(request, file_id):
    document = get_object_or_404(Document, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        return redirect("document_list")  # Redirect if file not found
