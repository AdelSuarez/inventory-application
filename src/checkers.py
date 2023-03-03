def validate_empty_int(number):
    # Verify that the phone entered is numbers
    is_value = None
    try:
        if int(number): 
            is_value = True
    except:
        is_value = False

    return is_value

def delete_point( number, message):
    try:
        ip  = ''
        for i in number.get():
            if i != '.':
                ip += i
        return int(ip)
    except Exception:
        message