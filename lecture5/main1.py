from progress.bar import Bar
import time


bar = Bar('', max=10)

for i in range(10):
    time.sleep(1)
    # Do some work
    bar.next()

bar.finish()