# My self learned and coded lambda function example
def count_words(str):
  return len(str.split()) 

def list_word_initial(str_list):
  word_list = str_list.split()
  initial_list = [word[:1] for word in word_list]
  return initial_list

function_list = [count_words, list_word_initial]
string_api = "Give me the initials of the following employee string"
map_obj = map(lambda f : f(string_api), function_list)

result_list = list(map_obj)
print(result_list)