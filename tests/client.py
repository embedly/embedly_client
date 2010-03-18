import embedly

# print out response
import pprint
oembed_json = embedly.get_oembed('http://www.youtube.com/watch?v=60og9gwKh1o')
pprint.pprint(oembed_json)

