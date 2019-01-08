def element_completely_viewable(driver, elem):
    elem_left_bound = elem.location.get('x')
    elem_top_bound = elem.location.get('y')
    elem_width = elem.size.get('width')
    elem_height = elem.size.get('height')
    elem_right_bound = elem_left_bound + elem_width
    elem_lower_bound = elem_top_bound + elem_height

    win_upper_bound = driver.execute_script('return window.pageYOffset')
    win_left_bound = driver.execute_script('return window.pageXOffset')
    win_width = driver.execute_script('return document.documentElement.clientWidth')
    win_height = driver.execute_script('return document.documentElement.clientHeight')
    win_right_bound = win_left_bound + win_width
    win_lower_bound = win_upper_bound + win_height

    left = bool(win_left_bound<=elem_left_bound)
    right = bool(win_right_bound>=elem_right_bound)
    top = bool(win_upper_bound<=elem_top_bound)
    bottom = bool(win_lower_bound>=elem_lower_bound)

    dict = { 'left':left, 'right':right, 'top':top, 'bottom':bottom }
    return dict

def parse():
    print("Gathering Information")
    element_visisbility_dictionary={}
    print('Length: '+str(len(elements)))
    for element in elements:
        dict={}
        value = element_completely_viewable(driver, element)
        dict.update({'dimensions':value})
        dict.update({'element':element})

        key = len(element_visisbility_dictionary)
        element_visisbility_dictionary.update({key:dict})

    pprint.pprint(element_visisbility_dictionary)

    print("Parsing Dictionaries")
    return_dictionary = {}
    for key in element_visisbility_dictionary.keys():
        array=[]
        element = element_visisbility_dictionary[key]['element']
        for value in element_visisbility_dictionary[key]['dimensions'].items():
            user.prompt(feed=value, type_of=True)
            user.prompt(feed=element, type_of=True)
            a, b = value
            if b == False:
                array.append(a)
                array.append(b)
        if len(array) > 0:
            return_dictionary.update({element:array})
    return return_dictionary

pprint.pprint(parse())
