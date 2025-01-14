
from utils.cmd import cmd, check_cmd
from utils.visualizer import parse_dot_to_diagram
from utils.files import writefiles, clear_terraform_files, closefile, replace_terraform_file, writefile, upload_image
from models.generate_graph_model import GenerateGraphModel
from multiprocessing import Process, JoinableQueue
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger(__name__)

number_queue = JoinableQueue()
processes = {}

def consumer(in_queue: JoinableQueue, dir: str):
    while True:
        item = in_queue.get()
        heavy_task(item, dir)
        in_queue.task_done()

def heavy_task(data: GenerateGraphModel, dir):

    directory = f"terraform/{dir}"
    logger.info(f"currently working on: {dir}")
    try:
        files = data.files
        writefiles(directory, files)
        cmd(["terraform", "init"], directory)
        cmd(["terraform", "validate"], directory)
        dot_content = check_cmd(["terraform", "graph", "-draw-cycles"], directory)
        dot_file_path = "/".join([directory, "graph.dot"])
        writefile(dot_file_path, str(dot_content.decode("utf-8") ))
        image_path = parse_dot_to_diagram(dot_file_path, f"{directory}/graph")
        upload_image(".".join([image_path, "png"]), data.id)    
    except Exception as e:
        print("Error", e)
    finally:
        print("rollback")
        clear_terraform_files(directory)

class Threads:
    try:
        def start(self):
            logger.info("starting threads")
            for i in range(4):
                p = Process(target=consumer, args=(number_queue, f'terraform_{i+1}'), daemon=True)
                p.start()
    except Exception as e:
        logger.error(e)

async def producer(req: GenerateGraphModel):
    try:
        number_queue.put(req)
        # print number_queue readable
        return {"message": "task sheduled successfully", "task_id": req.id}
    except Exception as e:
        return {"Error": e}

