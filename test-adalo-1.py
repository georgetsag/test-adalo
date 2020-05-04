def handler(event, context):
    print(event)
    return {"records":
                     [{"id":"1","fields":{ "message": "Successfully executed"} } ] }
