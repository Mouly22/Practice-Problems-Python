def jsonfile(a, b):
    for i in range(len(a)):
        if len(a) != len(b):
            return 'different'
        else:
            return 'same'




a = '{"browsers": {"firefox": {"name": "Firefox","pref_url": "about:config","releases": {"1": {"release_date": "2004-11-09","status": "retired","engine": "Gecko","engine_version": "1.7"}}}}}'
b = '{"browsers":{"firefox":{"name":"Firefox","pref_url":"about:config","releases":{"1":{"engine":"Gecko","engine_version":"1.7","release_date":"2004-11-09","status":"retired"}}}}}'
jsonfile(a, b)
