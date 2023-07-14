# TODO Найдите количество книг, которое можно разместить на дискете
info_disc = 1.44
list_book = 100
str_book = 50
simb = 25
bit = 4  # Для хранения кода одного символа нужно 4 байта.

simb_book = (str_book * simb) * list_book
total_bit = simb_book * bit
info_disc_bit = (info_disc * 1024) * 1024
count_book = int(info_disc_bit // total_bit)

print("Количество книг, помещающихся на дискету:", count_book)



