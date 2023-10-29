import re

NON_ALPHA_RE = re.compile('[^A-Z0-9]+')
POSTCODE_RE = re.compile('^[A-Z]{1,2}[0-9]{1,2}[A-Z]? [0-9][A-Z]{2}$')

def normalise_postcode(postcode):
    """Return a normalised postcode if valid, or None if not."""
    postcode = NON_ALPHA_RE.sub('', postcode.upper())
    postcode = postcode[:-3] + ' ' + postcode[-3:]
    if POSTCODE_RE.match(postcode):
        #return postcode
        print('Valid Postcode')
    else:
        print('Invalid Postcode')
    return None

postcode = str(input('Enter postcode: '))
normalise_postcode(postcode)