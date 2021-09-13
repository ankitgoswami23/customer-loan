from rest_framework import serializers


class CustomerSerilaizer(serializers.Serializer):
    file = serializers.FileField()

    @staticmethod
    def validate_file(value):
        if value.name.split(".")[-1].lower() not in ["xlsx", "xls"]:
            raise serializers.ValidationError("only xlsx or xls file supported")
        return value

