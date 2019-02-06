from selenium import webdriver
from pprint import pprint
driver = webdriver.Firefox()
driver.get('https://www.bespokepost.com')

def get_css_values():
    elements_css_dict = {}
    elements = driver.find_elements_by_xpath("//*[not(*)]")
    for element in elements:
        '''try:
            styleprops_dict = driver.execute_script('var items = {};'+
            'var compsty = getComputedStyle(arguments[0]);'+
            'var len = compsty.length;'+
            'for (index = 0; index < len; index++)'+
            '{items [compsty[index]] = compsty.getPropertyValue(compsty[index])};'+
            'return items;', element)
            elements_css_dict.update({element:styleprops_dict})
        except:
            print("failed")'''

        try:
            print(element.rect)
        except:
            print("failed")

    return elements_css_dict

d1=get_css_values()
print(len(d1.keys()))

input('>>>')

d2=get_css_values()
print(len(d2.keys()))

'''for key in d2.keys():
    if key in d1.keys():
        if not d2[key] == d1[key]:
            for subkey in d2[key].keys():
                if not d2[key][subkey] == d1[key][subkey]:
                    print("\n\n_________________________")
                    print(key.get_attribute('outerHTML'))
                    print("\n"+str(subkey))
                    print(d2[key][subkey])
                    print(d1[key][subkey])
'''
