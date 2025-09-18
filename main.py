from pyscript import display, document


def compute_area(e):
   
   b1 = float(document.getElementById('num1').value)
   b2 = float(document.getElementById('num2').value)
   height = float(document.getElementById('num3').value)
   area = (b1 + b2) * h / 2


   display(f'The area of a trapezoid is {area:.2f}')
