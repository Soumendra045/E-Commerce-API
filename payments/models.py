# from django.db import models
# from django.conf import settings
# from django.utils.translation import gettext_lazy as _
# import uuid

# class PaymentMethod(models.TextChoices):
#     CARD = "CARD",_("Credit/Debit Card")
#     UPI = "UPI",_("Upi")
#     NETBANKING = "NETBANKING",_("Net Banking")
#     WALLET = "WALLET",_("Wallet")
#     COD = "COD",_("Cod")
    
# class PaymentStatus(models.TextChoices):
#     PENDING = "PENDING", _("Pending")
#     SUCCESS = "SUCCESS", _("Success")
#     FAILED = "FAILED", _("Failed")
#     REFUNDED = "REFUNDED", _("Refunded")

# class RefundStatus(models.TextChoices):
#     PENDING = "PENDING", _("Pending")
#     SUCCESS = "SUCCESS", _("Success")
#     FAILED = "FAILED", _("Failed")

# class Payment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='payments')
#     order = models.OneToOneField("orders.Order",on_delete=models.CASCADE,related_name='payment')
#     amount = models.DecimalField(max_digits=10,decimal_places=2)
#     method = models.CharField(max_length=20,choices=PaymentMethod.choices,default=PaymentMethod.CARD)
#     status = models.CharField(max_length=20,choices=PaymentStatus.choices,default=PaymentStatus.PENDING)
#     transaction_id = models.CharField(max_length=100,blank=True,null=True,help_text='ID From Payment gateway')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=True)

#     def __str__(self):
#         return f"Payment {self.id} - {self.order} - {self.status}"
    
# class Refund(models.Model):
#     payment = models.ForeignKey(
#         Payment, on_delete=models.CASCADE, related_name="refunds"
#     )
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     reason = models.TextField(blank=True, null=True)
#     refund_transaction_id = models.CharField(max_length=100, blank=True, null=True, help_text="ID from payment gateway")
#     status = models.CharField(max_length=20, choices=RefundStatus.choices, default=RefundStatus.PENDING)
#     refunded_at = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

#     def save(self, *args, **kwargs):
#         # Prevent over-refund
#         total_refunded = sum(
#             refund.amount for refund in self.payment.refunds.all()
#         )
#         if total_refunded + self.amount > self.payment.amount:
#             raise ValueError("Refund amount cannot exceed payment amount")
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Refund {self.id} for Payment {self.payment.id}"