"""
Leaf is our executable running in another process, potentially on another host.
"""
#pylint: disable=invalid-name
import processor

OUTOFSCOPE = "another value"

result = processor.the.oc.group("こんにちわ")
print("Result is %s" % result)
print(repr(result))
print(result.__class__)


result = processor.the.oc.clan()
print("Result is %s" % result)
result.prove()

result = processor.memes.nd.dreams()
print("Result is %s" % result)

result = processor.the.oc.clan()
print("Result is %s" % result)
result.prove()
result.move()

result = processor.other()
print("Result is %s" % result)

result = processor.memes.nd.NAME()
print("Result is %s" % result)
