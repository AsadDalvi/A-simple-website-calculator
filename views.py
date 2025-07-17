from django.shortcuts import render

# Create your views here.

def simplecalcapp(request):
    result = ""
    if request.method == "POST":
        num1 = request.POST.get('num1', "")
        num2 = request.POST.get('num2', "")
        operation = request.POST.get('operation', "")

        try:
            if num1 and num2 and operation:
                num1 = int(num1)
                num2 = int(num2)
                if operation == 'add':
                    result = num1 + num2
                elif operation == 'sub':
                    result = num1 - num2
                elif operation == 'mul':
                    result = num1 * num2
                elif operation == 'div':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Error: Division by zero"
            else:
                result = "Check Input"
        except ValueError:
            result = "Check Input"

    return render(request, 'simplecalcapp.html', {'result': result})
