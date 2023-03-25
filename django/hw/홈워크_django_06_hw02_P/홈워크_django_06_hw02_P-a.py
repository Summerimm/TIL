from django.views.decorators.http import require_POST

@require_POST
def delete(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    chatting.delete()
    return redirect("chattings:index")