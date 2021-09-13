from pandas import read_excel

from rest_framework.response import Response

from loan_management import models as loan_model


def create_response(data, code, message=None, extra=None):
    if not message:
        if code == 400:
            message = "Bad request"
        elif code == 200:
            message = "Success"

    return Response(
        data={"data": data, "message": message, "code": code, "extra": extra},
        status=code,
        content_type="application/json"
    )


def parse_excel(file):

    customers_data = read_excel(file)
    for index in range(len(customers_data["Customer Name"])):
        customer_instance = loan_model.Customer.objects.create(
            **{
                "name": customers_data["Customer Name"][index],
                "father_name": customers_data["Father Name"][index],
                "customer_profile": customers_data["Customer Profile"][index],
                "loan_account_no": customers_data["Loan Account No"][index]
            }
        )
        loan_model.Branch.objects.create(
            **{
                "customer": customer_instance,
                "zone": customers_data["Zone Name"][index],
                "region": customers_data["Region Name"][index],
                "area": customers_data["Area Name"][index],
                "branch_name": customers_data["Branch Name"][index],
                "branch_code": customers_data["Branch Code"][index]
            }
        )
        loan_model.CustomerAddress.objects.create(
            **{
                "customer": customer_instance,
                "pincode": customers_data["pincode"][index],
                "landmark": customers_data["landmark"][index],
                "address_1": customers_data["address1"][index],
                "address_2": customers_data["address2"][index],
                "address_3": customers_data["address3"][index]
            }
        )
