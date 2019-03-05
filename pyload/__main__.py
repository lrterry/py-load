import yaml
import io


def load_config(path):
    """Loads a yml configuration file from disk

    Args:
        path: The file path to load the config from
    Returns:
        config: A dictionary representing the configuration file
    """
    with io.open(path, 'r') as stream:
        try:
            config = yaml.load(stream)
        except IOError as ex:
            print(ex.message)
            raise ex
    return config


if __name__ == '__main__':
    config = load_config('config.yml')
    print(config)
