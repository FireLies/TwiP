from tkinter import *


window = Tk()
width = height = 450
window.title('Twin Prime')
canv = Canvas(window, width=width, height=height, bg='#000017', highlightthickness=0)
canv.pack()

def isprime(num):
    if num > 1:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True
    else:
        return False


prime, twin = [i for i in range(width) if isprime(i)], []
for index, p in enumerate(prime):
    if index + 1 != len(prime):
        if p + 2 == prime[index + 1]:
            twin.append(f"{p, prime[index + 1]}")
            canv.create_line(p + 5, height, p + 5, height - p, fill='#4B4BFF', width=2)
 
canv.create_text(50, 35, fill='White', text=f"Numbers: {width}\nPrime: {len(prime)}\nTwin: {len(twin)}")
window.mainloop()