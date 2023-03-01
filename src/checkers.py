def validate_empty_int(number):
    # Verify that the phone entered is numbers
    is_value = None
    try:
        if int(number): 
            is_value = True
    except:
        is_value = False

    return is_value