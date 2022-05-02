import configparser
import collections

config = configparser.RawConfigParser()
config.read('escape_vm_worker.cfg')

#details_dict = dict(config.items('AUTH'))
#print(list(iter(details_dict)))

def get_config_by_section(cfg_section):

    if not hasattr(get_config_dict, 'config_dict'):
        get_config_dict.config_dict = dict(config.items(cfg_section))
    #print(list(iter(get_config_dict.config_dict)))
    return get_config_dict.config_dict

def get_config_dict():
    if not hasattr(get_config_dict, 'section_dict'):
        # gets a dictionary of available sections
        get_config_dict.section_dict = collections.defaultdict()

        # for each section fill the pairs key-value
        for section in config.sections():
            get_config_dict.section_dict[section] = dict(config.items(section))

    # returns a dictionary of dictionary
    return get_config_dict.section_dict

def get_param(cfg_section, cfg_key):

    # How to access a value crresponding on a key in a section
    config_dict = get_config_dict()

    return config_dict[cfg_section][cfg_key]

#section_config = get_config_by_section("AOB")
#print("Config of section AOB")
#print(list(iter(section_config)))


