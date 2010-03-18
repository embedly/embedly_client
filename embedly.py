# Built in library imports
import re

# Server imports
import urllib
import urllib2
import json

# Embed.ly Multi Provider API Endpoint
OEMBED_API_ENDPOINT = 'http://api.embed.ly/v1/api/oembed'

# URL Schemes Supported
URL_SCHEMES_RE = (
    r'^http://www\.5min\.com/Video/.*',
    r'^http://[\w\.-]+\.viddler\.com/explore/.*/videos/(?P<id>\w+)/?',
    r'^http://qik\.(ly|com)/video/.*',
    r'^http://qik\.(ly|com)/.*',
    r'^http://www\.hulu\.com/watch/.*',
    r'^http://[\w\.-]+\.revision3\.com/.*',
    r'^http://([\w\.-]+\.|)nfb\.ca/film/.*',
    r'^http://[\w\.-]+\.dailymotion\.com/video/.*',
    r'^http://blip\.tv/file/.*',
    r'^http://[\w\.-]+\.scribd\.com/doc/.*',
    r'^http://[\w\.-]+\.movieclips\.com/watch/.*',
    r'^http://screenr.com/.+',
    r'^http://twitpic\.com/.*',
    r'^http://[\w\.-]+\.youtube\.com/watch.*',
    r'^http://yfrog\.[\w\.-]+/.*',
    r'^http://([\w\.-]+\.|)amazon\.[\w\.-]+/gp/product/(?P<ASIN>[\w-]+).*$',
    r'^http://([\w\.-]+\.|)amazon\..*/(?P<product_slug>[\w-]+)/dp/(?P<ASIN>[\w-]+).*$',
    r'^http://([\w\.]+\.|)flickr.com/.*',
    r'^http://www\.vimeo\.com/groups/[\w-]+/videos/.*',
    r'^http://www\.vimeo\.com/.*',
    r'^http://tweetphoto\.com/.*$',
    r'^http://www\.collegehumor\.com/video:.*',
    r'^http://www\.funnyordie\.com/videos/.*',
    r'^http://video\.google\.com/videoplay?.*',
    r'^http://www\.break\.com/[\w-]+/.*',
    r'^http://www\.slideshare\.net/[\w-]+/.*',
    r'^http://www\.ustream\.tv/recorded/.*',
    r'^http://www\.ustream\.tv/channel/.*',
    r'^http://www\.twitvid\.com/.*',
    r'^http://www\.justin.tv/clip/.*',
    r'^http://www\.justin.tv/.*',
    r'^http://vids\.myspace\.com/index.cfm\?fuseaction=vids\.individual&videoid.*$',
    r'^http://www\.metacafe\.com/watch/.*',
    r'^http://([\w\.-]+\.|)crackle\.com/c/.*',
    r'^http://www\.veoh\.com/.*/watch/.*',
    r'^http://www\.fancast\.com/(tv|movies)/.*/videos',
    r'^http://(\w+\.|)imgur\.com/(?P<key>[\w-]+).(?P<format>[\w-]+)$',
    r'^http://(\w+\.|)imgur\.com/(?P<key>[\w-]+)$',
)


def is_pattern_match(url):
    for pat_re in URL_SCHEMES_RE:
        if re.search(pat_re, url):
            return True
    return False

# returns a dictionary of the oembed object
def get_oembed(url, format='json', maxwidth=None, maxheight=None):

    # make sure embed.ly supports the url scheme
    if not is_pattern_match(url):
       return None

    # gather url, format, maxwidth or maxheight options for embed sizing
    params = {"url": url}
    if maxwidth is not None:
        params['maxwidth'] = maxwidth
    if maxheight is not None:
        params['maxheight'] = maxwidth
    if format is not None:
        params['format'] = format
    
    # generate query string
    query = urllib.urlencode(params)

    # api endpoint url
    fetch_url = "%s?%s" %(OEMBED_API_ENDPOINT,query)

    try:
        r = urllib2.urlopen(fetch_url).read()
        obj = json.loads(r)
    except urllib2.HTTPError, e:
        return None
    except urllib2.URLError:
        return None

    return obj



