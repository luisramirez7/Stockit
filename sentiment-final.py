import httplib, urllib, base64

def sentiment(text):

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'YOURAPIMSUBSCRIPTION',
    }

    params = urllib.urlencode({
    })

    body = "{\n   'documents': [\n  {\n  'language': 'en',\n  'id': 'string',\n      'text': '" + text + "'\n  }\n  ]\n}"

    try:
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))