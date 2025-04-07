import time 

def perf_(func):
    def wrapper():
        start = time.time()
        print('Running program...')
        func()
        end = time.time()
        print(f'Time taken to run the program : {end-start} seconds')
    return wrapper

def store_weights(coefficiant,intercept):
    try :
        with open('weights/weights.txt','w') as f:
            f.write(str([coefficiant,intercept]))

    except FileNotFoundError as e:
        print('File not found! ',e)

    except ValueError as e:
        print('Invalid Value(not a string) ',e)

