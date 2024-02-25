# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"        # {} is the placeholder for str format

print("The " + animal + " jumped over the " + item)          # normal str.format
print("The {} jumped over the {}".format("cow", "moon"))     # value arguments
print("The {} jumped over the {}".format(animal, item))      # keyword / variable arguments
print("The {} jumped over the {}".format(item, animal))
print("The {0} jumped over the {1}".format(item, animal))    # positional arguments
print("The {1} jumped over the {0}".format(item, animal))
print("The {animal} jumped over the {item}".format(animal="sheep", item="moon"))     # key word argument


text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Prawin"
print("hello , my name is {}".format(name))
print("hello , my name is {}. nice to meet you".format(name))
print("hello , my name is {:10}. nice to meet you".format(name))
print("hello , my name is {:<10}. nice to meet you".format(name))
print("hello , my name is {:>10}. nice to meet you".format(name))
print("hello , my name is {:^10}. nice to meet you".format(name))


number = 3.14159
numbers = 1000000
print("The number pi is  {:f}".format(number))
print("The number pi is  {:.3f}".format(number))
print("The number  is  {:,f}".format(numbers))
print("The number  is  {:,}".format(numbers))
print("The number  is  {:f}".format(numbers))
print("The number  is  {:b}".format(numbers))
print("The number  is  {:x}".format(numbers))
print("The number  is  {:X}".format(numbers))
print("The number  is  {:e}".format(numbers))
print("The number  is  {:E}".format(numbers))


