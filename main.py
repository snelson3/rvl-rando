import shutil
import time, json, os, random, yaml

import os, re, shutil

from gooey import Gooey, GooeyParser

# Then the main file generation will be really easy, an argument to set 0, set 50, infinite, random swap, random values, and an openkh location

@Gooey(program_name="Kingdom Hearts 2 Revenge Value Limit Randomizer")
def main_ui():
    main()

def main(cli_args: list=[]):
    values=[92.0, 75.0, 92.0, 75.0, 100.0, 75.0, 75.0, 55.0, 75.0, 75.0, 75.0, 75.0, 100.0, 100.0, 75.0, 75.0, 75.0, 50.0, 80.0, 75.0, 100.0, 75.0, 100.0, 75.0, 100.0, 5.0, 200.0, 200.0, 200.0, 200.0, 50.0, 80.0, 60.0, 60.0, 60.0, 60.0, 50.0, 40.0, 40.0, 75.0, 100.0, 75.0, 100.0, 150.0, 125.0, 50.0, 50.0, 30.0, 60.0, 60.0, 100.0, 100.0, 100.0, 100.0, 80.0, 70.0, 60.0, 50.0, 100.0, 80.0, 60.0, 40.0, 100.0, 80.0, 60.0, 40.0, 100.0, 80.0, 60.0, 40.0, 100.0, 80.0, 60.0, 40.0, 50.0, 95.0, 90.0, 85.0, 80.0, 100.0, 40.0]

    last_settings = {
        "rando_type": "random_values",
        "minimum_value": 5,
        "maximum_value": 200,
        "seed": ""
    }
    default_config = {
        "openkh_dir": ""
    }
    if os.path.exists("last_settings.json"):
        last_settings = json.load(open("last_settings.json"))
    if os.path.exists("config.json"):
        default_config = json.load(open("config.json"))

    parser = GooeyParser()

    options = parser.add_argument_group(
        "Options",
        """prototype mod to randomize the revenge value limit of all bosses that do not use the games default. Normally these values range anywhere from 5 to 200, but a few different options are offered
    set 0 - Set the revenge value limits to 0, so that a single attack will trigger revenge
    set X - Set the revenge value to the minimum value specified in the below option
    set infinite - Set the revenge value to a really high value of 9999 that seems unlikely to ever be hit
    random swap - Take the 83 instances in boss ai where revenge value limit is set, and randomly swap these values with each other
    random values - Independently randomize each instance of setting RVL to a random value between the set minimum and maximum"""
    )

    options.add_argument("-rando_type", choices=["set_0", "set_x", "set_infinite", "random_swap", "random_values"], default=last_settings.get("rando_type"))
    options.add_argument("-seed", help="empty is random", default=last_settings.get("seed"))
    options.add_argument("-minimum_value", default=last_settings.get("minimum_value"), widget='IntegerField')
    options.add_argument("-maximum_value", default=last_settings.get("maximum_value"), widget='IntegerField')
   

    options.add_argument("-openkh_dir", help="Path to OpenKH folder.", default=default_config.get("openkh_dir"), widget='DirChooser')

    # Parse and print the results
    if cli_args:
        args = parser.parse_args(cli_args)
    else:
        args = parser.parse_args()

    settings_to_write = {
        "rando_type": args.rando_type,
        "minimum_value": args.minimum_value,
        "maximum_value": args.maximum_value,
        "seed": args.seed
    }
    config_to_write = {
        "openkh_dir": args.openkh_dir
    }
    json.dump(config_to_write, open("config.json", "w"))
    json.dump(settings_to_write, open("last_settings.json", "w"))

    rando_type = args.rando_type
    minimum = int(args.minimum_value)
    maximum = int(args.maximum_value)
    seed = args.seed if args.seed else time.time()

    random.seed(seed)

    if rando_type == "random_swap":
        random.shuffle(values)
    elif rando_type.startswith("set"):
            setvalue = minimum
            if rando_type.endswith("0"):
                setvalue = 0
            elif rando_type.endswith("infinite"):
                setvalue = 9999
            values = [setvalue for _ in values]
    else:
        values = [random.randint(minimum, maximum) for _ in values]

    moddir = os.path.join(args.openkh_dir, "mods", "kh2", "rvlrando")
    if os.path.exists(moddir):
        shutil.rmtree(moddir)
    os.makedirs(moddir)

    modyml = {
        "name": "Revenge Value Randomizer: Seed {}".format(seed),
        "description": "Settings:\n{}".format(settings_to_write),
        "assets": []
    }
    def writeAi(fn, text):
        dirname = os.path.dirname(fn)
        dirtree = dirname.split(os.sep)
        modelname = dirtree[-1]

        relfn = os.path.join(modelname+"_"+os.path.basename(fn))
        outfn = os.path.join(moddir, relfn)

        with open(outfn, "w") as f:
            f.write(text)
        return {
            "method": "binarc",
            "name": "obj/{}.mdlx".format(modelname),
            "source": [
                {
                    "method": "bdscript",
                    "name": os.path.basename(fn).split(".")[0][:4],
                    "source": [{"name": relfn}],
                    "type": "Bdx"
                }
            ]
        }

    for root, dirs, files in os.walk(os.path.join("bdscript")):
        for ff in files:
            fn = os.path.join(root, ff)
            with open(fn) as f:
                txt = f.read()
            karma_param = re.compile(r'pushImmf (.*)\n.*; trap_enemy_set_karma_limit')
            text = karma_param.sub(lambda m: str(values.pop()), txt)
            # Will cheat with git to test things later
            writeAi(fn, text)

if __name__ == "__main__":
    main()