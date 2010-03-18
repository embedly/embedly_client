import embedly

# print out response
import pprint
oembed_json = embedly.get_oembed('http://www.flickr.com/photos/ende/7521239/')
pprint.pprint(oembed_json)

