from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    customer_profile = models.CharField(max_length=100)
    loan_account_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_details(self):
        return {
            "name": self.name,
            "father_name": self.father_name,
            "customer_profile": self.customer_profile,
            "loan_account_no": self.loan_account_no,
        }


class Branch(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="branch", on_delete=models.CASCADE
    )
    zone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)

    def get_details(self):
        return {
            "zone": self.zone,
            "region": self.region,
            "area": self.area,
            "branch_name": self.branch_name,
            "branch_code": self.branch_code
        }


class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="address", on_delete=models.CASCADE
    )
    pincode = models.CharField(max_length=7)
    landmark = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)

    def get_details(self):
        return {
            "pincode": self.pincode,
            "landmark": self.landmark,
            "address_1": self.address_1,
            "address_2": self.address_2,
            "address_3": self.address_3
        }
