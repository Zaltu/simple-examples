"""
Definitely NOT break Google's terms of service and submit HTTP requests to the Google Translate service
"""
import re
import html
import time
import urllib.parse
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

AGENT = {
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
SELE_GTRAN_URL = "https://translate.google.com/#view=home&op=translate&sl={sl}&tl={tl}&text={text}"
SELE_KEYSTR_URL = "https://translate.google.com/#view=home&op=translate&sl={sl}&tl={tl}"

HEADLESS = Options()
HEADLESS.add_argument("--headless")
DRIVER = webdriver.Chrome(options=HEADLESS)
DRIVER.get("about:blank")

def timeit(method):
    """
    Decorator for timed

    :param function method: function to call

    :returns: decorator
    :rtype: function
    """
    def timed(*args, **kwargs):
        """
        Executes function and prints how long it took.

        :param args: function args
        :param kwargs: function kwargs

        :returns: function return
        :rtype: unknown
        """
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


@timeit
def wreq(to_translate, to_language="en", from_language="auto"):
    """
    Translate the text "to translate" into the specified langage from the specified language by bypassing
    the auth restrictions from google. Done by passing a deprecated mobile version of firefox as the source
    agent.

    :param str to_translate: text to be translated
    :param str to_language: language to translate to, defaults to english.
    :param str from_language: language to translate from. Defaults to 'auto'. Results may vary.

    :returns: translated text
    :rtype: str
    """
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    print(link)
    response = requests.get(link, headers=AGENT)
    data = response.text
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if len(re_result) == 0:  #pylint: disable=len-as-condition
        result = ""
    else:
        result = html.unescape(re_result[0])
    return result


@timeit
def withSelenium_URL(to_translate, to_language="en", from_language="auto"):
    """
    Translate the text "to translate" into the specified langage from the specified language using the
    Selenium framework. This implementation directly fetches the URL. Slower and less stable due to URI
    restriction but only requires a call. No need to parse the page to send the request.

    :param str to_translate: text to be translated
    :param str to_language: language to translate to, defaults to english.
    :param str from_language: language to translate from. Defaults to 'auto'. Results may vary.

    :returns: translated text
    :rtype: str
    """
    to_translate = urllib.parse.quote(to_translate)
    DRIVER.get(SELE_GTRAN_URL.format(text=to_translate, sl=from_language, tl=to_language))
    elem = DRIVER.find_element_by_class_name("translation")
    return elem.text


@timeit
def withSeleniumKeys(to_translate, to_lang="en", from_lang="auto"):
    """
    Translate the text "to translate" into the specified langage from the specified language using the
    Selenium framework. This implementation assumes the Selenium driver is already pointing to the google
    translate page, and simply selects the requested language via URL HTML tag and sends keystrokes. This is
    much faster than the other implementation and generally more stable, but requires extra interaction with
    Selenium. Note that the speed improvement is essentially void if Selenium is not already pointing towards
    the right base page.

    :param str to_translate: text to be translated
    :param str to_lang: language to translate to, defaults to english.
    :param str from_lang: language to translate from. Defaults to 'auto'. Results may vary.

    :returns: translated text
    :rtype: str
    """
    DRIVER.get(SELE_KEYSTR_URL.format(sl=from_lang, tl=to_lang))
    sElem = DRIVER.find_element_by_id("source")
    sElem.send_keys(to_translate)
    text = None
    cutoff = time.time()
    while not text and (time.time() - cutoff) < 1:
        try:
            elem = DRIVER.find_element_by_class_name("translation")
            text = elem.text
        except NoSuchElementException:
            pass
    if not text:
        text = "Translation taking too long, aborted..."
    return text


print("Requests w/ mocked Firefox")
print(wreq("Hello world", "fr"))
print("Selenium w/ URL")
print(withSelenium_URL("Hello World", "fr"))
print("Prepping for Selenium keystroke")
DRIVER.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=en")
print("Selenium by keystroke")
print(withSeleniumKeys("Hello world", "ja"))



DRIVER.close()
