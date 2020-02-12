import math, logging, distgfs, pickle
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def levi(x, y):
    """
    Levi's function (see https://en.wikipedia.org/wiki/Test_functions_for_optimization).
    Has a global _minimum_ of 0 at x=1, y=1.
    """
    a = math.sin(3. * math.pi * x)**2
    b = (x - 1)**2 * (1 + math.sin(3. * math.pi * y)**2)
    c = (y - 1)**2 * (1 + math.sin(2. * math.pi * y)**2)
    return a + b + c


def obj_fun(x, y, pid):
    """ Objective function to be _maximized_ by GFS. """
    res = levi(x, y)
    logger.info(f"Iter: {pid}\t x:{x}, y:{y}, result:{res}")
    # Since Dlib maximizes, but we want to find the minimum,
    # we negate the result before passing it to the Dlib optimizer.
    return -res

if __name__ == '__main__':

    # For this example, we pretend that we want to keep 'y' fixed at 1.0
    # while optimizing 'x' in the range -4.5 to 4.5
    space = {'x': [-4.5, 4.5]}
    problem_parameters = {'y': 1.}
    
    # Create an optimizer parameter set
    distgfs_params = {'opt_id': 'distgfs_levi',
                      'obj_fun_name': 'obj_fun',
                      'obj_fun_module': 'example_distgfs_levi',
                      'problem_parameters': problem_parameters,
                      'space': space,
                      'n_iter': 10,
                      'file_path': 'distgfs.levi.h5',
                      'save': True
                      }

    distgfs.run(distgfs_params, verbose=True)

