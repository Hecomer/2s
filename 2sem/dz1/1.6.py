def number_in_english(number):
    numbers = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    numbers2 = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }
    number3 = {
        0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'
    }
    if len(str(number)) == 1:
        print(numbers[number])
    elif len(str(number)) == 2:
        if str(number)[0] == 1:
            print(number3[int(str(number)[1])])
        else:
            print(numbers2[int(str(number)[0])] + ' ' + numbers[int(str(number)[1])])
    elif len(str(number)) == 3:
        if str(number)[1] == 1:
            print(numbers[int(str(number)[0])] + ' hundred ' + number3[int(str(number)[1])])
        else:
            print(numbers[int(str(number)[0])] + ' hundred ' + numbers2[int(str(number)[1])] + ' ' + numbers[int(str(number)[2])])

number_in_english(48)