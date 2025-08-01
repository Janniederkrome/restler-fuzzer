""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_stores_post_id = dependencies.DynamicVariable("_stores_post_id")

def parse_storespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data, strict=False)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["id"])

        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_stores_post_id", temp_7262)

req_collection = requests.RequestCollection([])
# Endpoint: /stores, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stores"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

    {
        'post_send':
        {
            'parser': parse_storespost,
            'dependencies':
            [
                _stores_post_id.writer()
            ]
        }
    },

],
requestId="/stores"
)
req_collection.add_request(request)

# Endpoint: /stores/{storeId}/order, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stores"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_stores_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("order"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "tags":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "storeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "storeProperties":
        {
            "tags":"""),
    primitives.restler_custom_payload("/storeProperties/tags", quoted=False),
    primitives.restler_static_string(""",
            "intro":"""),
    primitives.restler_custom_payload("/storeProperties/intro", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "deliveryProperties":
        {
            "tags":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "rush":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "bagType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "items":
    [
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "deliveryTags":"""),
    primitives.restler_custom_payload("/items/[0]/deliveryTags", quoted=False),
    primitives.restler_static_string(""",
            "code":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "storeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "expirationMaxDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "useDoubleBags":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "bannedBrands":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/stores/{storeId}/order"
)
req_collection.add_request(request)
