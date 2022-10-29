import first

n = input("Добрый день! Чем я могу Вам помочь?" + "\n")

while n != "off":
    first.get_req(n)
    n = input("Чем я могу Вам помочь?" + "\n")