def logger(original_func):

    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ram with args: {} and kwargs: {}'.format(args,kwargs))
        return original_func(*args,**kwargs)

    return wrapper

@logger
def display_info(name,age):
    print('Display info ran with the arguments ({},{})'.format(name,age))


display_info('Utsav', 28)