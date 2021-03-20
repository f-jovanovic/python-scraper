import concurrent.futures


def execute_concurrently(function, args):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = list()
        for item in args:
            futures.append(executor.submit(function, item))

        for future in concurrent.futures.as_completed(futures):
            print(future.result(30))
