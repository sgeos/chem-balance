import re

elementPattern      = re.compile('([A-Z][a-z]*)(\d*)')
elementGroupPattern = re.compile('\(((?:[A-Z][a-z]*\d*)+)\)(\d*)')

def elementList( equation, multiplier=1, result=None, ):
    result = result or {}
    for ( element, count ) in elementPattern.findall ( equation ):
        try:
            count = int( count )
        except ValueError, e:
            count = 1
        count = count * multiplier
        try:
            result[ element ] = result[ element ] + count
        except KeyError, e:
            result[ element ] = count
        # print element, count
    # result = { item[ 0 ]: item[ 1 ] * multiplier for item in result.items() }
    return result

def elementString ( elementList ):
    return "".join ([str(k)+str(v) for (k,v) in elementList.items()])

# def mysub( mymatch ):
    # print mymatch.group(1), mymatch.group(2)
    # return elementString(elementList(str(mymatch.group(1)), int(mymatch.group(2))))

def flattenEquation( equation ):
    mysub  = lambda mymatch: elementString(elementList(str(mymatch.group(1)), int(mymatch.group(2))))
    result = elementGroupPattern.sub(mysub, equation)
    # print result
    while (result != equation):
        equation = result
        result   = elementGroupPattern.sub(mysub, equation)
        # print result
    return result

def complexElementList( equation ):
    return elementList(flattenEquation( equation ))

