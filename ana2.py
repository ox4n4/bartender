# make user ingredient list file
# make two txt file in the same folder for this to work: avaliable.txt and unavaliable.txt

search_item = input('What ingredient do you have?')

with open('avaliable.txt', 'r') as drink_file:
    avaliable = drink_file.read()
    avaliable = avaliable + ' ' + search_item

with open('avaliable.txt', 'w+') as drink_file:
    drink_file.write(avaliable)

no_item = input("What ingredient don't you want in your drink?")

with open('unavaliable.txt', 'r') as no_file:
    unavaliable = no_file.read()
    unavaliable = unavaliable + ' ' + no_item

with open('avaliable.txt', 'w+') as drink_file:
    drink_file.write(unavaliable)

    # have to pull up API to compare then we can print this
    print("here is some of the recipe with {} and without {}".format(avaliable, unavaliable))

# need to pull up the API to compare

if search_item in the_API:
    print
    the_API

    