# from urllib3 import Retry
# from .signals import object_viewed_signal

# class objectViewMixin:
#     def dispatch(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except self.model.DoesNotExist:
#             instance = None

#         # if request.user.is_authenticated and instance is not None
#         if instance is not None:
#             object_viewed_signal.send(instance.__class__, instance=instance, request=request)

#         return super(objectViewMixin, self).dispatch(request, *args, **kwargs)
    
