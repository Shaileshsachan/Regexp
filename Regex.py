import re


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Metacharacters (Need to be searched):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321--555--4321
123.555.1234
232*323*2312
800-323-4243
900.454.4545

Mr. Shailesh
Mr Smith
Mrs Robinson
Ms Davis
Mr. T

cat
mat
pat

'''

emails = '''
shaileshsachan1997@gmail.com
shaileshsachan1998@gmail.com
shailesh.sachan@university.edu
shailesh-123-sachan@my-work.net
'''

urls = '''
https://www.google.com
http://shailesh.com
https://youtube.com
https://www.isro.gov
'''
sentence = 'Start a sentence and than bring it on an end'
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')    # not in the range negates
# pattern = re.compile(r'[^p]at')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'\d{3}[-]\d{3}[.]\d{4}')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

#emails
# pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.com') # Just two emails
# pattern = re.compile(r'[a-zA-Z0-9.-]+[@a-zA-Z0-9-]+\.(com|edu|net)')

# url
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# pattern = re.compile(r'(http|https)://(www\.)?[a-z]+\.(com|gov)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
pattern = re.compile(r'sentence')
pattern = re.compile(r'start', re.I)
# pattern = re.compile((r'https?://(www\.)?(\w+)(\.\w+)'))
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)
matches = pattern.finditer(urls)
# matches = pattern.findall()
matches = pattern.match(sentence)  # matches at start'
matches = pattern.search(sentence)
print(matches)
# for match in matches:
#     print(match)
# print(match.group(3))


# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches  = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)
