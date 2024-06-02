def char_count(str):
  ans_dic = {}
  #create dictionary from string
  for let in str:
    if let == " ":
      continue
    elif let in ans_dic.keys():
      ans_dic[let] += 1
    else:
      ans_dic[let] = 1
  #sort dictionary by values in descending order
  sorted_dict = dict(sorted(ans_dic.items(), key=lambda item: item[1], reverse=True))
  
  return sorted_dict

