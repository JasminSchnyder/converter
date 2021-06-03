def converter(atommasseEinheit):
    if float(guess) > 1000: 
         print("This is a heavy molecule!")

    msg_1 = " u sind ungefähr "
    msg_2 = " *10^(-27) kg."
    result = atommasseEinheit * 1.6605
    return str(atommasseEinheit) + msg_1 + str(result) + msg_2

guess = input("Input mass of molecule in [u]: ")

print(converter(float(guess)))

