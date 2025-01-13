
from utils.cmd import cmd, check_cmd
from utils.visualizer import parse_dot_to_diagram
from utils.files import writefiles, clear_terraform_files, closefile, replace_terraform_file, writefile, upload_image
from models.generate_graph_model import GenerateGraphModel
from multiprocessing import Process, JoinableQueue
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger(__name__)

number_queue = JoinableQueue()
str_queue = JoinableQueue()
processes = {}

def consumer(in_queue: JoinableQueue, out_queue: JoinableQueue, file: str):
    print(file)
    while True:
        item = in_queue.get()
        heavy_task(item, file)
        out_queue.put(item.id)
        in_queue.task_done()

def heavy_task(x: GenerateGraphModel, file):

    process_file = f"terraform/{file}/{file.split('_')[1]}.tf"
    directory = f"terraform/{file}"
    print("currently working on:", file)
    try:
        file_x = x.file
        print(file_x)
        writefiles(directory, x.file)
        cmd(["terraform", "init"], directory)
        cmd(["terraform", "validate"], directory)
        dot_content = check_cmd(["terraform", "graph", "-draw-cycles"], directory)
        dot_file_path = "/".join([directory, "graph.dot"])
        writefile(dot_file_path, str(dot_content.decode("utf-8") ))
        parse_dot_to_diagram(dot_file_path, f"{directory}/graph")
    except Exception as e:
        print("Error", e)
    finally:
        print("rollback")
        clear_terraform_files(directory)

class Threads:
    try:
        def start(self):
            print("running")
            for i in range(4):
                p = Process(target=consumer, args=(number_queue, str_queue, f'terraform_{i+1}'), daemon=True)
                p.start()
    except Exception as e:
        print("Error", e)

async def producer(req: GenerateGraphModel):
    try:
        number_queue.put(req)
        return number_queue.qsize()
    except Exception as e:
        return {"Error": e}

