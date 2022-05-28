def read_file_content(filename):
    with open(filename,'r') as file:
        contents=file.read()
        
         
    return contents  


def count_words():
    text = read_file_content("./story.txt")
    splitted_text = (text.split())
    count_dic = {}
    for i in splitted_text:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    return count_dic

        

    


print(count_words())

