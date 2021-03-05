from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Consumer
from api.serializers import ConsumerSerializer


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return HttpResponseRedirect(redirect_to=f"{reverse('fake_ivi', kwargs={'uid': serializer.data.get('id')})}")

    @action(detail=True, methods=["post"], url_name="update-income")
    def update_income(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# class InsightViewSet(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):


class FakeIVI(TemplateView):
    template_name = "api/ivi.html"

    def get_context_data(self, **kwargs):
        consumer = Consumer.objects.get(id=self.kwargs.get('uid'))
        form_action = reverse("consumer-update-income", kwargs={'pk': consumer.id})
        return {"consumer": consumer, "form_action": form_action}