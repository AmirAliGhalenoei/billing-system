from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import CreateinvoiceItemForm
from .models import Invoice, InvoiceItem



class CreateInvoiceView(View):
    template_name = "invoices/home.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        titles = request.POST.getlist("title")
        quantities = request.POST.getlist("quantity")
        prices = request.POST.getlist("price")
        discounts = request.POST.getlist("discount")

        rows = []
        for title, quantity, price, discount in zip(titles, quantities, prices, discounts):
            if not title.strip():
                continue

            form = CreateinvoiceItemForm({
                "title": title,
                "quantity": quantity,
                "price": price,
                "discount": discount,
            })
            if not form.is_valid():
                error = "اطلاعات یکی از ردیف‌ها درست نیست."
                return render(request, self.template_name, {"error": error})
            rows.append(form.cleaned_data)

        if not rows:
            error = "حداقل یک کالا وارد کنید."
            return render(request, self.template_name, {"error": error})

        invoice = Invoice.objects.create()
        for cd in rows:
            InvoiceItem.objects.create(
                invoice=invoice,
                title=cd["title"],
                quantity=cd["quantity"],
                price=cd["price"],
                discount=cd["discount"] or 0,
            )
        return JsonResponse({
            "ok": True,
            "invoice_id": invoice.id,
            "created": invoice.created.isoformat(),
        })