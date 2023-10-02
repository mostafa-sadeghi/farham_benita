# def get_chess_square_color(x,y):
#     if x % 2 == y % 2:
#         return "White"
#     else:
#         return "Black"

# print(get_chess_square_color(1,1))
# print(get_chess_square_color(1,2))
# print(get_chess_square_color(4,2))
# print(get_chess_square_color(4,4))

# numbers = list(range(1,101))
# print(numbers)

# numbera = []
# for i in range(1,101):
#     numbera.append(i)

# message = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

# print(message.count("Internet"))
# new_message = message.replace("Internet","net")
# print(new_message)

message = "The fox is looking for another fox"
# new_message = message.replace("fox","dog")
# print(new_message)

def my_count(message, word):
    i = 0
    count = 0
    while i < len(message):# i = 2
        if message[i:i+len(word)] == word  :
            count += 1

        i += 1
    return count

print(my_count(message, "fox"))




