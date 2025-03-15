def get_num_words(text):
    return len(text.split())

def get_each_character(text):
    result = {}
    for i in text:
        if i.lower() in result:
            result[i.lower()] += 1
        else:
            result[i.lower()] = 1
    
    return result

def sort_on(dict):
    return dict["number"]


def sort_dictionary(base_dictionary):
    result = []
    for i in base_dictionary:
        result.append({"character": i, "number": base_dictionary[i]})
    
    result.sort(reverse=True, key=sort_on)
    return result

