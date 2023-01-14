class ArgsParse(object):
    PARAMS_NAME = 'name'
    PARAMS_IP = 'ip'
    PARAMS_NO = 'no'


class Constant(object):
    NAME_ADMIN = 'wtl'


if __name__ == '__main__':

    params = {'name': 'wtl', 'ip': '192'}
    post_data = {
        ArgsParse.PARAMS_NAME: params.get(ArgsParse.PARAMS_NAME, None),
        ArgsParse.PARAMS_NO: params.get(ArgsParse.PARAMS_NO, None),
    }
    post_data.update([("AAA", "aaa"), ("BBB", "bbb")])
    # print(params)
    print(post_data)
    if params.get(ArgsParse.PARAMS_NAME, None) == Constant.NAME_ADMIN:
        print('yes')

    if params.get(ArgsParse.PARAMS_NO, None) == Constant.NAME_ADMIN:
        print('ohh yes')
