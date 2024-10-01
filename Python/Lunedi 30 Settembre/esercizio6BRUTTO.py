def compress_str():
    input_string = str(input("write a word or a sequence of letters: ").lower())
    to_compress = []
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            to_compress.append(input_string[i-1] + str(count))
            count = 1      

    to_compress.append(input_string[-1] + str(count))
    compressed_string = "".join(to_compress)
    print ("Your compressed string is: ", compressed_string)
compress_str()