from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response


class Fibonacci(APIView):
    def fibonacci_series(self, x, y, n):
        if x == 0 and y == 0:
            return [0]
        elif n == 0:
            return [x, y]
        else:
            series = [x, y]
            for _ in range(2, n + 2):
                next_num = series[-1] + series[-2]
                series.append(next_num)
            return series[:-2]

    def get(self, request):
        # Obtener la hora actual
        current_time = datetime.now()

        # Obtener las semillas de la serie Fibonacci
        seed1 = current_time.minute // 10  # Primer dígito de los minutos
        seed2 = current_time.minute % 10   # Segundo dígito de los minutos

        # Calcular los N primeros números de la serie Fibonacci
        n = current_time.second  # Utilizar los segundos como cantidad de números a generar
        fib_numbers = self.fibonacci_series(seed1, seed2, n)

        # Generar la respuesta JSON
        response_data = {
            "current_time": current_time.strftime("%H:%M:%S"),
            "seed1": seed1,
            "seed2": seed2,
            "fibonacci_numbers": fib_numbers[-n:]  # Tomar los últimos N números de la serie
        }
        return Response(response_data)


def enviar_correo(numero):
    try:
        # Envía el correo electrónico
        send_mail(
            '',
            'Mensaje del correo',
            'tu_correo_electronico',
            ['correo_destino@example.com'],
            fail_silently=False,
        )
        return "Correo enviado"
    except Exception as e:
        return "Error al enviar el correo: {}".format(e)



def fibonacci_series(x, y, n):
    if x == 0 and y == 0:
        return [0]
    elif n == 0:
        return [x, y]
    else:
        series = [x, y]
        for _ in range(2, n + 2):
            next_num = series[-1] + series[-2]
            series.append(next_num)
        return series[:-2]


