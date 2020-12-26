import sys
import time
import logging
import os
from distutils.dir_util import copy_tree
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

class EventHandlerObserver(LoggingEventHandler):
        def dispatch(self, event):
                if event.event_type == "created":
                        src=event.src_path
                        dst=os.environ["OUT_PATH"]
                        print(f"started copy from '{src}', out path: '{dst}'")
                        #dst="/tmp/test/"
                        if os.path.isdir(src):
                                time.sleep(3)
                                copy_tree(src, dst)
                                print("Done copying")
                        else:
                                print("Warn - folder does not exist.")
if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
        #path = sys.argv[1] if len(sys.argv) > 1 else '.'
        path = "/media/"
        event_handler = EventHandlerObserver()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
                while True:
                        time.sleep(1)
        finally:
                observer.stop()
                observer.join()


