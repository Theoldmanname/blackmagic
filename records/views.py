from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from .forms import RecordForm


def record_list(request):
    records = Record.objects.all().order_by('-created_at')
    return render(request, 'records/record_list.html', {'records': records})


def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'records/record_detail.html', {'record': record})


def record_new(request):
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            return redirect('record_detail', pk=record.pk)
    else:
        form = RecordForm()
    return render(request, 'records/record_edit.html', {'form': form})


def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            record = form.save()
            return redirect('record_detail', pk=record.pk)
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/record_edit.html', {'form': form})


def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect('record_list')
    return render(request, 'records/record_delete_confirm.html', {'record': record})
