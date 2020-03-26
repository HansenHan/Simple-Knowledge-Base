# In[1]:


# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"


# In[2]:


# Load .txt file and read rules.
# Return a list of head and tails for each rules
def load_text(ss):
    f= open(ss,"r")
    rule = list(f)
    head = []
    tails = []
    for i in rule:
        ele = i.split("<--", 1)
        head.append(ele[0].strip())
        items = ele[1].split('&')
        for j in range(len(items)):
            items[j] = items[j].strip()
        tails.append(items)
    com = [head, tails]
    print("   "+str(len(head))+" definite clauses read in:")
    for j in rule:
        print("   "+j, end = '')
    f.close()
    return com


# In[3]:


# load_text("sample.txt")


# In[4]:


# Infer atoms based on kb and rules
# Return a list of inferred atoms
def infer_all(kb, rules):
    head = rules[0]
    tails = rules[1]
    infer_c = []
    com = []
    find_one = False
    
    while 1:
        find_one = False
        com = kb + infer_c
        
        for idx, rul in enumerate(tails):
            test = True
            for each_ele in rul:
                if(each_ele not in com):
                    test = False
                    break
            if(test):
                if(head[idx] not in com):
                    infer_c.append(head[idx])
                    find_one = True

        if(not find_one):
            break
    return infer_c


# In[5]:


def start_input():
    kb = []
    rules = []
    while 1:
        ss = input("kb> ")
        if(ss == ""):
            continue
        ss_list = ss.split()
        
#         Exit program:
        if(ss_list[0] == "Exit"):
            return
        
#         Load .txt file of rules:
        if(ss_list[0] == "load"):
            if(len(ss_list) <= 1):
                print("Error: load needs the file name (end with .txt)")
            else:
                try:
                    rules = load_text(ss_list[1])
                except:
                    print("Error: "+ss_list[1]+" is not a valid knowledge base")
        
#         Tell atoms:
        elif(ss_list[0] == "tell"):
            if(len(ss_list) <= 1):
                print("Error: tell needs at least one atom")
            else:
                all_atom = True
                for val in ss_list[1:]:
                    if(not is_atom(val)):
                        print('Error: "'+val+'" is not a valid atom')
                        all_atom = False
                        break
                if(not all_atom):
                    continue
                for idx, val in enumerate(ss_list[1:]):
                    if val in kb:
                        print('  atom "'+val+'" already known to be true')
                    else:
                        kb.append(val) # Add atom to KB
                        print('  "'+val+'" added to KB')

#         Infer atoms:
        elif(ss == "infer_all"):
            if(kb == []):
                print("Error: tell at least one atom before infer")
            elif(rules == []):
                print("Error: please load your clauses first")
            else:
                c = infer_all(kb, rules)
#                 Print Inferred atoms for UI:
                print("  Newly inferred atoms:")
                if(c == []):
                    print("     <none>")
                else:
                    print("     ",end = '')
                    for idx_c, each_c in enumerate(c):
                        if(idx_c == (len(c)-1)):
                            print(each_c)
                        else:
                            print(each_c,end = ' ')
                print("  Atoms already known to be true:")
                print("     ", end = '')
                for idx_kb, each_kb in enumerate(kb):
                    if(idx_kb == (len(kb)-1)):
                        print(each_kb)
                    else:
                        print(each_kb, end = ", ")
                kb = kb+c
                
#         Clear atoms:
        elif(ss == "clear_atoms"):
            kb = []
            print("  Successfully clear all atoms")
            
#         Cannot find command:
        else:
            print('Error: unknown command "'+ss+'"')


# In[6]:


start_input()


# In[ ]:




