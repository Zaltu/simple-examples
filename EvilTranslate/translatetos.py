"""
Definitely NOT break Google's terms of service and submit HTTP requests to the Google Translate service
"""
import re
import html
import urllib.parse
import requests

agent = {
    'User-Agent':
        "Mozilla/4.0 (\
        compatible;\
        MSIE 6.0;\
        Windows NT 5.1;\
        SV1;\
        .NET CLR 1.1.4322;\
        .NET CLR 2.0.50727;\
        .NET CLR 3.0.04506.30\
        )"
}

def wreq(to_translate, to_language="auto", from_language="auto"):
    """
    Translate the text "to translate" into the specified langage from the specified language.
    """
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    print(link)
    response = requests.get(link, headers=agent)
    data = response.text
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if len(re_result) == 0:
        result = ""
    else:
        result = html.unescape(re_result[0])
    return result



print(wreq("Hello world", "fr"))
