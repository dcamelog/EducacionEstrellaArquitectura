from shadowd.django_connector import InputDjango, OutputDjango, Connector

def shadowdconnector(get_response):
    def middleware(request):
        input = InputDjango(request)
        output = OutputDjango()

        status = Connector().start(input, output)
        if not status == True:
            return status

        return get_response(request)

    return middleware
