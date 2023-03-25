def update(request,pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("articles:detail",reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    context = {
        'reservation':reservation,
        'form':form,
    }
    return render(request,"articles/update.html",context)