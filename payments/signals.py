# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Refund, PaymentStatus, RefundStatus


# @receiver(post_save, sender=Refund)
# def update_payment_status(sender, instance, **kwargs):
#     """Auto-update payment status when refunds are made."""
#     payment = instance.payment
#     successful_refunds = sum(
#         refund.amount for refund in payment.refunds.filter(status=RefundStatus.SUCCESS)
#     )

#     if successful_refunds >= payment.amount:
#         payment.status = PaymentStatus.REFUNDED
#         payment.save(update_fields=["status"])