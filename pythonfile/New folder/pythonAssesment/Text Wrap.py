import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
  
    word_list = wrapper.wrap(text=string) 
    w=""
    for i in word_list:
        w=w+i+"\n"

    return w


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)