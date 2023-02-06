from django.utils import timezone
from restapis.colors import bcolors
from ipware import get_client_ip



class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.start_time = timezone.now()
        client_ip, is_routable = get_client_ip(request)
        
        if client_ip is None: 
            print("No IP Found")
        else:
            print(client_ip)


    def process_response(self, request, response):
        total_time = timezone.now() - request.start_time
        print(bcolors.OKCYAN ,'Time taken: {}'.format(total_time), bcolors.ENDC)

    def __call__(self, request):
        self.process_request(request)
        request.META['HTTP_CUSTOM_HEADER'] = "CUSTOM VALUE"
        response = self.get_response(request)
        
        self.process_response(request,response)
        return response



   
