
#Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…"
#  to create a summary. Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",

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
def summary(my_list):
    review_summary, holder = '',''
    for i in range(len(my_list)):
        holder=my_list[i]
        x=30
        while holder[x]!=" ":
            x+=1
            #print(holder)
            #print(x)     
        my_list[i]=holder[:x]+"..."
        print("Summary:\n",end='')
        print(my_list)
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
summary(reviews)
    