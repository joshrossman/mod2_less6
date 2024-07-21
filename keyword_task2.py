#Task 2: Sentiment Tally
# Develop a function that tallies the number of positive
#  and negative words in each review.  The function should 
# return the total count of positive and negative words.
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
count_sent_list=[]
list_holder=[]
def count_sent(my_list):
     
    global list_holder
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    for i in range(len(my_list)):
        list_holder.append(my_list[i].upper())
    for i in range(len(my_list)):
        pos = 0
        neg =0
        for my_word in positive_words:
            if my_word.upper() in list_holder[i]:
                pos+=1
        for my_word in negative_words:
            if my_word.upper() in list_holder[i]:
                neg+=1 
        count_sent_list.append("There are " +str(pos)+ " positive words and " +str(neg) + " negative words in this review.\n")
        
    

my_keywords= ["good", "excellent", "bad", "poor", "average"]
reviews= [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
my_string=''
count_sent(reviews)
for i in range(len(reviews)):
    for keyword_string in my_keywords:
        reviews[i]=reviews[i].replace(keyword_string,keyword_string.upper())
    print(count_sent_list[i]+reviews[i]+"\n")
    
    

    
    

