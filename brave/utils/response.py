
def BraveErrorResponse(code, msg):
    return {"retCode":code,
            "retMsg":msg
    }

def BraveResponse(data):
    return {"retCode":0,
        "retMsg":"",
        "data":data
     }
