from rest_framework.views import APIView
from django.views import View
from django.shortcuts import render

from loan_management import serializers as loan_serializer
from loan_management import utils as loan_utils
from loan_management import models as loan_models


# Create your views here.
class UploadView(APIView):

    @staticmethod
    def post(request):
        customer_serializer = loan_serializer.CustomerSerilaizer(data=request.data)

        if not customer_serializer.is_valid():
            return loan_utils.create_response(customer_serializer.errors, 400)

        loan_utils.parse_excel(customer_serializer.validated_data.get("file"))

        return loan_utils.create_response({"data_url": "http://localhost:8000/"}, 200)


class ShowCustomer(View):

    @staticmethod
    def get(request):
        customers = []
        customers_instances = loan_models.Customer.objects.filter().all()
        # if not customers_instances.exists()
        for customer in customers_instances:
            customer_data = customer.get_details()
            customer_data.update(**customer.branch.filter().last().get_details())
            customer_data.update(**customer.address.filter().last().get_details())
            customers.append(customer_data)

        return render(
            request=request,
            template_name="customer.html",
            context={"customers": customers}
        )
