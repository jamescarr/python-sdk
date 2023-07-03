from pytest import fail


def test_metadata_payload_contruction_and_retrieval():
    # given
    flag_metadata = ImmutableMetadata.builder()\
        .add("string", "string")\
        .add("integer", 1)\
        .add("long", 1)\
        .add("float", 1.5)\
        .add("double", float('inf'))\
        .add("boolean", False)\
        .build()

    # then
    assert flag_metadata.data["string"] == "string"
    assert flag_metadata.data["integer"] == 1
    assert flag_metadata.data["long"] == 1
    assert flag_metadata.data["float"] == 1.5
    assert flag_metadata.data["double"] == float('inf')
    assert flag_metadata.data["boolean"] == False

def test_value_mismatch_returns_none():
    pass

def test_none_returned_if_key_does_not_exist():
    pass


