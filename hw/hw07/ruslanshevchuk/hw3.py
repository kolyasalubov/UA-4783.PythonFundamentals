def couner_text(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else: 
            result[i] = 1        
    return result

print(couner_text("hello"))

    
