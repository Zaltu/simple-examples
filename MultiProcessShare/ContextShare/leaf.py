"""
Leaf is our executable running in another process, potentially on another host.
"""
#pylint: disable=invalid-name
import processor

result = processor.memes.nd.dreams({"1":"AKA"}, aka="MAD")
print("Result is %s" % result)


result = processor.the.oc.clan({"2":"luigi"}, smug=2)
print("Result is %s" % result)
