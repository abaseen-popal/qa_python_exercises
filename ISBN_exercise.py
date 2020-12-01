digit_total = 0
isbn = list(str(input("Enter the 12 digit ISBN code: ")))
for i in range(len(isbn)):
    if i % 2 == 0:
        digit_total += int(isbn[i])
    else:
        digit_total += 3 * int(isbn[i])
        
last_digit = str(10 - (digit_total % 10))
isbn.append(last_digit)
isbn_formula = [isbn[0], isbn[1], isbn[2], '-', isbn[3], '-', isbn[4], isbn[5], isbn[6], '-', isbn[7], isbn[8],isbn[9], isbn[10], isbn[11], '-', isbn[12]]
print('last digit is: ',''.join(isbn_formula))
