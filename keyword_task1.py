#Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks
#  for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.
# reviews = ["This product is really good. I'm impressed with its quality.",
# "The performance of this product is excellent. Highly recommended!",
# "I had a bad experience with this product. It didn't meet my expectations.",
# "Poor quality product. Wouldn't recommend it to anyone.",
# "The product was average. Nothing extraordinary about it."
    
my_keywords= ["good", "excellent", "bad", "poor", "average"]
reviews= [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
for string in reviews:
    for keyword_string in my_keywords:
        string=string.replace(keyword_string,keyword_string.upper())
    print(string)
